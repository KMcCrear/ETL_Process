import cx_Oracle
import dbconfig as cfg
import subprocess

def insert_etl(data_list):
    """
        insert row of data
        :param data_list: a list of data
        :return:
    """
    sql = ('insert into etl_process(id, prefix, first_name, last_name, ssn, email, company_email, domain_name, phone_number, job, salary, address, street_number, postcode, city, country, iban_no, swift_no, ip_address, mac_address) values(:id, :prefix, :first_name, :last_name, :ssn, :email, :company_email, :domain_name, :phone_number, :job, :salary, :address, :street_number, :postcode, :city, :country, :iban_no, :swift_no, :ip_address, :mac_address)')

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


def sql_loader():
    """
    Inserting data using sql loader
    :return:
    """
    host = 'localhost'
    database = 'XE'
    controlfile = './data_store/test_data.ctl'
    sqlldr_command = f"""sqlldr USERID='{cfg.username}/{cfg.password}@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST={host})(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME ={database}) ))'  control={controlfile}  parallel=true"""
    subprocess.call(sqlldr_command, shell=True)
