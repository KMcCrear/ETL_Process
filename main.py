from faker import Faker
import csv
from time import perf_counter
import cx_Oracle
import dbconfig

cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\Oracle\instantclient_21_3")

fake = Faker('en_GB')
sql = 'select * from etl_process'


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
                        print("no row")
                        break
                    print(row)
    except cx_Oracle.Error as error:
        print(error)
    # finally:
    #     if connection:
    #         print("close")
    #         connection.close()


header = [
    '_id',
    'prefix',
    'first_name',
    'last_name',
    'ssn',
    'email',
    'company_email',
    'domain_name',
    'phone_number',
    'address',
    'street_number',
    'postcode',
    'city',
    'county',
    'country',
    'country_code',
    'iban_no',
    'swift_no',
    'ip_address',
    'mac_address'
]
data = []


def generate_data():
    start = perf_counter()
    f = open('./test_data.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(header)
    for _ in range(10):
        data.append([fake.iana_id(),
                     str(fake.prefix()),
                     str(fake.first_name()),
                     str(fake.last_name()),
                     str(fake.ssn()),
                     str(fake.ascii_safe_email()),
                     str(fake.ascii_company_email()),
                     str(fake.domain_name()),
                     str(fake.cellphone_number()),
                     str(fake.street_name()),
                     str(fake.building_number()),
                     str(fake.postcode()),
                     str(fake.city()),
                     str(fake.county()),
                     str(fake.current_country()),
                     str(fake.current_country_code()),
                     str(fake.iban()),
                     str(fake.swift()),
                     str(fake.ipv4_public()),
                     str(fake.mac_address())])
    writer.writerows(data)
    f.close()
    end = perf_counter()
    execution_time = (end - start)
    print(execution_time)


if __name__ == '__main__':
    connect_to_db()
    # generate_data()
