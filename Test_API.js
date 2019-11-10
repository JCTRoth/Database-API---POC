/*
    Run this code in a blank tab in your Browser.
*/


/*
GET
Copy this to your browser Console to Test the API
*/
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var response = xhttp.responseText;
        console.log(response);
    }
};
xhttp.open("GET", "http://localhost:8000/database", true);

xhttp.send();


/*
POST
Copy this to your browser Console to Test the API
*/
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var response = xhttp.responseText;
        console.log(response);
    }
};
xhttp.open("POST", "http://127.0.0.1:8000/database", true);

xhttp.send('{ "sql": "SHOW DATABASES" }');