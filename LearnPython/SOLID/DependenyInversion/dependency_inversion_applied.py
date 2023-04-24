from abc import ABC, abstractmethod

class IWeapon(ABC):
    @abstractmethod
    def use_on(self, other_character):
        pass

class Sword(IWeapon):
    """Sword class"""
    def __init__(self, damage):
        self.damage = damage

    def use_on(self, other_character):
        """Method for using the sword"""
        other_character.get_damage(self.damage)

class GameCharacter:
    """Game character class"""
    def __init__(self, name, hp, weapon: IWeapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def attack(self, other_character):
        """Method for attacking other users"""
        if self.hp > 0:
            self.weapon.use_on(other_character)
        else:
            print(self.name + " cannot attack because they have died.")

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def get_damage(self, damage):
        """Method for reducing own HP when attacked"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + " has died.")
        else:
            self.hp -= damage

    def __str__(self):
        """Method for returning remaining HP as a string"""
        return self.name + " has " + str(self.hp) + " HP remaining."


from abc import ABC, abstractmethod

class IExporter(ABC):
    @abstractmethod
    def export(self, new_name:str, document: Document):
        """Converts the document to the appropriate format for each conversion type and returns it."""
        pass

class CSVExporter(IExporter):
    """Class for converting documents to CSV format"""
    def export(self, new_name, document):
        """Converts the document to CSV format and returns it with the given name"""
        print("\nConverting document to CSV...")

        new_content = document.content.replace("|", ",")
        exported_document = Document(new_name, new_content)

        print("Conversion complete!\n")

        return exported_document

class HTMLExporter(IExporter):
    """Class for converting documents to HTML format"""
    def export(self, new_name, document):
        """Converts the document to HTML format and returns it with the given name"""
        print("\nConverting document to HTML...")

        new_content = """
<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
{}
</body>

</html>
        """.format(document.content)
        exported_document = Document(new_name, new_content)

        print("Conversion complete!\n")

        return exported_document

class ExportController:
    """Class for converting documents to a specific file type"""
    def __init__(self):
        self.exporter = None

    def set_exporter(self, exporter: IExporter):
        """Sets the appropriate converter for the file type you want to convert"""
        self.exporter = exporter

    def run_export(self, new_name, document):
        """Converts the file and returns it"""
        if self.exporter == None:
            print("Please select a converter.")
            return document

        return self.exporter.export(new_name, document)
