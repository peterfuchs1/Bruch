from __future__ import print_function
__author__ = 'Walter Rafeiner-Magor'
class Employee(object):
    """Doc-String der Klasse """
    empCount = 0 # Klassenattribut

    def __init__(self, name, salary):
        """
        Konstruktor
        :param name: Name des Mitarbeiters
        :param salary: Gehalt des Mitarbeiters
        """
        self.name = name        # Objektattribut
        self.salary = salary    # Objektattribut
        Employee.empCount += 1
    @staticmethod
    def displayCount():
        """
        Gibt die Anzahl der Objekte aus
        :return: void
        """
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        """
        Ausgabe eines Mitarbeiters
        :return: void
        """
        print ("Name : ", self.name,  ", Salary: ", self.salary)


# Unser erstes Objekt der Klasse
emp1 = Employee("Andrea", 2000)
# Das wird unser zweites Objekt
emp2 = Employee("Franziska", 5000)
# Ausgabe der Mitarbeiter
emp1.displayEmployee()
emp2.displayEmployee()
# Ausgabe der Anzahl aller Mitarbeiter
print ("Total Employee %d" % Employee.empCount)
# Mit Attributen waehrend der Laufzeit arbeiten:
hasattr(emp1, 'age')    # True, falls das Attribut 'age' existiert
setattr(emp1, 'age', 8) # Setter fuer das Attribut 'age'
getattr(emp1, 'age')    # Getter fuer das Attribut 'age'
delattr(emp1, 'age')    # Das Attribute 'age' wird geloescht!