from Db import Db


class User(Db):

    def __init__(self, name, age):
        super().__init__()
        self.__name = name
        self.__age = age

    # geter -> metoda koja vraca podatak
    @property
    def name(self):
        return self.__name

    # seter -> metoda koja setuje/dodeljuje vrednos atrubutu klase
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self, age):
        return age

    @age.setter
    def age(self, age):
        self.__age = age
