## ETL Multithreading Approach

### Overall Performance
Script takes approx 18 minutes to generate 2 million records and insert them into the target DB using SQL*Loader

#### Loading Performance

Direct Method :-
To load two CSV files with 1 million rows each into the target DB it takes an average of 20 seconds

Conventional Method :- 142.1 Seconds