import csv
import xlsxwriter 
import pandas as pd
import logger

def save_data(cursor, outfile_type):
    ''' save data with given file type '''
    try:
        columns = [col[0] for col in cursor.description]
        rows = [row for row in cursor]
        logger.info('Total no. of records = '+ str(len(rows)))
        # Writing to csv
        if outfile_type == 'csv':
            with open("fetch_data.csv","w") as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(columns)
                writer.writerows(rows)
                logger.info('Saved records in fetch_data.csv file')
        # Writing to excel file    
        if outfile_type == 'xlsx':
            df = pd.DataFrame(rows, columns=columns)
            df.to_excel('fetch_data.xlsx', index=False)
            logger.info('Saved records in fetch_data.xlsx file')
        # Writing to a text file    
        if outfile_type == 'txt':
            with open("fetch_data.txt","w") as outfile:
                outfile.writelines(str(tuple(columns))+'\n')
                outfile.writelines(str(row)+'\n' for row in rows)
                logger.info('Saved records in fetch_data.txt file')
    except Exception as e:
        logger.error(e)


# testing save_data()
if __name__ == '__main__':
    import fetch_data
    fetch_data.fetch_data(config_path='config.ini', db_name='mysql', querry_file='querry.txt', outfile_type='xlsx')
