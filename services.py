
class Services:

    @staticmethod
    def show_all():
        return 'select * from services;'

    @staticmethod
    def select():
        title = input('Enter service title:')
        return f"select * from services where service_title = '{title}';"

    @staticmethod
    def delete():
        title = input('Enter service title:')
        return f"delete from services where service_title = '{title}';"
