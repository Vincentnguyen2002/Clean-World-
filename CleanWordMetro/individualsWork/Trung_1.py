from config import connection

# // user play game
# // 1. New Game
# 2. Continue


def newPlayerData(name): # create a newPlayer record
    #id,name,resStat,location,isInCity, energy, isNew
    nameData = [name,1,1,1,3,1]
    return nameData


# sql_update = f"INSERT INTO quiz_user_answer VALUES {userAnswerTuple}"


def insertNewPlayer (nameData):
    nameDataToTuple = tuple(nameData)
    playerComlumn = "name, resStat, location, isInCity, energy, isNew"
    sql = f"INSERT INTO player({playerComlumn}) VALUE {nameDataToTuple}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result #result user answer as a

name ="Trung1"
newPlayer = newPlayerData(name)
insertNewPlayer(newPlayer)