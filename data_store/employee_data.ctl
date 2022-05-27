load data 
infile 'C:\Python\PycharmProjects\ETL_Process\data_store\employee_data.csv' "str '\r\n'"
append
into table ETL_PROCESS
fields terminated by ','
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( ID,
             PREFIX CHAR(4),
             FIRST_NAME CHAR(50),
             LAST_NAME CHAR(50),
             SSN CHAR(20),
             EMAIL CHAR(100),
             COMPANY_EMAIL CHAR(100),
             DOMAIN_NAME CHAR(100),
             PHONE_NUMBER CHAR(50),
             JOB CHAR(100),
             SALARY,
             ADDRESS CHAR(100),
             STREET_NUMBER,
             POSTCODE CHAR(10),
             CITY CHAR(100),
             COUNTRY CHAR(100),
             IBAN_NO CHAR(100),
             SWIFT_NO CHAR(100),
             IP_ADDRESS CHAR(100),
             MAC_ADDRESS CHAR(100)
           )
