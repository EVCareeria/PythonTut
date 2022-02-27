import http.client
import sqlite3
import datetime
aika = datetime.datetime.now()
conn = sqlite3.connect('Tehtävä.db')
sql = """CREATE TABLE IF NOT EXISTS Paikkakunnat (
         nimi text)"""
kursori = conn.cursor()
kursori.execute(sql)
kysymys = input("haluatko muuttaa seurattavia paikkakuntia? vastaa k kyllä tai e ei:  ")
nimi = ""
if kysymys == "e":
    quit()
else:
    sql = "DELETE FROM Paikkakunnat"
    kursori = conn.cursor()
    kursori.execute(sql)
    print("Eka if lause")
    while nimi != "x":
        print("Paina x lopettaaksesi")
        nimi = input("Anna paikkakunnan nimi: ")
        if nimi == "x":
            break
        sql = f"INSERT INTO Paikkakunnat VALUES ('{nimi}')"
        kursori.execute(sql)
        conn.commit()
sql = "SELECT * FROM Paikkakunnat"
for rivi in kursori.execute(sql):
    print(rivi)
vastaus2 = input("Haluatko hakea lämpötilatiedon ilmatieteenlaitokselta? k kyllä:  ")
summa = 0
if vastaus2 != "k":
    quit()
else:
    
    for kaupunki in kursori.execute(sql):
        tiedosto = open("Lokitiedosto.txt", "a")
        try:
            
            str_kaupunki = ",".join(kaupunki)
            conn2 = http.client.HTTPSConnection("www.ilmatieteenlaitos.fi")
            conn2.request("GET", "/saa/" + str(str_kaupunki))
            html_vastaus = conn2.getresponse()
            html = str(html_vastaus.read())
            indeksi = html.index('Temperature')
            alku = indeksi+12
            loppu = alku+3
            lämpötila = html[alku:loppu]
            if int(lämpötila.replace('.', '')) > 99:
                lämpötila = lämpötila[:-1]
            summa += 1
            print(str(aika) + ":  " + str(str_kaupunki) + ":   " + lämpötila)
        except:
            tiedosto.write(str(aika)+ ": " + str(str_kaupunki) + ":  Hakuvirhe! " + "\r\n ")
            pass
    tiedosto.write(str(aika) + ": " + str(summa)  + ": " "Paikkakunnan tiedot haettiin onnistuneesti! " + "\r\n ")
    tiedosto.close()
conn2.close()
conn.close()
