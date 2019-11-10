# Pip - Imports
from falcon import falcon
import json

# Project - Imports
from dbConnection import dbConnection

# DB-Obj
internal_dbConnection = dbConnection();  # Init. DB Connection


#
# One Class - One Endpoint
#

class Example(object):
    def on_get(self, req, resp):
        resp.body = json.dumps("This is a test")


class DataBase(object):

    def on_post(self, req, resp):
        if req.content_length:  # length > 0
            req_stream = req.bounded_stream.read()
            req_dict = json.loads(req_stream.decode('utf-8'))

        if req_dict["sql"] != None:  # If request is formated correctly
            return_value = internal_dbConnection.run_sql(req_dict["sql"])  # Run SQL Command
            if return_value == "Error":
                resp.body = '{ "message" : "SQL Error" }'
                return #End Method
            if return_value != None:
                resp.body = json.dumps(return_value)
            else:
                resp.body = '{ "message" : "No Return" }'

    def on_get(self, req, resp):
        resp.body = json.dumps("Warnings: " + internal_dbConnection.returnWarnings())


#
# Setup API
#

api = falcon.API()

# Define Endpoint Class-Obj
database_endpoint = DataBase()
example_endpoint = Example()

# Add them to API
api.add_route('/testing', example_endpoint)
api.add_route('/database', database_endpoint)
