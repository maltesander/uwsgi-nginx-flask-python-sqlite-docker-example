# uwsgi-nginx-flask-python-sqlite-docker-example
This example creates a dockerized Flask webserver using uWSGI and Nginx with a simple REST API to access a Sqlite database.
The code example demonstrates:
* The setup of uWSGI and Nginx to serve static files
* How to integrate the code and static files into docker using docker-compose
* The access of an internal database via REST API with JSON response

## Instructions

1. Download and unzip the code
2. Install docker and docker-compose
3. Go into the unzipped directory (uwsgi-nginx-flask-python-sqlite-docker-example)
4. Run: "docker-compose up"
    1. Make sure port 80 is not already used
    2. If so, change the port configuration in the docker-compose.override.yml to e.g. 5000
5. Use the REST API e.g.
    1. http://127.0.0.1/run?query=SELECT%20*%20FROM%20student
    2. Goto http://127.0.0.1 and use the provided HTML interface
6. If you changed the port in 4.1, adapt step 5
    1. http://127.0.0.1:5000/run?query=SELECT%20*%20FROM%20student
    2. http://127.0.0.1:5000 for the index page


## About
Detailed explanation can be found here: [tutorial-academy.com](http://tutorial-academy.com/uwsgi-nginx-flask-python-sqlite-docker-example)