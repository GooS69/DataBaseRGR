
class Subscriptions:

    @staticmethod
    def show_all():
        return 'select * from subscriptions;', []

    @staticmethod
    def select():
        number = input('Enter phone number:')
        service_title = input('Enter service title:')
        return "select * from subscriptions where number = %s and service_title = %s;", [number, service_title]

    @staticmethod
    def insert():
        number = input('Enter phone number(not null):')
        service_title = input('Enter service title:')
        duration = input('Enter duration(in days):')
        description = input('Enter description:')
        return "insert into subscriptions (number, service_title, duration, description) VALUES (%s, %s, %s, %s)",\
               [number, service_title, duration, description]

    @staticmethod
    def update():
        number = input('Enter phone number(not null):')
        service_title = input('Enter service title:')
        duration = input('Enter duration(in days):')
        description = input('Enter description:')
        return "update subscriptions set duration = %s, description = %s where number = %s and service_title = %s",\
               [duration, description, number, service_title]

    @staticmethod
    def delete():
        number = input('Enter phone number:')
        service_title = input('Enter service title:')
        return "delete from subscriptions where number = %s and service_title = %s;", [number, service_title]
