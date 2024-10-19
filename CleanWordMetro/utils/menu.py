import sys

from config import connection
import utils.player as playerUtils


def getPlayers():
    sql = "SELECT * from player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("this is",result)
    # result =runSQL(sql)
    return result

def isExist(username,namesInDatabase ):
    if username.lower() in namesInDatabase:
        return True
    else:
        return False

def formatedNameList(nameListFromDatabase): # return onlyNameList
    onlyNameList = []
    for nameData in nameListFromDatabase:
        nameInData = nameData[1].lower() # return nameList in lowercase
        # print('this is lower case',
        #       nameData[1].lower())
        # print(nameInData)
        onlyNameList.append(nameInData)
    # print(onlyNameList)
    return onlyNameList

def getNewPlayerData(userName) :
    defaultStat = 1
    defaultLocation = 1
    defaultIsInCity = 1
    defaultEnergy = 3
    defautIsNew = 1
    newPlayerData = [userName,defaultStat,defaultLocation,defaultIsInCity,defaultEnergy,defautIsNew]
    return newPlayerData

def inputName():
    name = input("Type your username: ")
    return name

def existNameGUI(name):
    print("Welcoome back,",name)
    print("1.New game")
    print("2.Continue")
    print("3.Exit program")
    option = input("Please enter your option(1-3): ")
    return option

def optionWithExistNameGUI(option,username):
    if option == "1":
        oldPlayerData = playerUtils.getPlayerByName(username)
        playerUtils.setDefaultData(oldPlayerData)
        print(f"Welcome to new game! {username}")
        playerData = playerUtils.getPlayerByName(username)
        formattedPlayerData = playerUtils.formatPlayerData(playerData)
        return formattedPlayerData

        # return a newData for this user
    elif option == "2":
        playerData = playerUtils.getPlayerByName(username)
        # print("Here is your point and your stamina !")
        formattedPlayerData = playerUtils.formatPlayerData(playerData)

        return formattedPlayerData
    elif option == "3":
        print("End process")
        sys.exit()
    else:
        print("Invalid number, please type in range(1/2/3)")
        existNameGUI(username)

def nonExistGUI(username):
    print(f"Congratulation !! It is a new name! {username}")
    print("1.New game")
    print("2.Exit program")
    option = input("Please enter your option(1/2): ")
    while (option == "1"):
        return option

    nonExistGUI(username)

def optionNonExistGUI(option,username):
        if option == "1":
            newPlayer = getNewPlayerData(username)            # insert new player
            playerUtils.insertNewPlayer(newPlayer)
            print("New User has been created Successfully!")
            print(f"Welcome to Clean World!!! {username}")
            newPlayerData= playerUtils.getPlayerByName(username)
            newFormattedPlayerData = playerUtils.formatPlayerData(newPlayerData)

            return newFormattedPlayerData

        elif option == "2":
            print("End process")
            sys.exit()
        else:
            print("Invalid number, please type in range(1/2)")
            nonExistGUI(username)
            # anotherOption = int(input("Invalid number, please type in range(1/2)"))
            # nonExistGUI(anotherOption)
def menu():
    username =inputName()
    nameListInDatabase = getPlayers() # return list of username
    onlyNameList = formatedNameList(nameListInDatabase)
    # print(nameInDatabase)
    while True:
        if isExist(username,onlyNameList) == True:
            # menu.existNameGUI()
            option = existNameGUI(username)
            player = optionWithExistNameGUI(option,username)

        else:
            option = nonExistGUI(username)
            player = optionNonExistGUI(option,username)


        return player # return a player

#return a name


# player = menu()
# print("after menu",player)
# optionWithExistNameGUI(1,"Huy")