import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the FBREF page for Newport County stats
url = "https://fbref.com/en/squads/6c15d7e1/Newport-County-Stats#all_stats_standard"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# List of tables you want to scrape, identified by their IDs
table_ids = ['stats_standard_16', 'stats_keeper_16', 'stats_shooting_16',
             'stats_playing_time_16', 'stats_misc_16']

# Initialize an empty dictionary to store DataFrames
dfs = {}

# Loop through each table ID
for table_id in table_ids:
    # Find the table containing player stats
    table = soup.find('table', {'id': table_id})

    # Check if table is found
    if table is None:
        print(f"Table with ID '{table_id}' not found. Skipping...")
    else:
        # Extract the second row of headers to ignore the yellow-highlighted row
        headers = [th.get_text() for th in table.find_all('tr')[1].find_all('th')]

        # Extract rows of data
        rows = []
        for row in table.find('tbody').find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 0:  # Avoid header rows
                row_data = [row.find('th').get_text()] + [cell.get_text() for cell in cells]
                rows.append(row_data)

        # Create a DataFrame
        df = pd.DataFrame(rows, columns=headers[:len(rows[0])])

        # Clean the 'Age' column if it exists
        if 'Age' in df.columns:
            df['Age'] = df['Age'].str.split('-').str[0]  # Keep only the part before the dash

        # Store the DataFrame in the dictionary with the table_id as key
        dfs[table_id] = df

# Save all DataFrames to a multi-sheet Excel file
output_file = "Newport_County_Stats.xlsx"
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    for table_id, df in dfs.items():
        # Use the table_id as the sheet name
        df.to_excel(writer, sheet_name=table_id, index=False)

print(f"DataFrames have been saved to {output_file}")
