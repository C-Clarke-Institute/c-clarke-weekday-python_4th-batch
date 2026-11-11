class Engine:

    def __init__(self,engine_no:str, horsepower: int, capacity: str):
        self.horsepower = horsepower
        self.capacity = capacity
        self.engine_no = engine_no

    def start(self):
        print(f"Engine with horsepower - {self.horsepower} is starting")

class Car:

    def __init__(self, model: str, engine: Engine):
        self.engine  = engine #has a relationship
        self.model = model

    def print_car_details(self):
        print(f"car model - {self.model} | capacity - {self.engine.capacity}")

engine = Engine(engine_no="MC-6523323", horsepower=112, capacity="1500CC")
car = Car(model="Axio", engine=engine)
print(car.engine.capacity)

