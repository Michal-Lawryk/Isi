import sqlite3

conn = sqlite3.connect('university.db')

print("a. Wyświetl wszystkich studentów:")
querry = conn.execute('SELECT Nr_albumu, Imie, Nazwisko FROM student')
for x in querry:
    print(x)

print("\nb. Wyświetl studentów 1 grupy:")
querry = conn.execute('SELECT Imie, Nazwisko, Id_grupy FROM student WHERE Id_grupy=1')
for x in querry:
    print(x)

print("\nc. Wyświetl studentów, którzy z jednego przedmiotu otrzymali ocenę wyższą bądź równą 4:")
querry = conn.execute('SELECT * FROM student WHERE Nr_albumu in (SELECT Nr_albumu FROM ocena WHERE Wartosc>=4) GROUP '
                      'BY Nr_albumu')
for x in querry:
    print(x)

print("\nd. Wyświetl wszystkich wykładowców z prowadzonymi przez nich przedmiotami:")
querry = conn.execute('SELECT Imie, Nazwisko, Nazwa FROM wykladowca, przedmiot WHERE '
                      'przedmiot.Id_wykladowcy=wykladowca.Id_wykladowcy')
for x in querry:
    print(x)

print("\ne. Wyświetl wydział z wszystkimi jego grupami studenckimi:")
querry = conn.execute('SELECT Nazwa, Nazwa_grupy FROM wydzial, grupa_studencka WHERE wydzial.Id_wydzialu = '
                      'grupa_studencka.Id_wydzialu')
for x in querry:
    print(x)

print("\nf. Wyświetl wszystkich studentów wraz ze średnią arytmetyczną ich ocen")
querry = conn.execute('SELECT Imie, Nazwisko, AVG(wartosc) FROM student, ocena WHERE '
                      'student.Nr_albumu=ocena.Nr_albumu GROUP BY student.Nr_albumu')
for x in querry:
    print(x)

conn.close()
