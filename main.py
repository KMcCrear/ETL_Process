import data_generate
from time import perf_counter
import multiprocessing as mp

if __name__ == '__main__':
    start = perf_counter()
    threading = mp.set_start_method('spawn')

    """Data generation methods: """
    # gen_1 = mp.Process(target=data_generate.generate_csv_data, args=('test_data.csv', 1000000))
    # gen2 = mp.Process(target=data_generate.generate_csv_data, args=('employee_data.csv', 1000000))
    # gen_1.start()
    # gen2.start()
    # gen_1.join()
    # gen2.join()

    """Data input"""
    first_thread = mp.Process(target=data_generate.read_file, args=('test_data', 10000))
    second_thread = mp.Process(target=data_generate.read_file, args=("employee_data", 10000))
    first_thread.start()
    second_thread.start()
    first_thread.join()
    second_thread.join()

    end = perf_counter()
    execution_time = (end - start)
    print("Took", execution_time, "Seconds")
