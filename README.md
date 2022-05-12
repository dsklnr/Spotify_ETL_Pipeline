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
<img src="https://imgur.com/LORpS5m.png" height="100%" width="100%" alt="Dashboard Screen"/>
<br />
<br />
New parts are either created in-house or by an outsourced party. A toggle group is created to keep track of this selection. In-house parts require a 
machine ID and outsourced parts require a company name.
<br/>
<br/>
Add a New In-House Part:  <br/>
<img src="https://imgur.com/8GWNFWs.png" height="50%" width="50%" alt="Add In-House Part"/>
<br />
<br />
Add an Outsourced Part: <br/>
<img src="https://imgur.com/V5SgYm1.png" height="50%" width="50%" alt="Add Outsourced Part"/>
<br />
<br />
Parts can be modified by selecting a part in the parts table and clicking the modify button below the parts table.
<br />
<br />
Modify a Part  <br/>
<img src="https://imgur.com/P1IYsrB.png" height="50%" width="50%" alt="Modify Part"/>
<br />
<br />
Parts can be deleted by selecting a part in the parts table and clicking the delete button below the parts table.
<br />
<br />
Delete Part:  <br/>
<img src="https://imgur.com/BWLHb1T.png" height="100%" width="100%" alt="Delete Part"/>
<br />
<br />
Add Product:  <br/>
<img src="https://imgur.com/tGQDpIH.png" height="80%" width="80%" alt="Add Product"/>
<br />
<br />
On the right side of the add product form, there are two different parts tables. The top parts table displays all parts. Users should select a part and
click the add button to add the part to the second parts table. The bottom parts table displays a list of all parts required to create the product.
<br />
<br />
Add Parts to the Product:  <br/>
<img src="https://imgur.com/h1oq5eT.png" height="80%" width="80%" alt="Adding Parts to Product"/>
<br />
<br />
Products can be modified by selecting a product in the product table and clicking the modify button below the product table.
<br />
<br />
Update Product:  <br/>
<img src="https://imgur.com/xBNYA1T.png" height="80%" width="80%" alt="Update Product"/>
<br />
<br />
Products can be deleted by selecting a product in the products table and clicking the delete button below the products table. Note that all associated parts must be removed before a product can be deleted.
<br />
<br />
Delete Product:  <br/>
<img src="https://imgur.com/3aaKqWd.png" height="100%" width="100%" alt="Delete Product"/>
<br />
<br />
</p>

<!--
 ```diffd
