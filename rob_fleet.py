class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery
        self.manufacturer = "ChocoStarfish"
        self.population = 1

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"


    def _clamp(self, value): 
        return max(0, min(100, value))

    @property 
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        self._battery = self._clamp(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(battery={self.battery!r}, manufacturer={self.manufacturer!r})"

    def use_battery(self, amount):
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0
        
        
class FootRobot(Robot):
    def __init__(self, name, battery=100, massage_strength=10):
        super().__init__(name, battery)
        self.massage_strength = massage_strength
    
    def massage_toes(self, strength):
        self.massage_strength = strength
        self.use_battery(10)
        return f"Touching Toes... at {self.massage_strength}/10 massage strength"
        

class KitchenRobot(Robot):
    def __init__(self, name, battery=100, cooking_speed=10):
        super().__init__(name, battery, cooking_speed)
        self.cooking_speed = 0

    def cook_food(self, cooking_speed):
        self.cooking_speed = cooking_speed
        self.use_battery(15)
        return f"Cooking Fod.... at {self.cooking_speed}/10 cooking speed"
