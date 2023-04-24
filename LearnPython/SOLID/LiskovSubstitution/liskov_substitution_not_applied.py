class Rectangle:
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area"""
        return self.width * self.height

    @property
    def width(self):
        """Getter method for width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """Getter method for height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self._height = value if value > 0 else 1


class Square(Rectangle):
    """Square class"""

    def __init__(self, side):
        super().__init__(side, side)

    @property
    def width(self):
        """Getter method for width"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1

    @property
    def height(self):
        """Getter method for height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self._width = value if value > 0 else 1
        self._height = value if value > 0 else 1


class Employee:
    """Employee class"""
    company_name = "Amazing Burger"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """Increase employee's wage"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """Return employee information as a string"""
        return Employee.company_name + " employee: " + self.name


class Cashier(Employee):
    """Cashier class that violates the Liskov substitution principle"""
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount):
        """Increase employee's wage"""
        self.wage += self.raise_amount

    @property
    def wage(self):
        return "Cannot provide wage information"
