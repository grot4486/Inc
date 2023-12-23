class Orc:
    def __init__(self, n, a, h):
        print('Доступен объект класса Orc')
        self.name=n
        self.age=a
        self.height=h
    
    def print(self):
        print(f'Введите имя:{self.name}')
        print(f'Введите возраст:{self.age}')
        print(f'Введите рост:{self.height}')
     
    @property
    def name(self):
        return self.__name.upper()
        
    @name.setter    
    def name(self, n):
        self.__name=n.capitalize()
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 300:
            self.__age = age
        else:
            print("Данный обьект уже мертв")


class Destroyer(Orc):
    def study(self):
        print(f'{self.name} Всё крушит')
            

person1=Orc('Seryy Klyk', 100, 189)
person1.print()
person1.study()
