from time import perf_counter
from faker import Faker
import csv
import db_DAO
import numpy as np
import uuid
import pandas as pd


def generate_csv_data(filename, rows):
    """
        Generate data
        :param filename
        :param rows
        :return:
    """

    Faker.seed(np.random.randint(1, 1000))
    fake = Faker('en_GB')
    header = [
        'id',
        'prefix',
        'first_name',
        'last_name',
        'ssn',
        'email',
        'company_email',
        'domain_name',
        'phone_number',
        'job_title',
        'salary',
        'address',
        'street_number',
        'postcode',
        'city',
        'country',
        'iban_no',
        'swift_no',
        'ip_address',
        'mac_address'
    ]

    data = []

    start = perf_counter()
    f = open(f"./data_store/{filename}", 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(header)
    for _ in range(rows):
        salary = np.random.randint(10000, 200000)
        data.append([uuid.uuid4(),
                     str(fake.prefix()),
                     str(fake.first_name()),
                     str(fake.last_name()),
                     str(fake.ssn()),
                     str(fake.ascii_safe_email()),
                     str(fake.ascii_company_email()),
                     str(fake.domain_name()),
                     str(fake.cellphone_number()),
                     fake.job(),
                     salary,
                     str(fake.street_name()),
                     str(fake.building_number()),
                     str(fake.postcode()),
                     str(fake.city()),
                     str(fake.current_country()),
                     str(fake.iban()),
                     str(fake.swift()),
                     str(fake.ipv4_public()),
                     str(fake.mac_address())])
    writer.writerows(data)
    f.close()
    end = perf_counter()
    execution_time = (end - start)
    print(f"Generation of {filename} took ", execution_time, " seconds")


def read_file(filename):
    for chunk_df in pd.read_csv(f"./data_store/{filename}.csv", chunksize=1000):
        values = chunk_df.values
        db_DAO.insert_etl(values.tolist())