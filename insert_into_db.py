import cx_Oracle
import dbconfig as cfg


def insert_etl(data_list):
    """
        insert row of data
        :param data_list: a list of data
        :return:
        """
    sql = ('insert into etl_process(id, prefix, first_name, last_name, ssn, email, company_email, domain_name, phone_number, address, street_number, postcode, city, county, country, country_code, iban_no, swift_no, ip_address, mac_address) values(:id, :prefix, :first_name, :last_name, :ssn, :email, :company_email, :domain_name, :phone_number, :address, :street_number, :postcode, :city, :county, :country, :country_code, :iban_no, :swift_no, :ip_address, :mac_address)')

    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                               cfg.password,
                               cfg.dsn,
                               encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.execute(sql, data_list)
                # commit work
                connection.commit()
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)
