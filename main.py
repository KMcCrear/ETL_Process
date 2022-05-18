import cx_Oracle

import db_DAO
import dbconfig
import data_generate
from time import perf_counter
import time
from threading import Thread
import logging



if __name__ == '__main__':
    """DB stuff"""
    start = perf_counter()
    data_generate.generate_csv_data('test_data.csv', 1000000)
    data_generate.generate_csv_data('employee_data.csv', 1000000)
    csv_thread = Thread(target=db_DAO.sql_loader())
    employee_thread = Thread(target=db_DAO.load_employee())
    csv_thread.start()
    employee_thread.start()
    end = perf_counter()
    execution_time = (end - start)
    print("Took", execution_time, "Seconds")
