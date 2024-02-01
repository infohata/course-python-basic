import sqlite3

connector = sqlite3.connect('zmones.db')
cursor = connector.cursor()

def create_table(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    query = '''
CREATE TABLE IF NOT EXISTS friends (
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(250)
);
'''
    cursor.execute(query)
    connector.commit()

def insert_friend(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print("Inserting a friend...")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("E-mail: ")
    cursor.execute("INSERT INTO friends (first_name, last_name, email)"
                    "VALUES (?, ?, ?)", (first_name, last_name, email))
    connector.commit()
    print("Done.")

def print_friends(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print("Friends List:")
    with connector:
        cursor.execute("SELECT * FROM friends")
        friends = cursor.fetchall()
    for friend in friends:
        print(f"{friend[0]} {friend[1]}, {friend[2]}")

def find_by(connector: sqlite3.Connection, cursor: sqlite3.Cursor, find_by: str):
    query = f'SELECT * FROM friends WHERE {find_by} = ?'
    search_argument = input(f"Find friends by {find_by.replace('_', ' ')}: ")
    with connector:
        cursor.execute(query, (search_argument, ))
        friends = cursor.fetchall()
    if len(friends) > 0:
        for friend in friends:
            print(f"{friend[0]} {friend[1]}, {friend[2]}")
    else:
        print("No friends found.")

if __name__ == "__main__":
    create_table(connector, cursor)
    while True:
        choice = input("Enter Command (h or help for help): ")
        if choice.lower() in ["q", "quit"]:
            break
        if choice.lower() in ["h", "help"]:
            print('h, help\t\tthis help')
            print('q, quit\t\tquit this program')
            print('i, insert\tinsert a friend')
            print('a, all\t\tprint all friends')
            print('ff\t\tfind by first name')
            print('fl\t\tfind by last name')
            print('fe\t\tfind by email')
        if choice.lower() in ["i", "insert"]:
            insert_friend(connector, cursor)
        if choice.lower() in ["a", "all"]:
            print_friends(connector, cursor)
        if choice.lower() in ["ff"]:
            find_by(connector, cursor, "first_name")
        if choice.lower() in ["fl"]:
            find_by(connector, cursor, "last_name")
        if choice.lower() in ["fe"]:
            find_by(connector, cursor, "email")

    connector.close()
