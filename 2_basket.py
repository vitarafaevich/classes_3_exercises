import ean_13

class Basket:
    """
    Class representing a marketplace basket
    """
    all_stuff = {}
    def __init__(self):
        self.__base = []

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, new):
        if new[0:3] == 'rem':
            if new[3:] in Basket.all_stuff:
                self.__base.remove(new[3:])
        else:
            if new in Basket.all_stuff:
                self.__base.append(new)

    @classmethod
    def product_info(cls, file):
        with open ('product_data.txt', 'r', encoding='utf8') as f:
            for line in f:
                name, code, info, price = line.strip().split('; ')
                result = Product(name, code.strip(), info, price)
                #calling the class and its atribute all_stuff. key - name of the product, value - other info. price has ind 4
                cls.all_stuff[result.repr()[0]] = result.repr()[1:]


    def add_product(self, product):
        self.base = product


    def remove_product(self, product):
        self.base = ('del' + product)


    def show(self):
        for elem in self.__base:
            print(elem, *Basket.all_stuff[elem])

    @classmethod
    def price(cls):
        amount = 0
        for elem in range(len(cls.all_stuff)):
            amount += cls.all_stuff[elem][3]
        print(amount)


    @classmethod
    def assortment(cls):
        for key in cls.all_stuff:
            print(key, *cls.all_stuff[key])


class Product:
    """
    Class representing a product in the basket (its name and country based on ean-13 code)
    """

    def __init__(self, name, code, info, price):
        self.__name = name
        self.__code = code
        self.__info = info
        self.__price = price
        #ean_13 - file name; dict_ean - dictionary with ean codes ('code': 'country')
        if code[0:3] in ean_13.dict_ean:
            self.country = ean_13.dict_ean[code[0:3]]
        else:
            self.country = ''


    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def info(self):
        return self.__info

    @property
    def price(self):
        return self.__price

    def __repr__(self):
        return [self.__name, self.__code, self.country, self.__info, self.__price]


class Shop_managing:
    @staticmethod
    def user():
        basket = Basket()
        interaction = (f'\n'
                       f'Welcome to our shop!\n'
                       f'To check available products enter 1\n'
                       f'To add the products into the cart enter 2\n'
                       f'To remove the products from the cart enter 3\n'
                       f'To see whats currently in the cart enter 4\n'
                       f'To check the price of the items in the cart enter 5\n'
                       f'To exit enter 0\n')

        print(interaction)
        request = input()

        while request != 0:
            if request == 1:
                basket.assortment()
                request = input()

            elif request == 2:
                print('Enter the name of the product u want to add to the cart')
                item = input()
                while item not in basket.all_stuff[item]:
                    print('No such product in the cart')
                    item = input()

                basket.add_product(item)
                request = input()

            elif request == 3:
                print('Enter the name of the product u want to remove from the cart')
                item = input()
                while item not in basket.all_stuff[item]:
                    print('No such product in the cart')
                    item = input()

                basket.remove_product(item)
                request = input()

            elif request == 4:
                basket.show()
                request = input()

            elif request == 5:
                basket.price()
                request = input()


Shop_managing.user()