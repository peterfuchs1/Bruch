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
emp1 = Employee("Zara", 2000)
# Das wir unser zweites Objekt
emp2 = Employee("Manni", 5000)
# Ausgabe der Mitarbeiter
emp1.displayEmployee()
emp2.displayEmployee()
# Ausgabe der Anzahl aller Mitarbeiter
print ("Total Employee %d" % Employee.empCount)
