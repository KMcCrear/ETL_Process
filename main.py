import cx_Oracle
import dbconfig
import generateCSV
from time import perf_counter

cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\Oracle\instantclient_21_3")

sql = 'select * from etl_process'

# connection to the database
def connect_to_db():
    connection = None
    try:
        with cx_Oracle.connect(
                dbconfig.username,
                dbconfig.password,
                dbconfig.dsn,
                encoding=dbconfig.encoding) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                while True:
                    row = cursor.fetchone()
                    if row is None:
                        break
                    print(row)
    except cx_Oracle.Error as error:
        print(error)




if __name__ == '__main__':
    start = perf_counter()
    # connect_to_db()
    generateCSV.generate_data()
    generateCSV.read_data()
    end = perf_counter()
    execution_time = (end - start)
    print(execution_time)
