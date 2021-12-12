from contextlib import closing

import psycopg2
from psycopg2 import IntegrityError

from customers import Customers
from operators import Operators
from phone_calls import PhoneCalls
from phones import Phones
from services import Services
from subscriptions import Subscriptions

with closing(psycopg2.connect(dbname='rgr', user='postgres', password='postgres', host='localhost')) as conn:
    with conn.cursor() as cursor:

        while True:
            table = input('Enter table (Operators, Phones, Customers, PhoneCalls, Services, Subscriptions):')
            if table not in ['Operators', 'Phones', 'Customers', 'PhoneCalls', 'Services', 'Subscriptions']:
                print(f'Table {table} not exist')
                continue

            operation = input(f'Enter operation for table {table} (show all, select, insert, update, delete):')
            if operation not in ['show all', 'select', 'insert', 'update', 'delete']:
                print(f'Operation {operation} not exist')
                continue

            if operation == 'show all':
                operation = 'show_all'

            try:
                if operation in ['show_all', 'select']:
                    query = eval(f'{table}.{operation}()')
                    cursor.execute(query)
                    print('Results:')
                    for row in cursor:
                        print(row)

                elif operation in ['insert', 'update', 'delete']:
                    query = eval(f'{table}.{operation}()')
                    cursor.execute(query)
                    conn.commit()
                    print('Done!')
            except Exception as e:
                print(e)
