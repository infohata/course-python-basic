import sqlite3
conn = sqlite3.connect("PTU12_live/db_scripts/zmones.db")
c = conn.cursor()

while True:
    print("""===[ Draugų katalogas ]===
    1 - Paieška pagal vardą
    2 - Įterpimas
    visa kita - išeiti
    ---
    """)
    choice = input("Pasirinkite: ")
    if choice == "1":
        vardas = input("Draugo vardas: ")
        with conn:
            # c.execute(f'SELECT * FROM draugai WHERE first_name = "{vardas}"')
            c.execute('SELECT rowid, * FROM draugai WHERE first_name = ?', (vardas, ))
            draugai = c.fetchall()

        if draugai and len(draugai) > 0:
            for draugas in draugai:
                print(draugas)
        else:
            print("Tokių draugų mes neturim...")
    elif choice == "2":
        first_name = input("Vardas: ")
        last_name = input("Pavardė: ")
        email = input("E-mail: ")
        with conn:
            c.execute("""INSERT INTO draugai 
            (first_name, last_name, email) 
            VALUES(?, ?, ?)""", (first_name, last_name, email))
        print(f"{first_name} įvestas.")
    else:
        break

c.close()