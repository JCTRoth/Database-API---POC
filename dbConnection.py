# Imports
import mysql.connector
from config import *


class dbConnection:

    def __init__(self):
        return

    # Objects
    # Running on Obj. Init.

    # Set up Database Connection
    _dbConnection = mysql.connector.connect(

        # Load Config form File to Program
        jsonConfig=config()
        # Extract Info from config file
        jsonConfig.read_config_file()
        print(jsonConfig.config)

        # SET SERVER CONFIG HERE #
        host='localhost',
        # port='3306',
        user='root',
        #  database='123-DB-XYZ',
        password="WilliamSamitienneGrigahcine(French:1986)",
    )

    _myCursor = _dbConnection.cursor()  # Init. Cursor used for exec.

    # Functions

    # Run SQL Code
    def run_sql(self, sqlCode):
        try:
            self._myCursor.execute(sqlCode)
            return list(self._myCursor)
        except:
            return "Error"

    # Undo Last SQL Code Run
    def undo_sql(self):
        self._myCursor.rollback()
        return self._myCursor.fetchwarnings()

    # Return Warnings
    def returnWarnings(self):
        return str(self._myCursor.fetchwarnings())  # Casted as String

    # Disconnect and clear connection pool
    def closeConnection(self):
        self._dbConnection.close()
        if self._dbConnection.can_consume_results == False:
            return "Connection Closed"
        else:
            return "Connection Not Closed - ConnectionID: " + str(self._dbConnection.connection_id)

    # Reestablish Connection
    def reestablishConnection(self):
        # Reconnect == True, one try, 0 delay
        self._dbConnection.ping(True, 1, 0)
        if self._dbConnection.can_consume_results == True:
            dbConnection._myCursor = self.dbConnection.cursor()  # Set Cursor
            return "Connection Reestablished"
        else:
            return "Connection Failed " + str(self._dbConnection.connection_id)
