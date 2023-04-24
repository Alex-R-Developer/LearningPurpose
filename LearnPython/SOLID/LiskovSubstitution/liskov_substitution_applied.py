class Rectangle:
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area method"""
        return self.width * self.height

    @property
    def width(self):
        """Width variable getter method"""
        return self._width

    @width.setter
    def width(self, value):
        """Width variable setter method"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """Height variable getter method"""
        return self._height

    @height.setter
    def height(self, value):
        """Height variable setter method"""
        self._height = value if value > 0 else 1


class Square():
    def __init__(self, side):
        self._side = side
    
    def area(self):
        """Calculate area method"""
        return self.side * self.side

    @property
    def side(self):
        """Side variable getter method"""
        return self._side

    @side.setter
    def side(self, value):
        """Side variable setter method"""
        self._side = value if value > 0 else 1
        

class Employee:
    """Employee class"""
    company_name = "Amazing Burger"
    raise_percentage = 1.03
    
    def __init__(self, name, wage):
        """Set instance variables"""
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """Method that increases employee's wage"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        """Wage variable getter method"""
        return self._wage

    def __str__(self):
        """Method that returns employee information as string"""
        return Employee.company_name + " employee: " + self.name

class Cashier(Employee):
    """Cashier class"""
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        """Method that processes order and returns change"""
        if Cashier.burger_price > money_received:
            print("Not enough money. Please recalculate the money!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + " cashier: " + self.name
