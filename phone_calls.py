
class PhoneCalls:

    @staticmethod
    def show_all():
        return 'select * from phone_calls;', []

    @staticmethod
    def select():
        number_from = input('Enter phone number(from):')
        number_to = input('Enter phone number(to):')
        return "select * from phone_calls where number_from = %s and number_to = %s;", [number_from, number_to]

    @staticmethod
    def insert():
        number_from = input('Enter phone number(from, not null):')
        number_to = input('Enter phone number(to, not null):')
        call_date = input('Enter call date(YYYY-MM-DD HH:MM:SS):')
        duration = input('Enter duration(on sec):')
        return "insert into phone_calls (number_from, number_to, call_date, duration) VALUES (%s, %s, %s, %s)",\
               [number_from, number_to, call_date, duration]

    @staticmethod
    def update():
        number_from = input('Enter phone number(from, not null):')
        number_to = input('Enter phone number(to, not null):')
        call_date = input('Enter call date(YYYY-MM-DD HH:MM:SS):')
        duration = input('Enter duration(on sec):')
        return "update phone_calls set call_date = %s, duration = %s where number_from = %s and number_to = %s",\
               [call_date, duration, number_from, number_to]

    @staticmethod
    def delete():
        number_from = input('Enter phone number(from):')
        number_to = input('Enter phone number(to):')
        return "delete from phone_calls where number_from = %s and number_to = %s;", [number_from, number_to]
