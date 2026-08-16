from abc import ABC, abstractmethod
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)


#--------------------------------------------------------------------------------------------
class InsufficientBatteryError(Exception):
    def __init__(self, name, required, available):
        self.name = name
        self.required = required
        self.available = available
        
        super().__init__(
            f"{name} needs {required}% battery but currently only has {available}%"
        )

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}")
        return result
    return wrapper

#----------------------------------------------------------------------------------
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
        return f"{self.__class__.__name__}(name={self.name!r}, battery={self.battery!r}, manufacturer={self.manufacturer!r})"

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
    
    @classmethod
    def from_config(cls, config_dict):
        return cls(config_dict["name"], config_dict.get("battery", 100))
        
#-----------------------------------------------------------------------------------------
class FootRobot(Robot):
    def __init__(self, name, battery=100, massage_strength=10):
        super().__init__(name, battery)
        self.massage_strength = massage_strength
    
    def perform_task(self, massage_strength): 
        self.use_battery(10)
        return f"Touching Toes... at {self.massage_strength}/10 massage strength"
        
#------------------------------------------------------------------------------------------
class KitchenRobot(Robot):
    def __init__(self, name, battery=100, cooking_speed=10):
        super().__init__(name, battery)
        self.cooking_speed = cooking_speed

    @log_action
    def perform_task(self, cooking_speed):
        self.use_battery(15)
        return f"Cooking Fod.... at {self.cooking_speed}/10 cooking speed"

#---------------------------------------------------------------------------------------------
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

#---------------------Mutable Class Attribute----------------------------------------------------
#bad class
# class RobotBug:
#     colors = []
#
#     def add_color(self, color):
#         self.colors.append(color)
#
# robot1 = RobotBug()
# robot2 = RobotBug()
#
# robot1.add_task("Massage toes")
#
# print(robot1.tasks)
# print(robot2.tasks)

#good class----------------------------------------------------

# class RobotFix:
#     def __init__(self):
#         self.colors = []
#
#     def add_color(self, color):
#         self.colors.append(color)
#
# robot1 = RobotFix()
# robot2 = RobotFix()
#
# robot1.add_task("Massage toes")
#
# print(robot1.tasks)
# print(robot2.tasks)

