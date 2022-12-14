import pandas as pd  # pip install pandas

df = pd.read_csv('stats_nba_player_data_totals_bballref_2021-22 copy.csv')
# reads csv file with basketball statistic data
# make sure the csv file is in the same folder as this python file (stat_conversion.py)

df2 = pd.DataFrame({})      # creates a dataframe for a new csv file for information to be stored

# takes input from user to convert basketball stats to fantasy points
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


# copies converted stats into the dataframe
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

df2['FGM_pm'] = ((df['FGA'] * b) + (df['FG'] * a))      # calculates negative/positive fantasy points for FGs
                                                        #  based on FGM and FGA difference

df2['FT_pm'] = ((df['FTA'] * k) + (df['FT'] * j))       # calculates negative/positive fantasy points for FTs
                                                        # based on FTM and FTA difference

df2['NEGPTS'] = ((df['TOV'] * h) + (df['FTA'] * k) + (df['FGA'] * b))   # calculates total negative fantasy points

df2['POSPTS'] = ((df['FG'] * a) + (df['FT'] * j) + (df['3P'] * c) + (df['TRB'] * d) + (df['AST'] * e) + (df['STL'] * f)
                 + (df['BLK'] * g) + (df['PTS'] * i))           # calculates total positive fantasy points

df2['TOTPTS'] = ((df['TOV'] * h) + (df['FTA'] * k) + (df['FGA'] * b)) + ((df['FG'] * a) + (df['FT'] * j) +
        (df['3P'] * c) + (df['TRB'] * d) + (df['AST'] * e) + (df['STL'] * f) + (df['BLK'] * g) + (df['PTS'] * i))
                                                        # calculates total fantasy points

df2['Rk'] = df['Rk']    # copies player rank

df2.to_csv('fantasy_basketball_points.csv')         # creates new csv file with user's fantasy points conversions



