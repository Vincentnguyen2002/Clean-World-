from config import connection
# import utils.robot as robotUtil
# import utils.city as cityUtil
import utils.robot as robotUtil
import utils.city as cityUtil

# import importlib

# cityUtil = importlib.import_module('')

def insertNewPlayer (nameData):
    nameDataToTuple = tuple(nameData)
    playerComlumn = "name, resStat, location, isInCity, energy, isNew"
    sql = f"INSERT INTO player({playerComlumn}) VALUE {nameDataToTuple}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result #result user answer as a

def playerToTuple(player):
    playerTuple = tuple(player)
    # print(playerTuple)
    return playerTuple

def getPlayerByName(name):
    sql = "Select * from player "
    finalSql = sql + "where name = '" +name + "'"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    formattedPlayerData = formatPlayerData(result[0])
    return formattedPlayerData


def getPlayerByID(id):
    sql = "SELECT * from player "
    finalSql = sql + "where id  =" + str(id)
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    # print(result)
    # print("this is", result)
    # result =runSQL(sql)
    # for player in result:
    #     print(player)
    formattedResult = formatPlayerData(result[0])
    return formattedResult

# player =  (3, 'testPlayer', 5, 1, 1, 3, 0)

# format a player data from a tuple to a list
def formatPlayerData(player):
    formattedData = []
    for value in player:
        formattedData.append(value)
    return formattedData

def getCurrentPlayerLocationId(player):
    currentLocationId = player[3]
    return currentLocationId

def changeIsNew(player):
    isNew = player[6]
    if isNew == 0:
        isNew = 1
    else:
        isNew = 0
    return isNew

def updateIsNew(player):
    currentPlayerId = player[0]
    updateIsNew = changeIsNew(player)
    sql = "update player"
    moreSql = sql + " SET isNew = " + str(updateIsNew)
    finaSql = moreSql + " where id= "  + str(currentPlayerId) + ""
    cursor = connection.cursor()
    cursor.execute(finaSql)
    result = cursor.fetchall()
    return result

def updateStat(player, newStat):
    currentPlayerId = player[0]
    sql = "update player"
    moreSql = sql + " SET resStat = " + str(newStat)
    finalSql = moreSql + " where id= "  + str(currentPlayerId) + ""
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    print("Your stat have been updated")
    return result

def showPlayerInfo(player):
    playerName = player[1] # playerName
    playerStat = player[2] # playerStat
    playerLocation = player[3] #playerLocation
    playerInfo = f"player: {playerName} -- Stat: {playerStat} -- Location: {playerLocation}"
    print(playerInfo)
    return

def setDefaultData(player):
    currentPlayerId = player[0]
    defaultIsNew = 1
    defaultResStat = 1
    defaultLocationId = 1
    sql = "update player"
    moreSql = f"{sql} SET resStat = {str(defaultResStat)}, isNew = {defaultIsNew}, location = {defaultLocationId}"
    finaSql = moreSql + " where id= "  + str(currentPlayerId) + ""
    cursor = connection.cursor()
    cursor.execute(finaSql)
    result = cursor.fetchall()
    return result

def isNewPlayer(player):
    isNew = player[6]
    if isNew == 1:
        return True
    else:
        return False

# def refillEnergy(player):
#     energy = player[5]


def updatelocation(player,newLocationID):
    currentPlayerId = player[0]
    sql = "update player"
    moreSql = sql + " SET location = " + str(newLocationID)
    finalSql = moreSql + " where id= " + str(currentPlayerId) + ""
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    print("Your location have changed.")
    return result


def changelocationID (player):
    currentLocationID = player[3]
    newLocationId = currentLocationID + 1
    player[3] = newLocationId
    updatelocation(player,newLocationId)
    # print(player)

def getDefautlStat (player,robotList):
    playerStat = player[2]
    robotLowestStat = robotList[0][3]
    # print("Robot lowest Stat",robotList[0][3])
    playerStat = robotLowestStat


    return playerStat


def movetoNewCity(resultOfIsCleanCity,player,city,country):

    cityList = cityUtil.getCityListInCurrentCountry(country)
    formattedCityList = cityUtil.formatCityList(cityList)
    isLast = cityUtil.isLastCity(city, formattedCityList)
    if resultOfIsCleanCity: # if the city is clean
        if isLast:
            print("You have clean the last city")
            print("Congratulation!! You have clean the world")
        else:
            print(f"Congrat on cleaning {city[1]} ")
            print("You will go to the next city shortly")
            changelocationID(player)
    # print(isLast)
    # if resultOfCleanCity == True:
    #     if
    return

    # return




# def updating(player):
#     location_id = player[3]
#     sql = "update player"
#     moresql = sql + " set location=" + str(location_id) + ""
#     finaSql = moresql + " where id=" + str(player[0]) + ""
#     cursor = connection.cursor()
#     cursor.execute(finaSql)
#     result = cursor.fetchall()
#     if cursor.rowcount > 0:
#         return result

# playerName = "Huy"
#
# player = getPlayerByName(playerName)
# # print(player)
# city = cityUtil.getCurrentCityData(player) # call city first so need to put import in city at first
# # print(city)
# boss = robotUtil.getCurrentBossData(player)
# # print(boss)
# changeLocation(player,boss,city)

# print(player)
# print(getCurrentPlayerLocationId(player))
# name = "Huy"
# player = getPlayerByName(name)
# showPlayerInfo(player)
# player = (2, 'Huy', 2, 1, 0, 3, 0)
# # print(updateIsNew(player))
# # updateStat(player,3)
# # print(getPlayerByName("Huy"))
# # print(player)
# getPlayerByID(1)