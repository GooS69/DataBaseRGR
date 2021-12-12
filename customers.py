
class Customers:

    @staticmethod
    def show_all():
        return 'select * from customers;'

    @staticmethod
    def select():
        customer_name = input('Enter customer name:')
        return f"select * from customers where customer_name = '{customer_name}';"

    @staticmethod
    def insert():
        customer_name = input('Enter customer name(not null):')
        address = input('Enter customer address:')
        email = input('Enter customer email:')
        return f"insert into customers (customer_name, address, email) VALUES " \
               f"('{customer_name}', '{address}', '{email}');"

    @staticmethod
    def delete():
        customer_name = input('Enter customer name:')
        return f"delete from customers where customer_name = '{customer_name}';"