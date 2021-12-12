
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
    def insert():
        number_from = input('Enter phone number(from, not null):')
        number_to = input('Enter phone number(to, not null):')
        call_date = input('Enter call date(YYYY-MM-DD HH:MM:SS):')
        duration = input('Enter duration(on sec):')
        return f"insert into phone_calls (number_from, number_to, call_date, duration) VALUES " \
               f"('{number_from}', '{number_to}', '{call_date}', '{duration}')"

    @staticmethod
    def update():
        number_from = input('Enter phone number(from, not null):')
        number_to = input('Enter phone number(to, not null):')
        call_date = input('Enter call date(YYYY-MM-DD HH:MM:SS):')
        duration = input('Enter duration(on sec):')
        return f"update phone_calls set call_date = '{call_date}', duration = '{duration}' " \
               f"where number_from = '{number_from}' and number_to = '{number_to}'"

    @staticmethod
    def delete():
        number_from = input('Enter phone number(from):')
        number_to = input('Enter phone number(to):')
        return f"delete from phone_calls where number_from = '{number_from}' and number_to = '{number_to}';"
