class Ship:
    """Ship class"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        self.fuel_tank = FuelTank(fuel)
        self.crew_manager = CrewManager(num_crew)
        self.supply_hold = SupplyHold(supplies, self.crew_manager)
        self.engine = Engine(self.fuel_tank, fuel_per_hour)


class FuelTank:
    """Fuel tank class"""
    def __init__(self, fuel):
        """Instance variable for the amount of fuel stored in the fuel tank"""
        self.fuel = fuel

    def load_fuel(self, amount):
        """Fuel refill method"""
        self.fuel += amount

    def use_fuel(self, amount):
        """Fuel usage method"""
        if self.fuel - amount >= 0:
            self.fuel -= amount
            return True
        print("Not enough fuel!")
        return False

    def report_fuel(self):
        """Fuel report method"""
        print("There are {} liters of fuel left".format(self.fuel))


class Engine:
    """Engine class"""
    def __init__(self, fuel_tank, fuel_per_hour):
        """Instance variables for the fuel tank instance and fuel consumption per hour"""
        self.fuel_tank = fuel_tank
        self.fuel_per_hour = fuel_per_hour

    def run_for_hours(self, hours):
        """Engine operation method, uses the fuel tank instance"""
        if self.fuel_tank.use_fuel(self.fuel_per_hour * hours):
            print("Running the engine for {} hours!".format(hours))
            return True
        print("Cannot start the engine due to insufficient fuel")
        return False


class CrewManager:
    """Crew management class"""
    def __init__(self, num_crew):
        """Instance variable for the number of crew members onboard"""
        self.num_crew = num_crew

    def load_crew(self, number):
        """Crew boarding method"""
        self.num_crew += number

    def report_crew(self):
        """Crew report method"""
        print("There are currently {} crew members".format(self.num_crew))


class SupplyHold:
    """Supply hold class"""
    def __init__(self, supplies, crew_manager):
        """Instance variables for the amount of supplies and crew management instance"""
        self.supplies = supplies
        self.crew_manager = crew_manager

    def load_supplies(self, amount):
        """Supply refill method"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """Supply distribution method, distributes the same amount of supplies to each crew member"""
        if self.supplies >= self.crew_manager.num_crew:
            self.supplies -= self.crew_manager.num_crew
            return True
        print("Cannot distribute supplies due to insufficient supplies")
        return False

    def report_supplies(self):
        """Supply report method"""
        print("There are currently enough supplies for {} crew members".format(self.supplies))
