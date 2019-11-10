# Database-API-POC
A Python MySQL Database REST API Connection - Proof Of Concept

With this Python Script you can access MySQL directly via a REST Interface.


![Direct Connection](img/direct_connection.png)

<br>
<br>

<h3>Comparison:</h3>

**Native MySQL Call**

![Native MySQL Client](img/Screen2.png) 

<br>

**API MySQL Call**

![Py API MySQL Client](img/Screen1.png) 


<br>
<br>

<h3>Configuration/Installation</h3>

- Install MySQL/MariaDB
- Add your DB credentials in **dbConnection.py**
- Install Python3.x
- sudo sh setup_py.sh
- sh start_server.sh
- Done

<h3>Test Connection</h3>

- Open TestApi.js
- Copy the Command you want to
- Open a blank WebBrowser Tab
- Past the Command and press Enter

<br>
<br>

<h3>Info</h3>

- Falcon was used to define the Interface
- Gunicorn was used to run the Server


<br>
<br>

Since this is a proof of concept, I have not implemented any security measures when accessing the SQL-Server nor protecting and monitoring a running session.
Normally, you would write functions that would call SQL commands and process the data. This would allow a client program to be connected via the REST interface.
The implementation with program specific functions could look like this:

<br>

![Bank Interface](img/bank_connection.png) 
