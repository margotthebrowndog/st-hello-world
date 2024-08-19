import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")




# Load the Excel file
file_path = r"C:\Users\stuar\PycharmProjects\ncfc\Newport_County_Stats.xlsx"
data_sheets = pd.read_excel(file_path, sheet_name=None)  # sheet_name=None loads all sheets

# Extract each sheet into a unique DataFrame
df_standard = data_sheets.get('stats_standard_16')
df_keeper = data_sheets.get('stats_keeper_16')
df_shooting = data_sheets.get('stats_shooting_16')
df_playing_time = data_sheets.get('stats_playing_time_16')
df_misc = data_sheets.get('stats_misc_16')

# Calculate Metrics
average_age = df_misc['Age']. mean()

st.title('Newport County Stats')
st.divider()

#col1, col2, col3 = st.columns(3)
#col1.metric("Squad Average Age", average_age)
#col2.metric("Most Minutes Played", "tbc")
#col3.metric("Top Scorer", "tbc")

# Debugging: Check column names and data types
#st.write("Standard Stats Columns:", df_standard.columns)

st.divider()


st.metric("Squad Average Age", average_age)

# Squad Age Plot
fig = px.scatter(
    df_standard,
    x='Age',
    y='Min',
    text="Player",
    title="Newport County - Squad Age Profile",
    color_discrete_sequence=['#f79213']  # Custom marker color
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=12,          # Custom font size
        color='black'    # Font color
    ),
    width=1300,           # Custom figure width
    height=800,          # Custom figure height
    title_font=dict(
        size=28,         # Title font size
        family='Roboto'  # Title font family
    )
)

# Customize text annotations
fig.update_traces(
    textposition='top center',   # Position text above the marker
    textfont=dict(
        color='white'            # Set the text color to white
    )
)

fig.add_shape(
    type="rect",
    x0=24, y0=0, x1=30, y1=df_standard['Min'].max(),
    fillcolor="grey", opacity=0.2, layer="below", line_width=0,
)

# Custom y-axis category labels
fig.add_annotation(
    x=0.15, y=0.8, text="YOUTH", font=dict(size=30, color="grey"), showarrow=False, xref="paper", yref="paper", textangle=-90
)
fig.add_annotation(
    x=0.53, y=0.5, text="PRIME", font=dict(size=30, color="grey"), showarrow=False, xref="paper", yref="paper", textangle=-90
)
fig.add_annotation(
    x=0.88, y=0.2, text="EXPERIENCE", font=dict(size=30, color="grey"), showarrow=False, xref="paper", yref="paper", textangle=-90
)

# Display the plot (replace with st.plotly_chart(fig) if using Streamlit)
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')

st.divider()

# Goals Plot
modified_df = df_standard.sort_values(by='Gls', ascending=False)


# Customize plot
fig = px.bar(
    modified_df.head(5),
    x='Gls',
    y='Player',
    title="Most Goals",
    orientation='h',
    color_discrete_sequence=['#f79213'],  # Custom bar color
    text='Gls'  # Automatically display the value of each bar
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=22,          # Custom font size
        color='black'    # Font color
    ),
    width=800,           # Custom figure width
    height=600,          # Custom figure height
    title_font=dict(
        size=28,          # Title font size
        family='Roboto'   # Title font family
    ),
    yaxis={'categoryorder': 'total ascending'}  # Largest bar on top
)

# Position the text inside the bars and set the color to black
fig.update_traces(
    textposition='inside',  # Position the text just inside the end of the bar
    textfont=dict(
        color='black',
        size=22,
        family='Roboto',
    )
)

# Display the plot
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')

st.divider()

# Shots on target per 90 Plot
modified_df = df_shooting.sort_values(by='SoT/90', ascending=False)


# Customize plot
fig = px.bar(
    modified_df.head(5),
    x='SoT/90',
    y='Player',
    title="Most Shots on Target per 90",
    orientation='h',
    color_discrete_sequence=['#f79213'],  # Custom bar color
    text='SoT/90'  # Automatically display the value of each bar
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=22,          # Custom font size
        color='black'    # Font color
    ),
    width=800,           # Custom figure width
    height=600,          # Custom figure height
    title_font=dict(
        size=28,          # Title font size
        family='Roboto'   # Title font family
    ),
    yaxis={'categoryorder': 'total ascending'}  # Largest bar on top
)

# Position the text inside the bars and set the color to black
fig.update_traces(
    textposition='inside',  # Position the text just inside the end of the bar
    textfont=dict(
        color='black',
        size=22,
        family='Roboto',
    )
)

# Display the plot
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')

st.divider()

# Assists Plot
modified_df = df_standard.sort_values(by='Ast', ascending=False)


# Customize plot
fig = px.bar(
    modified_df.head(5),
    x='Ast',
    y='Player',
    title="Most Assists",
    orientation='h',
    color_discrete_sequence=['#f79213'],  # Custom bar color
    text='Ast'  # Automatically display the value of each bar
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=22,          # Custom font size
        color='black'    # Font color
    ),
    width=800,           # Custom figure width
    height=600,          # Custom figure height
    title_font=dict(
        size=28,          # Title font size
        family='Roboto'   # Title font family
    ),
    yaxis={'categoryorder': 'total ascending'}  # Largest bar on top
)

