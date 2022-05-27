import db_DAO
import data_generate
from time import perf_counter
from threading import Thread
import multiprocessing as mp


if __name__ == '__main__':
    start = perf_counter()
    # data generation methods:
    threading = mp.set_start_method('spawn')
    # data_generate.generate_csv_data('test_data.csv', 100000)
    # data_generate.generate_csv_data('employee_data.csv', 100000)
    # gen_1 = mp.Process(target=data_generate.generate_csv_data, args=('test_data.csv', 100000))
    # gen2 = mp.Process(target=data_generate.generate_csv_data, args=('employee_data.csv', 100000))
    # gen_1.start()
    # gen2.start()
    # gen_1.join()
    # gen2.join()

    first_thread = mp.Process(target=data_generate.read_file, args=('test_data',))
    second_thread = mp.Process(target=data_generate.read_file, args=("employee_data",))
    first_thread.start()
    second_thread.start()
    first_thread.join()
    second_thread.join()


    end = perf_counter()
    execution_time = (end - start)
    print("Took", execution_time, "Seconds")
