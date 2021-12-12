
class Services:

    @staticmethod
    def show_all():
        return 'select * from services;', []

    @staticmethod
    def select():
        title = input('Enter service title:')
        return "select * from services where service_title = %s;", [title, ]

    @staticmethod
    def insert():
        title = input('Enter service title(not null):')
        price = input('Enter service price:')
        type = input('Enter service type:')
        return "insert into services (service_title, price, type) VALUES (%s, %s, %s);", [title, price, type]

    @staticmethod
    def update():
        title = input('Enter service title(not null):')
        price = input('Enter service price:')
        type = input('Enter service type:')
        return "update services set price = %s, type = %s where service_title = '{title}';", [price, type]

    @staticmethod
    def delete():
        title = input('Enter service title:')
        return "delete from services where service_title = %s;", [title, ]
