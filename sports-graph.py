from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px  # pip install plotly==5.0.0
import plotly.graph_objs as go
import pandas as pd  # pip install pandas
import csv
# pip install statsmodels # for scatter plot graph with an average line


# Source - https://www.basketball-reference.com/leagues/NBA_2022_per_game.html
# Source - https://www.basketball-reference.com/leagues/NBA_2022_totals.html

# df = pd.read_csv("https://raw.githubusercontent.com/sammy030609/COMPScode/master/stats_nba_player_data_bballref_2021-22.csv")

df = pd.read_csv('fantasy_basketball_points.csv')  # reads csv file with converted fantasy points that user inputted

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])  # dash app theme for the webpage
mytitle = dcc.Markdown(children='# Visualization of Fantasy Basketball Stats')  # title of the web page
mygraph = dcc.Graph(figure={})  # empty graph for now
dropdown = dcc.Dropdown(options=['Total Fantasy Points Scored (Bar Graph)',
                                 'Total Fantasy Points Scored (Scatter Plot)',
                                 'Total Fantasy Points Scored based on Total Points Scored (Scatter Plot)',
                                 'Breakdown of Points Scored from Each Statistic',
                                 'Breakdown of Positive and Negative Fantasy Points',
                                 'Breakdown of True Point Totals for Field Goals and Free Throws',
                                 'Chart of Fantasy Points per Player'],
                        value='Total Fantasy Points Scored (Bar Graph)',
                        clearable=False)
# dropdown is what the user chooses for which graph is displayed on the web app
# options are what each dropdown item is named
# value is the default graph that is shown


# app.layout takes the 3 variables mytitle, mygraph, dropdown
app.layout = dbc.Container([mytitle, mygraph, dropdown])

# Conversions of CSV file to work with the data format that the graphs take
with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col = {'Player': []}  # create dictionary with key 'Player'
    for record in reader:
        player_col['Player'].append(record['Player'])
        # takes each name from the player column of the csv file and
        # puts it into the values of the dictionary with key 'Player'

player_list = player_col['Player']  # changes 'Player' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col1 = {'FGA': []}  # create dictionary with key 'FGA'
    for record in reader:
        player_col1['FGA'].append(record['FGA'])
        # takes each value from the 'FGA' column of the csv file and
        # puts it into the values of the dictionary with key 'FGA'

player_col1a = player_col1['FGA']
player_fga = [eval(i) for i in player_col1a]  # changes 'FGA' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col2 = {'FTA': []}
    for record in reader:
        player_col2['FTA'].append(record['FTA'])

player_col2a = player_col2['FTA']
player_fta = [eval(i) for i in player_col2a]  # changes 'FTA' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col3 = {'TO': []}
    for record in reader:
        player_col3['TO'].append(record['TO'])

player_col3a = player_col3['TO']
player_to = [eval(i) for i in player_col3a]  # changes 'TO' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col4 = {'FGM': []}
    for record in reader:
        player_col4['FGM'].append(record['FGM'])

player_col4a = player_col4['FGM']
player_fgm = [eval(i) for i in player_col4a]  # changes 'FGM' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col5 = {'FTM': []}
    for record in reader:
        player_col5['FTM'].append(record['FTM'])

player_col5a = player_col5['FTM']
player_ftm = [eval(i) for i in player_col5a]  # changes 'FTM' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col6 = {'_3PM': []}
    for record in reader:
        player_col6['_3PM'].append(record['_3PM'])

player_col6a = player_col6['_3PM']
player_3pm = [eval(i) for i in player_col6a]  # changes '_3PM' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col7 = {'REB': []}
    for record in reader:
        player_col7['REB'].append(record['REB'])

player_col7a = player_col7['REB']
player_reb = [eval(i) for i in player_col7a]  # changes 'REB' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col8 = {'AST': []}
    for record in reader:
        player_col8['AST'].append(record['AST'])

player_col8a = player_col8['AST']
player_ast = [eval(i) for i in player_col8a]  # changes 'AST' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col9 = {'STL': []}
    for record in reader:
        player_col9['STL'].append(record['STL'])

player_col9a = player_col9['STL']
player_stl = [eval(i) for i in player_col9a]  # changes 'STL' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col10 = {'BLK': []}
    for record in reader:
        player_col10['BLK'].append(record['BLK'])

player_col10a = player_col10['BLK']
player_blk = [eval(i) for i in player_col10a]  # changes 'BLK' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col11 = {'PTS': []}
    for record in reader:
        player_col11['PTS'].append(record['PTS'])

player_col11a = player_col11['PTS']
player_pts = [eval(i) for i in player_col11a]  # changes 'PTS' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col12 = {'FGM_pm': []}
    for record in reader:
        player_col12['FGM_pm'].append(record['FGM_pm'])

player_col12a = player_col12['FGM_pm']
player_fgpm = [eval(i) for i in player_col12a]  # changes 'FGM_pm' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col13 = {'FT_pm': []}
    for record in reader:
        player_col13['FT_pm'].append(record['FT_pm'])

player_col13a = player_col13['FT_pm']
player_ftpm = [eval(i) for i in player_col13a]  # changes 'FT_pm' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col14 = {'NEGPTS': []}
    for record in reader:
        player_col14['NEGPTS'].append(record['NEGPTS'])

player_col14a = player_col14['NEGPTS']
player_negpts = [eval(i) for i in player_col14a]  # changes 'NEGPTS' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col15 = {'POSPTS': []}
    for record in reader:
        player_col15['POSPTS'].append(record['POSPTS'])

