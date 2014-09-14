Einfuehrungsbeispiel Python OOP
===============================

.. bibliographic fields:

:Author: Walter Rafeiner-Magor
:organization: TGM Wien
:date: $Date: 2014-09-14 $
:status: This is a "work in progress"
:revision: $Revision: 0.01 $
:version: 1

.. contents:: Inhaltsverzeichnis


Klassenstruktur
---------------
    - Objekt-Attribute
        - name: Name des Mitarbeiters
        - salary: Gehalt des Mitarbeiters

    - Klassen-Attribute
        - empCount: Anuahl der Objekte

Unser erstes Objekt der Klasse
------------------------------

    emp1 = Employee("Zara", 2000)

Das wir unser zweites Objekt
----------------------------

    emp2 = Employee("Manni", 5000)

Ausgabe der Mitarbeiter
------------------------

    emp1.displayEmployee()
    emp2.displayEmployee()

Ausgabe der Anzahl aller Mitarbeiter
------------------------------------


    print ("Total Employee %d" % Employee.empCount)
