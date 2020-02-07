import db_connect
import sys
import argparse
import save_data
import logger

def fetch_data(config_path, db_name, querry_file, outfile_type):
    ''' Fetch data of a table from a given database.
        Parameters:
            config_path - path of the conifg file with file name
            db_name - name of the database
            querry_file - name of the querry file
    '''
    # Connecting to the database
    connection = db_connect.db_connect(config_path, db_name)
    # Reading the querry from querry file
    try:
        logger.info('Reading querry file from path : '+ querry_file)
        with open(querry_file) as querry:
            querry = querry.read()
            logger.info('Querry : '+ querry)
        # Intatiating a cursor object and executing the query 
        cursor = connection.cursor()
        cursor.execute(querry)
        # save the data in a given file type
        save_data.save_data(cursor, outfile_type)
        connection.close()
    except Exception as e:
        logger.error(e)
        connection.close()


# testing fetch_data() | trigger for fetching and saving the data
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--config_path', help='Config path')
    parser.add_argument('-d','--db_name', help='DB name')
    parser.add_argument('-q','--querry_file', help='Querry file')
    parser.add_argument('-o','--outfile_type', help='Outfile type')
    args = vars(parser.parse_args())
    fetch_data(args['config_path'], args['db_name'], args['querry_file'], args['outfile_type'])




# command to execute the file
# python fetch_data.py -c config.ini -d mysql -q select_querry.txt -o xlsx