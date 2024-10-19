import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="clean_world",
    user="root",
    password="1234",
    autocommit=True
)


def playerstat():
    sql = f"SELECT id, name, resStat, energy From player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f"{row[1]}, your stat is {row[2]} and energy is {row[3]}")
        player_id = row[0]
        return player_id

player = int(input("Enter player id: "))
playerstat()

def start():
    print("Welcome to the Game or sth!")
    print("Press 1. for New Game")
    print("Press 2. to Continue")
    print("Press 3. to Exit")
    option = int(input("Enter option: "))

    if option == 1:
        print("Create username for a new game:")
        username = input("Enter username: ")
        sql = f"select name from player where name = ('{username}')"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if result is not None:
            print(f"Welcome, {username}! Let's start!")
            sql = f"INSERT INTO player(name) VALUES ('{username}')"
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
        else:
            print("Username already taken! Enter a different username.")


    elif option == 2:
        existing_user = input("Enter existing username: ")
        sql = f"select name from player where name = ('{existing_user}')"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if result is not None:
            sql = f"INSERT INTO player(name) VALUES ('{existing_user}')"
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
        else:
            print(f"Welcome back {existing_user}!")
            sql = f"SELECT * FROM player WHERE name = ('{existing_user}')"
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
    elif option == 3:
        print("Exiting Game!")


start()
playerstat()
