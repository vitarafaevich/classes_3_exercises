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
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                name, code, info, price = line.strip().split('; ')
                result = Product(name, code.strip(), info, price)
                #calling the class and its attribute all_stuff. key - name of the product, value - other info. price has ind 4
                cls.all_stuff[result.name] = [result.code, result.country, result.info, result.price]
            #for item in Basket.all_stuff:
                #print(item)


    def add_product(self, product):
        self.base = product


    def remove_product(self, product):
        self.base = ('rem' + product)


    def show(self):
        for elem in self.__base:
            print(elem, *Basket.all_stuff[elem])


    def price(self):
        amount, place = 0, 0
        for item in self.base:
            if item in self.all_stuff:
                place = len(self.all_stuff[item]) - 1
                amount += int(self.all_stuff[item][place])
        print(amount)


    @classmethod
    def assortment(cls):
        for key in cls.all_stuff:
            #print(key)
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




class ShopManaging:
    @staticmethod
    def user():
        basket = Basket()
        greeting = f'Hi, welcome to our shop!\n'
        interaction = (f'\n'
                       f'Available actions:\n'
                       f'To enter the path to the file with data, enter "file"\n'
                       f'To check this menu again, enter "menu"\n'
                       f'To check available products enter 1\n'
                       f'To add the products into the cart enter 2\n'
                       f'To remove the products from the cart enter 3\n'
                       f'To see what\'s currently in the cart enter 4\n'
                       f'To check the price of the items in the cart enter 5\n'
                       f'To exit enter 0\n')
        print(greeting, interaction)
        request = input('Enter your request: ')

        while request != '0':
            if request == 'file':
                path = input('Enter the path to your file: ')
                basket.product_info(path)
                request = input('Enter your request: ')

            elif request.lower() == 'menu':
                print(interaction)
                request = input('Enter your request: ')
                continue

            elif request == '1':
                basket.assortment()
                request = input('Enter your request: ')

            elif request == '2':
                item = input('Enter the name of the product you want to add to the cart: ')
                if item in Basket.all_stuff:
                    basket.add_product(item)
                    print('The product was successfully added!\n')
                else:
                    print('No such product in the shop\n', interaction)
                request = input('Enter your request: ')

            elif request == '3':
                item = input('Enter the name of the product you want to remove to the cart: ')
                if item in basket.base:
                    basket.remove_product(item)
                    print('The product was successfully removed!\n')
                else:
                    print('No such product in the cart\n', interaction)
                request = input('Enter your request: ')

            elif request == '4':
                basket.show()
                request = input('Enter your request: ')

            elif request == '5':
                basket.price()
                request = input('Enter your request: ')

        print('Have a nice day!')




ShopManaging.user()
