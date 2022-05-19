import db_DAO
import data_generate
from time import perf_counter
from threading import Thread
import multiprocessing as mp


if __name__ == '__main__':

    start = perf_counter()
    # data_generate.generate_csv_data('test_data.csv', 1000000)
    # data_generate.generate_csv_data('employee_data.csv', 1000000)
    mp.Process(target=db_DAO.sql_loader()).start()
    mp.Process(target=db_DAO.load_employee()).start()
    end = perf_counter()
    execution_time = (end - start)
    print("Took", execution_time, "Seconds")
