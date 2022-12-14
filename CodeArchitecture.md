# Code Architecture Overview

## stat_conversion.py Code

```  
import pandas as pd   
  
df = pd.read_csv('stats_nba_player_data_totals_bballref_2021-22 copy.csv')    
df2 = pd.DataFrame({})
```
- Variable df reads the csv file with basketball statistic data from [basketball-reference](https://www.basketball-reference.com/leagues/NBA_2022_totals.html) using the pandas library
- Variable df2 becomes an empty dataframe that will store the new csv data after the stats are converted based on user input

```
a = int(input("Enter FGM fantasy points value: "))  
b = int(input("Enter FGA fantasy points value: "))  
j = int(input("Enter FTM fantasy points value: "))  
k = int(input("Enter FTA fantasy points value: "))  
c = int(input("Enter 3PM fantasy points value: "))  
d = int(input("Enter REB fantasy points value: "))  
e = int(input("Enter AST fantasy points value: "))  
f = int(input("Enter STL fantasy points value: "))  
g = int(input("Enter BLK fantasy points value: "))  
h = int(input("Enter TO fantasy points value: "))  
i = int(input("Enter PTS fantasy points value: "))
```
- Each lettered variable takes the user's input for the fantasy point value of each statistic

```
df2['Player'] = df['Player']    #copies player name from csv file  
df2['Pos'] = df['Pos']          # copies player position from csv file  
df2['Team'] = df['Tm']          # copies player team from csv file  
df2['FGM'] = (df['FG'] * a)      # FGM conversion to fantasy points  
df2['FGA'] = (df['FGA'] * b)      # FGA conversion to fantasy points  
df2['FTM'] = (df['FT'] * j)       # FTM conversion to fantasy points  
df2['FTA'] = (df['FTA'] * k)      # FTA conversion to fantasy points  
df2['_3PM'] = (df['3P'] * c)       # 3PM conversion to fantasy points  
df2['REB'] = (df['TRB'] * d)      # REB conversion to fantasy points  
df2['AST'] = (df['AST'] * e)      # AST conversion to fantasy points  
df2['STL'] = (df['STL'] * f)      # STL conversion to fantasy points  
df2['BLK'] = (df['BLK'] * g)      # BLK conversion to fantasy points  
df2['TO'] = (df['TOV'] * h)       # TO conversion to fantasy points  
df2['PTS'] = (df['PTS'] * i)      # PTS conversion to fantasy points
```
- df2 copies 'Player', 'Pos', and 'Tm' from the 'stats_nba_player_data_totals_bballref_2021-22 copy.csv' file. The rest are conversions of the data from the csv file to fantasy points worth. They are multiplied by the user's input according to the variable. 

```
df2['FGM_pm'] = ((df['FGA'] * b) + (df['FG'] * a)) 
df2['FT_pm'] = ((df['FTA'] * k) + (df['FT'] * j)) 
df2['NEGPTS'] = ((df['TOV'] * h) + (df['FTA'] * k) + (df['FGA'] * b))
df2['POSPTS'] = ((df['FG'] * a) + (df['FT'] * j) + (df['3P'] * c) + 
				(df['TRB'] * d) + (df['AST'] * e) + (df['STL'] * f)  
                 + (df['BLK'] * g) + (df['PTS'] * i))        
df2['TOTPTS'] = ((df['TOV'] * h) + (df['FTA'] * k) + (df['FGA'] * b)) + 
					((df['FG'] * a) + (df['FT'] * j) + (df['3P'] * c) + 
					(df['TRB'] * d) + (df['AST'] * e) + (df['STL'] * f) + 
					(df['BLK'] * g) + (df['PTS'] * i))                                                   
df2['Rk'] = df['Rk']
```
- 'FGM_pm' calculates negative/positive fantasy points for FGs based on FGM and FGA difference
- 'FT_pm' calculates negative/positive fantasy points for FTs based on FTM and FTA difference
- 'NEGPTS' calculates total negative fantasy points from 'TOV', 'FTA' and 'FGA' added up
- 'POSPTS' calculates calculates total positive fantasy points from 'FGM', 'FTM', '_3PM', 'REB', 'AST', 'STL', 'BLK', 'PTS' added up
- 'TOTPTS' is calculated by adding 'NEGPTS' with 'POSPTS' which equals total fantasy points per each player
- df2['Rk'] copies the 'Rk' category from the csv file

```
df2.to_csv('fantasy_basketball_points.csv')
```
- Creates new csv file named 'fantasy_basketball_points.csv'with user's fantasy points conversions

---
## sports_graph.py Code
```
from dash import Dash, dcc, Output, Input  
import dash_bootstrap_components as dbc 
import plotly.express as px  
import plotly.graph_objs as go  
import pandas as pd 
import csv
```
- Libraries that are imported in the file for the code to run

```
df = pd.read_csv('fantasy_basketball_points.csv')
```
- reads the csv file with converted fantasy points

```
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX]) 
mytitle = dcc.Markdown(children='# Visualization of Fantasy Basketball Stats')  
mygraph = dcc.Graph(figure={})  
dropdown = dcc.Dropdown(options=['Total Fantasy Points Scored (Bar Graph)',  
  'Total Fantasy Points Scored (Scatter Plot)',  
  'Total Fantasy Points Scored based on Total Points Scored (Scatter Plot)',  
  'Breakdown of Points Scored from Each Statistic',  
  'Breakdown of Positive and Negative Fantasy Points',  
  'Breakdown of True Point Totals for Field Goals and Free Throws',  
  'Chart of Fantasy Points per Player'],  
  value='Total Fantasy Points Scored (Bar Graph)',  
  clearable=False)

app.layout = dbc.Container([mytitle, mygraph, dropdown])
```
- The `app` variable uses the dash app theme for the webpage
- The `mytitle` vairable is assigned the website's name 
- `mygraph` variable is assigned an empty figure because it waits for hte user's input from the dropdown boc
- `dropdown` variable codes a box that has the names in it for the user to pick. It will corespond to what graph is displayed
- `app.layout` takes the `dropdown`, `mytitle`, and `mygraph`variables to create the webpage

```
with open('fantasy_basketball_points.csv', mode='r') as infile:  
    reader = csv.DictReader(infile)  
    player_col = {'Player': []}  
	for record in reader:  
        player_col['Player'].append(record['Player'])  
       
player_list = player_col['Player'] 
  
with open('fantasy_basketball_points.csv', mode='r') as infile:  
    reader = csv.DictReader(infile)  
    player_col1 = {'FGA': []}  
    for record in reader:  
        player_col1['FGA'].append(record['FGA'])  
       
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
player_totpts = [eval(i) for i in player_col16a]
```
- This chunk of code takes the csv file data and converts each category into a list
-  `with open('fantasy_basketball_points.csv', mode='r') as infile:` function reads the csv file and `player_col#` variable is assigned a dictionary with the category as the key. It takes all the data from the category and is stored in the value of the dictionary. 
- `player_col#a = player_col#['Category']` takes the values from the dictionary of the category and stores it as a list
- `player_category = [eval(i) for i in player_col#a]`converts the strings of the list and turns each value into an integer

```
def update_graph(user_input):  
    if user_input == 'Total Fantasy Points Scored (Bar Graph)':    
		  fig = px.bar(data_frame=df,  
				x="Player",  
			    y="TOTPTS",  
				color="Pos",  
				labels={"TOTPTS": "Total Fantasy Points"},  
				title="Total Fantasy Points Scored (Bar Graph)")  
 ```
 - `def update_graph(user_input)` is a function that takes what the user selects from the dropdown menu of names
 - This if statement creates a bar graph of Total Fantasy Points Scored
 - The bar graph is created by assigning`fig` to `px.bar`
 - `data_frame=df` retrieves the data from the csv file 
 - x and y data is retrieved from the categories of the csv file
 - labels gives the category a new name
 ```
    elif user_input == 'Total Fantasy Points Scored (Scatter Plot)': 
		  fig = px.scatter(data_frame=df,  
				x="Player",  
				y="TOTPTS",  
				color="Pos",  
				symbol="Pos",  
				labels={"TOTPTS": "Total Fantasy Points"},  
				title="Total Fantasy Points Scored (Scatter Plot)")  
```
- This if statement creates a scatter plot of Total Fantasy Points Scored
-  The scatter plot is created by assigning `fig` to `px.scatter`
```  
    elif user_input == 'Total Fantasy Points Scored based on Total Points Scored (Scatter Plot)':  
		  fig = px.scatter(data_frame=df,  
				x="PTS",  
				y="TOTPTS",  
				color="Pos",  
				symbol="Pos",  
				hover_data=['Player'],  
				trendline="ols", 
				labels={"TOTPTS": "Total Fantasy Points"},  
				title="Total Fantasy Points Scored based on Total Points Scored (Scatter Plot)")  
  ```  
  - This if statement creates a scatter plot of Total Fantasy Points Scored based on Total Points Scored
-  The scatter plot is created by assigning `fig` to `px.scatter`
- `hover_data` is used to show the player's name when hovering over the symbol on the scatter plot
- `trendline` is used to calculate an average line for each position in basketball
  
```
  elif user_input == 'Breakdown of Points Scored from Each Statistic':  
		  fig = go.Figure(data=[
				go.Bar(x=player_list, y=player_fga, name='FGA'),  
				go.Bar(x=player_list, y=player_fta, name='FTA'),  
				go.Bar(x=player_list, y=player_to, name='TO'),  
				go.Bar(x=player_list, y=player_fgm, name='FGM'),  
				go.Bar(x=player_list, y=player_ftm, name='FTM'),  
				go.Bar(x=player_list, y=player_3pm, name='3PM'),  
				go.Bar(x=player_list, y=player_reb, name='REB'),  
				go.Bar(x=player_list, y=player_ast, name='AST'),  
				go.Bar(x=player_list, y=player_stl, name='STL'),  
				go.Bar(x=player_list, y=player_blk, name='BLK'),  
				go.Bar(x=player_list, y=player_pts, name='PTS')
				])  
  
        fig.update_layout(
		        barmode='relative',  
				title="Breakdown of Points Scored from Each Statistic",  
				 yaxis_title="Fantasy Points Scored")  
  
        fig.add_shape(
		        type='line',  
				x0=player_list[0],  
				y0=0,  
				x1=player_list[604],  
				y1=0,  
				line=dict(color='green', ),  
				xref='x',  
				yref='y'  
				)  
```
- This if statement creates a stacked bar graph to show each category of points scored for each player
- `go.Bar()` is used for each category and creates a bar graph using the data conversions 
-  `fig.update_layout()` changes the bar graph into stacked bar graph by changing the `barmode='relative'`
- `fig.add_shape()` adds a white line at the x=0 axis to differentiate between negative and positive points
   
 ```                 
    elif user_input == 'Breakdown of Positive and Negative Fantasy Points':   
		  fig = go.Figure(data=[
				go.Bar(x=player_list, y=player_negpts,  
				  name='Total Negative Fantasy Points\n (FGA, FTA, TO)'),  
				go.Bar(x=player_list, y=player_pospts,  
				  name='Total Positive Fantasy Points\n (FGM, FTM, 3PM, REB, 			
						AST, STL, BLK, PTS)'),  
				])  
        fig.update_layout(
		        barmode='relative',  
				title="Breakdown of Positive and Negative Fantasy Points",  
				yaxis_title="Fantasy Points Scored") 			
```
 - This if statement creates a stacked bar graph to show total positive and total negative fantasy points

```   
    elif user_input == 'Breakdown of True Point Totals for Field Goals and Free Throws':  
        fig = go.Figure(data=[
		        go.Bar(x=player_list, y=player_fgpm,  
				name='Total Fantasy Points for Field Goals (-FGA + FGM)'),  
				go.Bar(x=player_list, y=player_ftpm,  
				name='Total Fantasy Points for Free Throws (-FTA + FTM)'),  
				])  
        fig.update_layout(
		        barmode='relative',  
				title="Breakdown of True Point Totals for Field Goals and Free Throws",  
				yaxis_title="Fantasy Points Scored"
				)  
 ```
 
 - This if statment creates a stacked bar chart for Field Goal and Free Throw fantasy points
```  
    elif user_input == 'Chart of Fantasy Points per Player':   
		  fig = go.Figure(data=[go.Table(  
		        header=dict(values=list(df.columns),  
				fill_color='paleturquoise',  
				align='left'),  
				cells=dict(
					values=[df.Rk, df.Player, df.Pos, df.Team, df.FGM, df.FGA, 	
					df.FTM, df.FTA, df._3PM, df.REB, df.AST, df.STL, df.BLK, df.TO, df.PTS, 
					df.FGM_pm, df.FT_pm, df.NEGPTS, df.POSPTS, df.TOTPTS],  
				fill_color='lightcyan',  
				align='left'))  
		        ])  
  
    return fig  
```
- This if statement produces a chart of the csv file data
- `return fig` returns graphs or chart based on user's input on dropdown menu

```
if __name__ == '__main__':  
    app.run_server(debug=True, port=8054)
```
- When file is running, this allows the app to be ran on a web browser and provides a link to access it