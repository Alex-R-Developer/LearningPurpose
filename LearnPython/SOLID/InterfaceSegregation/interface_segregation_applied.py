from abc import ABC, abstractmethod

# Printer interface
class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file: str) -> bool:
        """Method to print a document"""
        pass

# Scanner interface
class IScanner(ABC):
    @abstractmethod
    def scan(self, content: str) -> bool:
        """Method to scan a document"""
        pass

class SamsungPrinter(IPrinter, IScanner):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """Method to print a document"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("Printing document {}!".format(file))
            return True
        return False

    def scan(self, content):
        """Method to scan a document"""
        if self.is_connected:
            print("Saving {} as an image file.".format(content))
            return True
        return False

class LGPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """Method to print a document"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("Printing document {}.".format(file))
            return True
        return False
