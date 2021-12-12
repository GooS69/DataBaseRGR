

class Operators:

    @staticmethod
    def show_all():
        return 'select * from operators;', []

    @staticmethod
    def select():
        title = input('Enter operator title:')
        return "select * from operators where operator_title = %s;", [title, ]

    @staticmethod
    def insert():
        title = input('Enter operator title(not null):')
        address = input('Enter operator address:')
        phone = input('Enter operator phone:')
        return "insert into operators (operator_title, address, phone) VALUES (%s, %s, %s);", [title, address, phone]

    @staticmethod
    def update():
        title = input('Enter operator title(not null):')
        address = input('Enter operator address:')
        phone = input('Enter operator phone:')
        return "update operators set address = %s, phone = %s where operator_title = %s;", [address, phone, title]

    @staticmethod
    def delete():
        title = input('Enter operator title:')
        return "delete from operators where operator_title = %s;", [title, ]
