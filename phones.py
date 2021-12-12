
class Phones:

    @staticmethod
    def show_all():
        return 'select * from phones;'

    @staticmethod
    def select():
        phone_number = input('Enter phone number:')
        return f"select * from phones where number = '{phone_number}';"

    @staticmethod
    def insert():
        number = input('Enter phone number(not null):')
        operator_title = input('Enter operator title:')
        customer_name = input('Enter customer name:')
        region = input('Enter region:')
        type = input('Enter phone type:')
        return f"insert into phones (number, operator_title, customer_name, region, type) VALUES " \
               f"('{number}', '{operator_title}', '{customer_name}', '{region}', '{type}');"

    @staticmethod
    def update():
        number = input('Enter phone number(not null):')
        operator_title = input('Enter operator title:')
        customer_name = input('Enter customer name:')
        region = input('Enter region:')
        type = input('Enter phone type:')
        return f"update phones set operator_title = '{operator_title}', customer_name = '{customer_name}'," \
               f"region = '{region}', type = '{type}' where number = '{number}';"

    @staticmethod
    def delete():
        phone_number = input('Enter phone number:')
        return f"delete from phones where number = '{phone_number}'"
