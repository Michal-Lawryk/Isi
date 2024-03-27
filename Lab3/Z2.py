import sqlite3

conn = sqlite3.connect('university.db')
c = conn.cursor()
c.execute('INSERT INTO uczelnia (Id_uczelni, Nazwa, Adres) VALUES(1, "UM", "Morska 81/87, 81-225 Gdynia")')
c.execute('INSERT INTO wydzial (Id_wydzialu, Nazwa, Id_uczelni) VALUES (1, "Elektryczny", 1), (2, "Mechaniczny", 1)')
c.execute('INSERT INTO `wykladowca` (`Id_wykladowcy`, `Imie`, `Nazwisko`, `Stopien_naukowy`, `Id_wydzialu`) VALUES(1, '
          '"Eugenia", "Pachnik", "inż.", 1), (2, "Nina", "Rut", "dr. inż.", 2),(3, "Tobiasz", "Faliszewski", '
          '"dr. hab.", 2), (4, "Mieczysław", "Labudda", "prof.", 1), (5, "Radosław", "Jerzyk", "dr.", 1)')
c.execute('INSERT INTO przedmiot (Id_przedmiotu, Nazwa, Id_wykladowcy) VALUES(1, "Sys. Oper.", 5),(2, '
          '"Budowa silnika", 2),(3, "Telekomunikacja", 1),(4, "Inż. Produkcja", 3),(5, "Instalacja", 4)')
c.execute('INSERT INTO grupa_studencka (Id_grupy, Nazwa_grupy, Kierunek, Id_wydzialu) VALUES(1, "Inf", "Informatyka", 1),'
          '(2, "IP", "Inż. Produkcji", 2)')
c.execute('INSERT INTO student (Nr_albumu, Imie, Nazwisko, Id_grupy) VALUES(1, "Tomasz", "Sędek", 1),(2, "Kornelia", '
          '"Kotwica", 1),(3, "Edward", "Kotyrba", 1),(4, "Nikola", "Mech", 2),(5, "Lucjan", "Łabaj", 2),(6, "Kornel", '
          '"Jaskóła", 2)')
c.execute('INSERT INTO ocena (Id_oceny, Wartosc, Nr_albumu, Id_przedmiotu) VALUES(1, 3.5, 1, 1),(2, 5, 1, 2),(3, 2, '
          '1, 3),(4, 5, 1, 4),(5, 4, 1, 5),(6, 3, 2, 1),(7, 4.5, 2, 2),(8, 4, 2, 3),(9, 4, 2, 4),(10, 3, 2, 5),(11, '
          '5, 3, 1),(12, 5, 3, 2),(13, 4.5, 3, 3),(14, 5, 3, 4),(15, 3.5, 3, 5),(16, 3, 4, 1),(17, 3, 4, 2),(18, 3, '
          '4, 3),(19, 3, 4, 4),(20, 3, 4, 5),(21, 3.5, 5, 1),(22, 4.5, 5, 2),(23, 4, 5, 3),(24, 3.5, 5, 4),(25, 3.5, '
          '5, 5),(26, 4, 6, 1),(27, 4, 6, 2),(28, 5, 6, 3),(29, 5, 6, 4),(30, 4.5, 6, 5)')
conn.commit()
conn.close()
