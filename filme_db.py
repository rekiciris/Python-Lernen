import sqlite3
verbindung = sqlite3.connect("meine_filme.db")
cursor = verbindung.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS filme (id INTEGER PRIMAR KEY, titel TEXT, jahr INTEGER, bewerung REAL)")
meine_favoriten = [
    (1, 'Inception', 2014, 8.8),
    (2, 'The Dark Knight', 2008, 9.0),
    (3, 'Interstellar', 2014, 8.7)
]
# 'INSERT OR IGNORE' verhindert Fehler, falls man das Skript mehrmals startet
cursor.executemany("INSERT OR IGNORE INTO filme VALUES (?, ?, ?, ?)", meine_favoriten)
# Speichern der Änderungen
verbindung.commit()
# Test-Check in der KOnsole
print("--- Deine Filmdatenbank ---")
cursor.execute("SELECT * FROM filme")
for zeile in cursor.fetchall():
    print(f"Film: {zeile[1]} | Jahr: {zeile[2]} | Rating: {zeile[3]}")
#Verbindung sauber schließen
verbindung.close()