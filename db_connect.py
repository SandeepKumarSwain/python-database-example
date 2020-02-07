from configparser import ConfigParser
import mysql.connector
import sys
import logger


def db_connect(config_path, db_name):
    ''' create and return a connection to a given database.
        Parameters:
        config_path - path of the conifg file with file name
        db_name - name of the database
    '''
    try:
        configur = ConfigParser() 
        print('Reading configuration file : ', config_path)
        configur.read(config_path) 
        #connecting to the database
        connection = mysql.connector.connect(
            host=configur.get(db_name,'host'),
            user=configur.get(db_name,'user'),
            passwd=configur.get(db_name,'passwd'),
            database=configur.get(db_name,'db')
        )
        logger.start()
        logger.info('Connection successful to a database : '+ db_name)
        return connection
    except Exception as e:
        logger.start()
        logger.error(e)
        sys.exit()
    


# testing db_connect()
if __name__ == '__main__':
    mydb = db_connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM info")
    myresult = mycursor.fetchone()
    print(myresult)
