<h1>Spotify ETL Pipeline</h1>

<h2>Description</h2>
This project was designed to learn how to make a basic ETL pipeline. The main purpose of this pipeline was to discover who my most listened to artists are.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Pandas</b>
- <b>JSON</b>
- <b>SQLAlchemy</b>
- <b>SQLite</b>
- <b>SQL</b>
- <b>Powershell</b>

<h2>Environments Used </h2>

- <b>Windows 10</b>
- <b>Visual Studio Code</b>

<h2>Program walk-through:</h2>

<p align="left">
To begin this project I had to create an account on spotify. Then I had to listen to at least 20 songs in order for the spotify API to work properly. First I needed to generate a token for my recenly played tracks. I did that here: https://developer.spotify.com/console/get-recently-played/?limit=&after=1652408889&before=. The next day I was able to start creating my ETL pipeline using Python. In Python I created a database location for my sqlite database, a USER_ID that is assigned to my spotify username, and a token that is assigned to the generated token from the previous link.
<br/>
<br/>
<img src="https://imgur.com/LORpS5m.png" height="100%" width="100%" alt="O-Auth Spotify"/>
<br />
<br />
<b>Extract:</b>
<br/>
<br/>
Following the Spotify API documentation, I need to make requests to obtain some data. I have decided to get music data from the last 24 hours (might change this later). Then I run the requests and convert the data to JSON format
<br/>
<br/>
<img src="https://imgur.com/OQ7vSVG.png" height="65%" width="65%" alt="Make Requests"/>
<br />
<br />
Next I initialized arrays for song names, artist names, played at list, and timestamps. Then I created a for loop to search for song names, artist names, played at time, and timestamp within the JSON requests received from the Spotify API that would add data to my arrays. Then I created a dictionary to store columns that display the data inserted into the corresponding array. Finally a Pandas dataframe was created to create a list of columns to display a tableview of the data.
<br/>
<br/>
<img src="https://imgur.com/A9MtYYH.png" height="55%" width="55%" alt="Add Outsourced Part"/>
<br />
<br />
<b>Transform:</b>
<br />
<br />
After extracting the data, it is time to transform the data. Here I am validating the data meets basic requirements for the project. I don't want to recieve and empty data set, I don't want two songs with the same played at time (my primary key), I dont want any null values, and I dont want to recieve songs that aren't from the past 24 hours. If all of these conditions are false, the program will continue to the load stage.
<br />
<br />
<img src="https://imgur.com/E9UEtqW.png" height="55%" width="55%" alt="Modify Part"/> <br />
<img src="https://imgur.com/Flpk3Kh.png" height="30%" width="30%" alt="Modify Part"/>
<br />
<br />
<b>Load:</b>
<br />
<br />
Now the data is ready to be exported into a sql database. This can be done by creating an engine, a connection to the database, and a cursor. Then a simple table is created to hold the data we have collected earlier in the process. The cursor will execute creating the table in the database. Then our data will be passed into the table. If data already exists in the database, the new data will be added below the last value. Then the connection can be closed because the data has successfully been imported to the database.
<br />
<br />
<img src="https://imgur.com/6ZYLyzs.png" height="45%" width="45%" alt="Delete Part"/>
</p>

<!--
 ```diffd
