
class Customers:

    @staticmethod
    def show_all():
        return 'select * from customers;', []

    @staticmethod
    def select():
        customer_name = input('Enter customer name:')
        return "select * from customers where customer_name = %s;", [customer_name, ]

    @staticmethod
    def insert():
        customer_name = input('Enter customer name(not null):')
        address = input('Enter customer address:')
        email = input('Enter customer email:')
        return "insert into customers (customer_name, address, email) VALUES (%s, %s, %s);",\
               [customer_name, address, email]

    @staticmethod
    def update():
        customer_name = input('Enter customer name(not null):')
        address = input('Enter customer address:')
        email = input('Enter customer email:')
        return "update customers set address = %s, email = %s where customer_name = %s;",\
               [address, email, customer_name]

    @staticmethod
    def delete():
        customer_name = input('Enter customer name:')
        return "delete from customers where customer_name = %s;", [customer_name, ]
