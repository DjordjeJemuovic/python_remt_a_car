class Car:
    CARS = {
        "Audi": [
            {"model": "A3", "year": 2004}
        ],
        "BMW": [
            {"model": "3 Series", "year": 1998},
            {"model": "X5", "year": 2007},
            {"model": "M3", "year": 2014}
        ],
        "Mercedes-Benz": [
            {"model": "C-Class", "year": 2001},
            {"model": "E-Class", "year": 2009},
            {"model": "GLC", "year": 2016}
        ],
        "Volkswagen": [
            {"model": "Golf", "year": 1999},
            {"model": "Passat", "year": 2005},
            {"model": "Tiguan", "year": 2012}
        ]

    }

    def __init__(self):
        self.__brend = None
        self.__model = None
        self.__year = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brend is None:
            raise ValueError("brend mast be set")
        valid_models = []
        for car in Car.CARS[self.__brend]:
            valid_models.append(car["model"])

        if model not in valid_models:
            raise ValueError("Invalid model")

        self.__model = model

        for car_model in Car.CARS[self.__brend]:
            if car_model['model'] == model:
                self.__year = car_model["year"]

    @property
    def brend(self):
        return self.__brend

    @brend.setter
    def brend(self, brend):
        if brend not in Car.CARS:
            raise ValueError("Invalid Brend")
        self.__brend = brend

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if self.__model is None:
            raise ValueError("Year not set")

        if self.__model is not None and self.__year is not None:
            raise ValueError("Production year cennot be set")

        self.__year = year


audi = Car()

audi.brend = "Audi"
audi.model = "A3"
print(audi.year)
