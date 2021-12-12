

class Operators:

    @staticmethod
    def show_all():
        return 'select * from operators;'

    @staticmethod
    def select():
        title = input('Enter operator title:')
        return f"select * from operators where operator_title = '{title}';"

    @staticmethod
    def delete():
        title = input('Enter operator title:')
        return f"delete from operators where operator_title = '{title}';"
