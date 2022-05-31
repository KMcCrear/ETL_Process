import cx_Oracle
import dbconfig as cfg
import subprocess
import sys


class db_DAO:
    def __init__(self, error_count):
        self.error_count = error_count

    def insert_etl(self, data_list):
        """
            insert row of data
            :param data_list: a list of data
            :return:
        """

        sql = (
            'insert into etl_process(id, prefix, first_name, last_name, ssn, email, company_email, domain_name, phone_number, job, salary, address, street_number, postcode, city, country, iban_no, swift_no, ip_address, mac_address) values(:id, :prefix, :first_name, :last_name, :ssn, :email, :company_email, :domain_name, :phone_number, :job, :salary, :address, :street_number, :postcode, :city, :country, :iban_no, :swift_no, :ip_address, :mac_address)')

        # error tolerance = 50 errors
        try:
            # establish a new connection
            with cx_Oracle.connect(cfg.username,
                                   cfg.password,
                                   cfg.dsn,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.executemany(sql, data_list)
                    # commit work
                    connection.commit()
                    print("Committed", cursor.rowcount)
        except cx_Oracle.Error as error:
            self.error_count += 1
            print(self.error_count, 'Error occurred:')
            print(error)
            if self.error_count == 50:
                sys.exit("Error threshold reached")

    def alter_table(self):
        sql = ('alter table etl_process add constraint  "fk_id" primary key (id)')

        try:
            # establish a new connection
            with cx_Oracle.connect(cfg.username,
                                   cfg.password,
                                   cfg.dsn,
                                   encoding=cfg.encoding) as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sql)
        except cx_Oracle.Error as error:
            print('Error occurred:')
            print(error)
        finally:
            print("Table altered successfully")

    def sql_loader(ctlfile):
        """
        Inserting data using sql loader
        :return:
        """
        host = 'localhost'
        database = 'XE'
        controlfile = f"./data_store/{ctlfile}.ctl"
        sqlldr_command = f"sqlldr USERID='{cfg.username}/{cfg.password}@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST={host})(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME ={database}) ))'  control={controlfile}  parallel=true"
        subprocess.call(sqlldr_command, shell=True)
