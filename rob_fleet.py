from abc import ABC, abstractmethod
import logging

class InsufficientBatteryError(Exception):
    def __init__(self, name, required, available):
        self.namae = name
        self.required = required
        self.available = available
        
        super().__init__(
            f"{name} needs {required}% battery but currently only has {available}%"
        )
class Robot(ABC):
    manufacturer = "ChocoStarfish"
    population = 0

    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery
        Robot.population += 1

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, (battery={self.battery!r}, manufacturer={self.manufacturer!r})"

    def _clamp(self, value): 
        return max(0, min(100, value))

    @property 
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        self._battery = self._clamp(value)


    def use_battery(self, amount):
        if self.battery < amount:
            raise InsufficientBatteryError(
                self.name,
                amount,
                self.battery
            )
        self.battery -= amount

    @abstractmethod
    def perform_task(self):
        pass
        
class FootRobot(Robot):
    def __init__(self, name, battery=100):
        super().__init__(name, battery)
    
    def perform_task(self, massage_strength=10): 
        self.massage_strength = massage_strength
        self.use_battery(10)
        return f"Touching Toes... at {self.massage_strength}/10 massage strength"
        

class KitchenRobot(Robot):
    def __init__(self, name, battery=100):
        super().__init__(name, battery)

    def perform_task(self, cooking_speed=10):
        self.cooking_speed = cooking_speed
        self.use_battery(15)
        return f"Cooking Fod.... at {self.cooking_speed}/10 cooking speed"

def fleet_report(robots):
    for robot in robots:
        print(str(robot))

def run_task_safely(robot, **kwargs):
    try:
        result = robot.perform_task(**kwargs)

    except InsufficientBatteryError as error:
        logging.error(error)

    else:
        print(result)

    finally:
        print(f"{robot.name} has {robot.battery}% battery remaining.")
