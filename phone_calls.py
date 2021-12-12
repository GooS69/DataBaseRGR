
class PhoneCalls:

    @staticmethod
    def show_all():
        return 'select * from phone_calls;'

    @staticmethod
    def select():
        number_from = input('Enter phone number(from):')
        number_to = input('Enter phone number(to):')
        return f"select * from phone_calls where number_from = '{number_from}' and number_to = '{number_to}';"

    @staticmethod
    def delete():
        number_from = input('Enter phone number(from):')
        number_to = input('Enter phone number(to):')
        return f"delete from phone_calls where number_from = '{number_from}' and number_to = '{number_to}';"