player_col15a = player_col15['POSPTS']
player_pospts = [eval(i) for i in player_col15a]  # changes 'POSPTS' column from csv file to an array list

with open('fantasy_basketball_points.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    player_col16 = {'TOTPTS': []}
    for record in reader:
        player_col16['TOTPTS'].append(record['TOTPTS'])

player_col16a = player_col16['TOTPTS']
player_totpts = [eval(i) for i in player_col16a]  # changes 'TOTPTS' column from csv file to an array list


# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(mygraph, component_property='figure'),
    Input(dropdown, component_property='value')
)
# function to show the different graphs that the user selects from the dropdown menu
def update_graph(user_input):
    if user_input == 'Total Fantasy Points Scored (Bar Graph)':     # bar graph of Total Fantasy Points Scored
        fig = px.bar(data_frame=df,
                     x="Player",
                     y="TOTPTS",
                     color="Pos",
                     labels={"TOTPTS": "Total Fantasy Points"},
                     title="Total Fantasy Points Scored (Bar Graph)")

    elif user_input == 'Total Fantasy Points Scored (Scatter Plot)':    # scatter plot of Total Fantasy Points Scored
        fig = px.scatter(data_frame=df,
                         x="Player",
                         y="TOTPTS",
                         color="Pos",
                         symbol="Pos",
                         labels={"TOTPTS": "Total Fantasy Points"},
                         title="Total Fantasy Points Scored (Scatter Plot)"
                         )

    elif user_input == 'Total Fantasy Points Scored based on Total Points Scored (Scatter Plot)':
        # scatter plot of Total Fantasy Points Scored on Y axis and Total Points Scored on X axis
        fig = px.scatter(data_frame=df,
                         x="PTS",
                         y="TOTPTS",
                         color="Pos",
                         symbol="Pos",
                         hover_data=['Player'],
                         trendline="ols",   # this line calculates average for each position
                                            # uses 'pip install statsmodels' to calculate
                         labels={"TOTPTS": "Total Fantasy Points"},
                         title="Total Fantasy Points Scored based on Total Points Scored (Scatter Plot)"
                         )

    elif user_input == 'Breakdown of Points Scored from Each Statistic':
        # stacked bar graph to show each category of points scored for each player
        fig = go.Figure(data=[go.Bar(x=player_list, y=player_fga, name='FGA'),
                              go.Bar(x=player_list, y=player_fta, name='FTA'),
                              go.Bar(x=player_list, y=player_to, name='TO'),
                              go.Bar(x=player_list, y=player_fgm, name='FGM'),
                              go.Bar(x=player_list, y=player_ftm, name='FTM'),
                              go.Bar(x=player_list, y=player_3pm, name='3PM'),
                              go.Bar(x=player_list, y=player_reb, name='REB'),
                              go.Bar(x=player_list, y=player_ast, name='AST'),
                              go.Bar(x=player_list, y=player_stl, name='STL'),
                              go.Bar(x=player_list, y=player_blk, name='BLK'),
                              go.Bar(x=player_list, y=player_pts, name='PTS')])

        fig.update_layout(barmode='relative',
                          title="Breakdown of Points Scored from Each Statistic",
                          yaxis_title="Fantasy Points Scored")

        fig.add_shape(type='line',
                      x0=player_list[0],
                      y0=0,
                      x1=player_list[604],
                      y1=0,
                      line=dict(color='green', ),
                      xref='x',
                      yref='y'
                      )
                    # adds a green line at x=0 to differentiate negative and positive points

    elif user_input == 'Breakdown of Positive and Negative Fantasy Points':
        # stacked bar graph to show total positive and total negative points
        fig = go.Figure(data=[go.Bar(x=player_list, y=player_negpts,
                                     name='Total Negative Fantasy Points\n (FGA, FTA, TO)'),
                              go.Bar(x=player_list, y=player_pospts,
                                     name='Total Positive Fantasy Points\n (FGM, FTM, 3PM, REB, AST, STL, BLK, PTS)'),
                              ])

        fig.update_layout(barmode='relative',
                          title="Breakdown of Positive and Negative Fantasy Points",
                          yaxis_title="Fantasy Points Scored")

    elif user_input == 'Breakdown of True Point Totals for Field Goals and Free Throws':
        # stacked bar graph to show positive/negative points from Field Goals (-FGA + FGM)
        # and show positive/negative points from Free Throws (-FTA + FTM)
        fig = go.Figure(data=[go.Bar(x=player_list, y=player_fgpm,
                                     name='Total Fantasy Points for Field Goals (-FGA + FGM)'),
                              go.Bar(x=player_list, y=player_ftpm,
                                     name='Total Fantasy Points for Free Throws (-FTA + FTM)'),
                              ])

        fig.update_layout(barmode='relative',
                          title="Breakdown of True Point Totals for Field Goals and Free Throws",
                          yaxis_title="Fantasy Points Scored")

    elif user_input == 'Chart of Fantasy Points per Player':
        # table of fantasy conversion statstics from csv file
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[df.Rk, df.Player, df.Pos, df.Team, df.FGM, df.FGA, df.FTM, df.FTA, df._3PM, df.REB,
                               df.AST, df.STL, df.BLK, df.TO, df.PTS, df.FGM_pm, df.FT_pm, df.NEGPTS, df.POSPTS,
                               df.TOTPTS],
                       fill_color='lightcyan',
                       align='left'))
        ])

    return fig  # returns graphs or chart based on user's input


# Run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8054)   # which server the web app is running on when active
