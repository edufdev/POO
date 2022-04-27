from car import Car
from account import Account

if __name__ == '__main__':
    print("Hola Mundo")
    car = Car("JDLC24", Account("Juan de la Cruz", "JCZ420"))
    print(vars(car))
    print(vars(car.driver))





    # print("Hola Mundo")
    # car = Car()
    # car.license = "AML255"
    # car.driver = "Melisa Juarez"
    # print(vars(car))

    # car2 = Car()
    # car2.license = "QLP420"
    # car2.driver = "Angel Calel"
    # print(vars(car2))