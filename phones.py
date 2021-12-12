
class Phones:

    @staticmethod
    def show_all():
        return 'select * from phones;'

    @staticmethod
    def select():
        phone_number = input('Enter phone number:')
        return f"select * from phones where number = '{phone_number}';"

    @staticmethod
    def delete():
        phone_number = input('Enter phone number:')
        return f"delete from phones where number = '{phone_number}'"
