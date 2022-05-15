from faker import Faker
import csv
from time import perf_counter
import cx_Oracle
import dbconfig

cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\Oracle\instantclient_21_3")

fake = Faker('en_GB')


def connect_to_db():
    connection = None
    try:
        connection = cx_Oracle.connect(
            dbconfig.username,
            dbconfig.password,
            dbconfig.dsn,
            encoding=dbconfig.encoding)

        print(connection.version, "Connected")
    except cx_Oracle.Error as error:
        print("error")
        print(error)
    finally:
        if connection:
            print("close")
            connection.close()


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
    for _ in range(1000000):
        data.append([fake.iana_id(),
                     fake.prefix(),
                     fake.first_name(),
                     fake.last_name(),
                     fake.ssn(),
                     fake.ascii_safe_email(),
                     fake.ascii_company_email(),
                     fake.domain_name(),
                     fake.cellphone_number(),
                     fake.street_name(),
                     fake.building_number(),
                     fake.postcode(),
                     fake.city(),
                     fake.county(),
                     fake.current_country(),
                     fake.current_country_code(),
                     fake.iban(),
                     fake.swift(),
                     fake.ipv4_public(),
                     fake.mac_address()])
    writer.writerows(data)
    f.close()
    end = perf_counter()
    execution_time = (end - start)
    print(execution_time)


if __name__ == '__main__':
    connect_to_db()
    # generate_data()
