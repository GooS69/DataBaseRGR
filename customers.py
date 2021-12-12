
class Customers:

    @staticmethod
    def show_all():
        return 'select * from customers;'

    @staticmethod
    def select():
        customer_name = input('Enter customer name:')
        return f"select * from customers where customer_name = '{customer_name}';"

    @staticmethod
    def delete():
        customer_name = input('Enter customer name:')
        return f"delete from customers where customer_name = '{customer_name}';"