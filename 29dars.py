class Avto:
    def __init__(self,model, rang, korobka, narh):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narh=narh
        self.km=0
    def get_info(self):
        return f"Avtomobilning modeli {self.model}, rangi {self.rang}, korobka {self.korobka}, narhi {self.narh}, yurgan kilometri {self.km}"
    def set_km(self,add_km):
        self.km=add_km
    def update_km(self):
        self.km+=10
avto1=Avto("Spark","oq","mexanika",7000)
avto1.update_km()
print(avto1.get_info())

class Avtosalon:
    def __init__(self,nomi):
        self.name=nomi
        self.adress="Farg'ona shahri"
        self.sell=[]

    def get_name(self):
        return self.name


    def add_car(self, car):
        self.sell.append(car)

    def get_info(self):
        return f"Avtosallonning nomi: {self.name}, {self.adress}da joylashgan, ayni damda {self.sell} avtomobillari sotuvda mavjud"

cars=Avtosalon("Chevrolet")
car1=Avto("Spark","oq","mexanika",7000)
cars.add_car(car1)
print(cars.sell)

class Avtosalon:
    def __init__(self,nomi):
        self.name=nomi
        self.adress="Farg'ona shahri"
        self.sell=[]

    def add_car(self, car):
        self.sell.append(car)

    def get_cars(self):
        return [car.get_info() for car in self.sell]
avto_car=cars.get_cars()
