from Db import Db

class User(Db):

    #geter -> metoda koja vraca podatak
    def get_name(self):
        return self.__name

    #seter -> metoda koja setuje/dodeljuje vrednos atrubutu klase
    def set_name(self,name):
        if len(name)<3:
            raise ValueError("Name is too short")

        self.__name = name

    def get_age(self,age):
        return age
    def set_age(self,age):
        if age<18:
            raise ValueError("Age is under 18")
        self.__age = age