# Position the text inside the bars and set the color to black
fig.update_traces(
    textposition='inside',  # Position the text just inside the end of the bar
    textfont=dict(
        color='black',
        size=22,
        family='Roboto',
    )
)

# Display the plot
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')

st.divider()


# Interceptions Plot
modified_df = df_misc.sort_values(by='Int', ascending=False)


# Customize plot
fig = px.bar(
    modified_df.head(5),
    x='Int',
    y='Player',
    title="Most Interceptions",
    orientation='h',
    color_discrete_sequence=['#f79213'],  # Custom bar color
    text='Int'  # Automatically display the value of each bar
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=22,          # Custom font size
        color='black'    # Font color
    ),
    width=800,           # Custom figure width
    height=600,          # Custom figure height
    title_font=dict(
        size=28,          # Title font size
        family='Roboto'   # Title font family
    ),
    yaxis={'categoryorder': 'total ascending'}  # Largest bar on top
)

# Position the text inside the bars and set the color to black
fig.update_traces(
    textposition='inside',  # Position the text just inside the end of the bar
    textfont=dict(
        color='black',
        size=22,
        family='Roboto',
    )
)

# Display the plot
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')

st.divider()

# Tackles Plot
modified_df = df_misc.sort_values(by='TklW', ascending=False)


# Customize plot
fig = px.bar(
    modified_df.head(5),
    x='TklW',
    y='Player',
    title="Most Tackles Won",
    orientation='h',
    color_discrete_sequence=['#f79213'],  # Custom bar color
    text='TklW'  # Automatically display the value of each bar
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=22,          # Custom font size
        color='black'    # Font color
    ),
    width=800,           # Custom figure width
    height=600,          # Custom figure height
    title_font=dict(
        size=28,          # Title font size
        family='Roboto'   # Title font family
    ),
    yaxis={'categoryorder': 'total ascending'}  # Largest bar on top
)

# Position the text inside the bars and set the color to black
fig.update_traces(
    textposition='inside',  # Position the text just inside the end of the bar
    textfont=dict(
        color='black',
        size=22,
        family='Roboto',
    )
)

# Display the plot
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')

st.divider()

# Crosses Plot
modified_df = df_misc.sort_values(by='Crs', ascending=False)


# Customize plot
fig = px.bar(
    modified_df.head(5),
    x='Crs',
    y='Player',
    title="Most Crosses",
    orientation='h',
    color_discrete_sequence=['#f79213'],  # Custom bar color
    text='Crs'  # Automatically display the value of each bar
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=22,          # Custom font size
        color='black'    # Font color
    ),
    width=800,           # Custom figure width
    height=600,          # Custom figure height
    title_font=dict(
        size=28,          # Title font size
        family='Roboto'   # Title font family
    ),
    yaxis={'categoryorder': 'total ascending'}  # Largest bar on top
)

# Position the text inside the bars and set the color to black
fig.update_traces(
    textposition='inside',  # Position the text just inside the end of the bar
    textfont=dict(
        color='black',
        size=22,
        family='Roboto',
    )
)

# Display the plot
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')


# Fouls Plot
modified_df = df_misc.sort_values(by='Fls', ascending=False)


# Customize plot
fig = px.bar(
    modified_df.head(5),
    x='Fls',
    y='Player',
    title="Most Fouls",
    orientation='h',
    color_discrete_sequence=['#f79213'],  # Custom bar color
    text='Fls'  # Automatically display the value of each bar
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=22,          # Custom font size
        color='black'    # Font color
    ),
    width=800,           # Custom figure width
    height=600,          # Custom figure height
    title_font=dict(
        size=28,          # Title font size
        family='Roboto'   # Title font family
    ),
    yaxis={'categoryorder': 'total ascending'}  # Largest bar on top
)

# Position the text inside the bars and set the color to black
fig.update_traces(
    textposition='inside',  # Position the text just inside the end of the bar
    textfont=dict(
        color='black',
        size=22,
        family='Roboto',
    )
)

# Display the plot
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')

# Most Fouled Plot
modified_df = df_misc.sort_values(by='Fld', ascending=False)


# Customize plot
fig = px.bar(
    modified_df.head(5),
    x='Fld',
    y='Player',
    title="Most Fouled",
    orientation='h',
    color_discrete_sequence=['#f79213'],  # Custom bar color
    text='Fld'  # Automatically display the value of each bar
)

# Further customization with layout
fig.update_layout(
    font=dict(
        family='Arial',  # Custom font family
        size=22,          # Custom font size
        color='black'    # Font color
    ),
    width=800,           # Custom figure width
    height=600,          # Custom figure height
    title_font=dict(
        size=28,          # Title font size
        family='Roboto'   # Title font family
    ),
    yaxis={'categoryorder': 'total ascending'}  # Largest bar on top
)

# Position the text inside the bars and set the color to black
fig.update_traces(
    textposition='inside',  # Position the text just inside the end of the bar
    textfont=dict(
        color='black',
        size=22,
        family='Roboto',
    )
)

# Display the plot
st.plotly_chart(fig)
st.caption('_Data Source: FBREF_')


