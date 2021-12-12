
class Subscriptions:

    @staticmethod
    def show_all():
        return 'select * from subscriptions;'

    @staticmethod
    def select():
        number = input('Enter phone number:')
        service_title = input('Enter service title:')
        return f"select * from subscriptions where number = '{number}' and service_title = '{service_title}';"

    @staticmethod
    def delete():
        number = input('Enter phone number:')
        service_title = input('Enter service title:')
        return f"delete from subscriptions where number = '{number}' and service_title = '{service_title}';"
