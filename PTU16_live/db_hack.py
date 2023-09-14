import sqlite3

db_conn = sqlite3.connect('PTU16_live/db/klientai.db')
cursor = db_conn.cursor()

vardas = input("Įveskite vardą: ")
with db_conn:
    cursor.execute(f'SELECT * FROM client WHERE first_name = "{vardas}"')
    clients = cursor.fetchall()
if clients:
    for client in clients:
        print(client)
