import db_DAO
import data_generate
from time import perf_counter
from threading import Thread
import multiprocessing as mp


if __name__ == '__main__':
    start = perf_counter()
    # data generation methods:
    # data_generate.generate_csv_data('test_data.csv', 1000000)
    # data_generate.generate_csv_data('employee_data.csv', 1000000)
    mp.set_start_method('spawn')
    test_data = mp.Process(target=db_DAO.sql_loader())
    emp = mp.Process(target=db_DAO.load_employee())

    # start the processes
    test_data.start()
    emp.start()
    # join processes to main process
    test_data.join()
    emp.join()
    db_DAO.alter_table()

    end = perf_counter()
    execution_time = (end - start)
    print("Took", execution_time, "Seconds")
