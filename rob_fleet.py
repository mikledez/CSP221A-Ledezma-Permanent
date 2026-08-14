class Robot:
    def __init__(self, name, battery=100, ):
        self.name = name
        self.battery = battery
        self.manufacturer = "ChocoStarfish"
        self.population = 1
        print(f"name ({__str__(battery)}% battery")

    def __repr__(self):
        return f"Person(name={self.name!r}, battery={self.battery})"
        
        
class FootRobot(Robot):
    def super.__init__(self, name, battery=100)
        self.massage_speed = 0
    
    def perform_task():
        print("Cleaning.... toes")

class KitchenRobot(Robot):
    def super.__init__(self, name, battery=100)
        self.cooking_speed = 0

    def perform_task():
        print("Cooking")