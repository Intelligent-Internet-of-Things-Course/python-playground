from car import Car
from audi import AudiCar
from electric_car import ElectricCar

car1 = Car("Audi", "A4")
car2 = Car("Audi", "A4")

print(f'Car 1 -> Manufacturer: {car1.manufacturer} Model: {car1.model} Default-Engine: {car1.engine}')
print(f'Car 2 -> Manufacturer: {car1.manufacturer} Model: {car1.model} Default-Engine: {car2.engine}')

print(f'Are car instances equal ? {car1 == car2}')

print(f'First Car instance: {car1}')
print(f'Second Car instance: {car2}')

# Change Car 1 engine type
car1.engine = "diesel_engine"
print(f'Car 1 -> Manufacturer: {car1.manufacturer} Model: {car1.model} Default-Engine: {car1.engine}')

# Use the description instance methods
print(f'Car 1 Description -> {car1.description()}\n')

# Use the default __str__() method
print(f'Car 1 __str__() result -> {car1}\n')

print(f'Car 1 ({car1.engine}) Estimated Air Pollution -> {car1.estimate_air_pollution(150)}')
print(f'Car 2 ({car2.engine}) Estimated Air Pollution -> {car2.estimate_air_pollution(150)}')

audi1 = AudiCar("Audi", "Q3")
print(f'\nAudiCar 1 Description -> {audi1}')

# Print objects type
print(f'\nVariable car1 is a -> {type(car1)}')
print(f'\nVariable audi1 is a -> {type(audi1)}\n')

if isinstance(car1, Car):
    print("Variable car1 is a Car")
else:
    print("Variable car1 is not a Car !")

electric_car1 = ElectricCar("Tesla", "Model-Y", 60)
print(f'\nElectric Car 1 Description -> {electric_car1}')
print(f'\nElectric Car 1 Battery Level -> {electric_car1.battery_level}')
electric_car1.measure_battery_level()
print(f'\nElectric Car 1 Battery Level -> {electric_car1.battery_level}')
