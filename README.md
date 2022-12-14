# Replication Instructions
- The software used for this project is IDE [PyCharm CE](https://www.jetbrains.com/pycharm/download/#section=mac) to run the python files **sports_graph.py** and **stat_conversion.py**. Download the free communtity version and install it on your computer
- To retrive NBA stat totals to convert them to fantasy points, go to [basketball-reference.com](https://www.basketball-reference.com/leagues/NBA_2022_totals.html) where the webpage shows the totals of NBA player's stats. Next to **Player Totals**, click on **Share and Export** and on the dropdown menu, click **Get Table as CSV (for Excel)**
 ![CSVtable](https://raw.githubusercontent.com/sammy030609/COMPScode/main/README%20images/bball-reference1.png)
Copy the contents on the webpage and add it to a blank text file (TextEdit on Mac or NotePad on Windows). Save the file as a csv file (For example: stats_nba_player_data_totals_bballref_2021-22.csv)
- Create a new project in PyCharm CE and add the files **sports_graph.py**, **stat_conversion.py**, and the csv file with the basketball data to the project folder
![project_folder](https://raw.githubusercontent.com/sammy030609/COMPScode/main/README%20images/project_folder.png)
- Next, multiple libraries need to be installed for these files to run: **pandas, dash, dash-bootstrap-components, plotly, statsmodels**. To install these, click the terminal buttom at the bottom of PyCharm and to install each library, type `pip install pandas`, `pip install dash`, etc until all of these libraries are installed. For **plotly**, use version 5.0.0 when installing which looks like `pip install plotly==5.0.0`

- Open **stat_conversion.py** and replace the csv file name with what you named the csv file of the basketball stats totals `df  =  pd.read_csv('your csv file name')`

- Once the csv file name is entered, run the file and it allows the user to enter the fantasy points worth of each stat (EX: FGM = 2 Fantasy points, FGA = -1 Fantasy Points) shown in the terminal of PyCharm ![stat_conv](https://raw.githubusercontent.com/sammy030609/COMPScode/main/README%20images/stat_conv.png)
- Once the user has entered all the conversion data, then a new file named **fantasy_basketball_points.csv** will be added to the project folder with the rest of the files. This file is used in **sports_graph.py** which uses the data from the new csv file in the code.
- To get the website to start, run the file **sports_graph.py** and in the terminal at the bottom of PyCharm, it should show a link for the webapp ![link-pic](https://raw.githubusercontent.com/sammy030609/COMPScode/main/README%20images/link.png)
- Click the link and the webapp should be up and working locally on a web browser
![webapp](https://raw.githubusercontent.com/sammy030609/COMPScode/main/README%20images/web_app.png)
