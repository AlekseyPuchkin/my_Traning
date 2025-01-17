class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        try:
            with open(self.__file_name, 'r'):
                pass
        except FileNotFoundError:
            with open(self.__file_name, 'w'):
                pass

    def get_products(self):
        products = []
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    name, weight, category = line.strip().split(', ')
                    product = Product(name, float(weight), category)
                    products.append(product)
        except FileNotFoundError:
            pass
        return products

    def add(self, *products):
        existing_products = self.get_products()
        existing_names = [p.name for p in existing_products]
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_names:
                    file.write(str(product) + '\n')
                    existing_names.append(product.name)
                else:
                    print(f'Продукт {product.name} уже есть в магазине')

if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)

    s1.add(p1, p2, p3)
    all_products = s1.get_products()
    for product in all_products:
        print(product)