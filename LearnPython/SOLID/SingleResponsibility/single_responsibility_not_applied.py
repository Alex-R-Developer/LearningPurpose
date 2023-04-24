class Ship:
    """Ship class"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        """Has instance variables of fuel amount, fuel consumption per hour, 
        supply amount, and number of crew"""
        self.fuel = fuel
        self.fuel_per_hour = fuel_per_hour
        self.supplies = supplies
        self.num_crew = num_crew

    def report_fuel(self):
        """Fuel report method"""
        print("Current fuel level is {}l".format(self.fuel))

    def load_fuel(self, amount):
        """Fuel charging method"""
        self.fuel += amount

    def report_supplies(self):
        """Supply report method"""
        print("Currently, there are supplies for {} crew members".format(self.supplies))

    def load_supplies(self, amount):
        """Supply replenishment method"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """Supply distribution method"""
        if self.supplies >= self.num_crew:
            self.supplies -= self.num_crew
            return True
        print("Not enough supplies to distribute")
        return False

    def report_crew(self):
        """Crew report method"""
        print("There are currently {} crew members".format(self.num_crew))

    def load_crew(self, number):
        """Crew boarding method"""
        self.num_crew += number

    def run_engine_for_hours(self, hours):
        """Engine operation method"""
        if self.fuel > self.fuel_per_hour * hours:
            self.fuel -= self.fuel_per_hour * hours
            print("Running the engine for {} hours!".format(hours))
        else:
            print("Not enough fuel to start the engine")
