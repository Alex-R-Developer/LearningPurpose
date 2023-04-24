class Sword:
    """Sword class"""
    def __init__(self, damage):
        self.damage = damage

    def slash(self, other_character):
        """Method to use the sword"""
        other_character.get_damage(self.damage)


class GameCharacter:
    """Game character class"""
    def __init__(self, name, hp, sword: Sword):
        self.name = name
        self.hp = hp
        self.sword = sword

    def attack(self, other_character):
        """Method to attack other users"""
        if self.hp > 0:
            self.sword.slash(other_character)
        else:
            print(self.name + " cannot attack because they are dead.")

    def change_sword(self, new_sword):
        """Method to change the sword"""
        self.sword = new_sword

    def get_damage(self, damage):
        """Method to reduce own health when attacked"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + " has died.")
        else:
            self.hp -= damage

    def __str__(self):
        """Method to return remaining health as a string"""
        return self.name + " has {} health remaining.".format(self.hp)

class Document:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def content(self):
        """Method to return the content of the document"""
        return self._content

    def __str__(self):
        """Method to return document information as a string"""
        return "Document Name: {}\nDocument Content:\n{}".format(self._name, self._content)


class CSVExporter:
    """Class to convert a document to csv format"""
    def export(self, new_name, document):
        """Converts the document and returns it with the given name"""
        print("\nConverting to CSV format...")

        new_content = document.content.replace("|", ",")
        exported_document = Document(new_name, new_content)

        print("Conversion complete!\n")

        return exported_document


class HTMLExporter:
    """Class to convert a document to HTML format"""
    def convert(self, new_name, document):
        """Converts the document and returns it with the given name"""
        print("\nConverting to HTML format...")

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
    """Class to convert a document to a specific file format"""
    def __init__(self):
        self.exporter = None

    def set_exporter(self, exporter):
        """Sets the converter for the desired file type"""
        self.exporter = exporter

    def run_export(self, new_name, document):
        """Converts the file and returns it"""
        if self.exporter == None:
            print("Please select a converter")
            return document

        return self.exporter.export(new_name, document)
