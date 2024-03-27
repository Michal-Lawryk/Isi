import sqlite3

conn = sqlite3.connect('university.db')
c = conn.cursor()

c.execute('CREATE TABLE uczelnia( Id_uczelni INT NOT NULL, Nazwa VARCHAR(30) NOT NULL, Adres VARCHAR(50) NOT NULL, '
          'PRIMARY KEY (Id_uczelni))')

c.execute('CREATE TABLE wydzial( Id_wydzialu INT NOT NULL, Nazwa VARCHAR(20) NOT NULL, Id_uczelni INT NOT NULL, '
          'PRIMARY KEY (Id_wydzialu),  FOREIGN KEY (Id_uczelni) REFERENCES Uczelnia(Id_uczelni))')

c.execute('CREATE TABLE grupa_studencka( Id_grupy INT NOT NULL, Nazwa_grupy VARCHAR(10) NOT NULL, Kierunek VARCHAR(15) '
          'NOT NULL, Id_wydzialu INT NOT NULL, PRIMARY KEY (Id_grupy), FOREIGN KEY (Id_wydzialu) REFERENCES '
          'Wydzial(Id_wydzialu))')

c.execute('CREATE TABLE wykladowca(  Id_wykladowcy INT NOT NULL,  Imie VARCHAR(15) NOT NULL,  Nazwisko VARCHAR(20) '
          'NOT NULL,  Stopien_naukowy VARCHAR(20) NOT NULL,  Id_wydzialu INT NOT NULL,  PRIMARY KEY (Id_wykladowcy),  '
          'FOREIGN KEY (Id_wydzialu) REFERENCES Wydzial(Id_wydzialu))')

c.execute('CREATE TABLE przedmiot(  Id_przedmiotu INT NOT NULL,  Nazwa VARCHAR(15) NOT NULL,  Id_wykladowcy INT NOT '
          'NULL,  PRIMARY KEY (Id_przedmiotu),  FOREIGN KEY (Id_wykladowcy) REFERENCES Wykładowca(Id_wykladowcy))')

c.execute('CREATE TABLE student(  Nr_albumu INT NOT NULL,  Imie VARCHAR(15) NOT NULL,  Nazwisko VARCHAR(20) NOT NULL, '
          ' Id_grupy INT NOT NULL,  PRIMARY KEY (Nr_albumu),  FOREIGN KEY (Id_grupy) REFERENCES Grupa_studencka('
          'Id_grupy))')

c.execute('CREATE TABLE ocena(  Id_oceny INT NOT NULL,  Wartosc FLOAT NOT NULL,  Nr_albumu INT NOT NULL,  '
          'Id_przedmiotu INT NOT NULL,  PRIMARY KEY (Id_oceny),  FOREIGN KEY (Nr_albumu) REFERENCES Student('
          'Nr_albumu),  FOREIGN KEY (Id_przedmiotu) REFERENCES Przedmiot(Id_przedmiotu))')

conn.close()
