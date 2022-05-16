from time import perf_counter
from faker import Faker
import csv
import insert_into_db

fake = Faker('en_GB')

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
    print("Generation took ", execution_time, " seconds")


def read_data():
    file = open("test_data.csv")
    csvreader = csv.reader(file)
    file_header = next(csvreader)
    #print(file_header)

    rows = []

    for row in csvreader:
        insert_into_db.insert_etl(row)
    #print(rows)
    file.close()
