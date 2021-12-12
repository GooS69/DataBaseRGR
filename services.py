
class Services:

    @staticmethod
    def show_all():
        return 'select * from services;'

    @staticmethod
    def select():
        title = input('Enter service title:')
        return f"select * from services where service_title = '{title}';"

    @staticmethod
    def insert():
        title = input('Enter service title(not null):')
        price = input('Enter service price:')
        #validation on price
        type = input('Enter service type:')
        return f"insert into services (service_title, price, type) VALUES " \
               f"('{title}', '{price}', '{type}');"

    @staticmethod
    def update():
        title = input('Enter service title(not null):')
        price = input('Enter service price:')
        # validation on price
        type = input('Enter service type:')
        return f"update services set price = '{price}', type = '{type}' where service_title = '{title}';"

    @staticmethod
    def delete():
        title = input('Enter service title:')
        return f"delete from services where service_title = '{title}';"
