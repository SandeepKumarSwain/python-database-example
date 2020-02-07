import db_connect
import logger
import argparse
import csv
import pandas as pd


def insert_data(config_path, db_name, record_path, querry_file):
    ''' Fetch data from given file and insert to database 
        Parameters:
            config_path - path of the conifg file with file name
            db_name - name of the database
            record_path - name of the record file
            querry_file - name of the querry file
    '''
    try:
        # Starting the connection with DB
        connection = db_connect.db_connect(config_path, db_name)
        cursor = connection.cursor()
        # Read and comapre the file extension name by a given file name
        file_ext = record_path.split(".")[-1]
        if file_ext == 'csv':
            df = pd.read_csv(record_path, delimiter=',')
        if file_ext == 'xlsx':
            df = pd.read_excel(record_path, delimiter=',')
        # Reading the querry file
        with open(querry_file) as querry:
            querry = querry.read()
            logger.info('Querry : '+ querry)
        # Inserting Each row
        for index, row in df.iterrows():
            print(row[0], row[1])
            data = (row[0], row[1])
            cursor.execute(querry, data)
        logger.info('Inserted successfully.')
        # Comiting and closing the connection
        connection.commit()
        connection.close()
    except Exception as e:
        logger.error(e)
        connection.close()



# testing insert_data() | trigger for inserting the data
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--config_path', help='Config path')
    parser.add_argument('-d','--db_name', help='DB name')
    parser.add_argument('-r','--record_path', help='Record file')
    parser.add_argument('-q','--querry_file', help='Querry file')
    args = vars(parser.parse_args())
    insert_data(args['config_path'], args['db_name'], args['record_path'], args['querry_file'])




# command to execute the file
# python insert_data.py -c config.ini -d mysql -r record.csv -q insert_query.txt