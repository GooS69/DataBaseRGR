

class Operators:

    @staticmethod
    def show_all():
        return 'select * from operators;'

    @staticmethod
    def select():
        title = input('Enter operator title:')
        return f"select * from operators where operator_title = '{title}';"

    @staticmethod
    def insert():
        title = input('Enter operator title(not null):')
        address = input('Enter operator address:')
        phone = input('Enter operator phone:')
        return f"insert into operators (operator_title, address, phone) VALUES " \
               f"('{title}', '{address}', '{phone}');"

    @staticmethod
    def delete():
        title = input('Enter operator title:')
        return f"delete from operators where operator_title = '{title}';"
