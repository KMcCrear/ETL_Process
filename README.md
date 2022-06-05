## ETL Multithreading Approach

To bypass pythons GIL, the multiprocessing module is being used for multithreading.

### Performance

Inserting 2 million rows from two CSV that contain 20 columns takes an average of 310 seconds using two threads.

Inserting 4 million rows form two CSV files takes an average of 490 seconds 

#### Dependencies

- Time
- Multiprocessing
- perfcounter
- cx_Oracle
- subprocess
- Faker
- CSV
- Numpy
- Uuid
- pandas