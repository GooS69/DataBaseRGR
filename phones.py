
class Phones:

    @staticmethod
    def show_all():
        return 'select * from phones;', []

    @staticmethod
    def select():
        phone_number = input('Enter phone number:')
        return "select * from phones where number = %s;", [phone_number, ]

    @staticmethod
    def insert():
        number = input('Enter phone number(not null):')
        operator_title = input('Enter operator title:')
        customer_name = input('Enter customer name:')
        region = input('Enter region:')
        type = input('Enter phone type:')
        return "insert into phones (number, operator_title, customer_name, region, type) VALUES (%s, %s, %s, %s, %s);",\
               [number, operator_title, customer_name, region, type]

    @staticmethod
    def update():
        number = input('Enter phone number(not null):')
        operator_title = input('Enter operator title:')
        customer_name = input('Enter customer name:')
        region = input('Enter region:')
        type = input('Enter phone type:')
        return "update phones set operator_title = %s, customer_name = %s, region = %s, type = %s where number = %s;",\
               [operator_title, customer_name, region, type, number]

    @staticmethod
    def delete():
        phone_number = input('Enter phone number:')
        return "delete from phones where number = %s", [phone_number, ]
