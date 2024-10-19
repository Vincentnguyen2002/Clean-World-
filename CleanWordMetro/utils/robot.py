from config import connection
#careful with importing order
# import utils.player as playerUtil
# import utils.city as cityUtil

import random


def getCurrentBossData(player):
    locationId = player[3]
    # sql = "SELECT name, type, pollustat,location FROM robot where id=" + str(bot_id)
    selectFields = "robot.id,robot.name,robot.type,robot.pollustat,robot.location,robottype.description"
    sql = f"SELECT {selectFields} FROM robot,robottype"
    final = (f"{sql} WHERE robot.type = robottype.id and"
             f" location= {locationId} and robottype.name ='boss'")
    cursor = connection.cursor()
    cursor.execute(final)
    result = cursor.fetchall()
    # print(result)
    # for row in result:
    #     print(f'Name: {row[0]}\nType: {row[1]}\nPollution Stats: {row[2]}\nLocation: {row[3]}')
    return result[0]

def getRobotsByLocation(player):
    locationId = player[3]
    selectFields = "robot.id, robot.name, robot.type, robot.pollustat, robot.location, robottype.description"
    sql = f"SELECT {selectFields} FROM robot,robottype"
    final = (f"{sql} WHERE robot.type = robottype.id and"
             f" location= {locationId} ")
    cursor = connection.cursor()
    cursor.execute(final)
    result = cursor.fetchall()
    # print(result)
    return result

def filterRobotList(player,robotList):
    playerStat = player[2]
    filteredList = []
    for robot in robotList:
        robotStat = robot[3]
        if robotStat >= playerStat:
            filteredList.append(robot)
    # print(filteredList)

    return filteredList

def getRandomRobot(robotList):
    randomRobot = random.choice(robotList)
    # print(randomRobot)
    return randomRobot

def getRobotType(robot):
    robotType = robot[2]
    return robotType

def isNormalRobot(robotType):
    if robotType == 1:
        return True
def isBossRobot(robotType):
    if robotType == 2:
        return True

# (3, 'Robot3', 1, 3, 1, 'Normal Robot is normal')
def isWinAgainstNormalRobot(player,robot):
    playerStat = player[2]
    # print(robot)
    robotStat = robot[3]
    if playerStat+1 >= robotStat:
        return True
    else:
        return False

def isWinAgainstBossRobot(player,boss):
    playerStat = player[2]
    # robot(boss)
    bossStat = boss[3]
    if playerStat == bossStat:
        return True
    else:
        return False

# def MatchI
# def insertMatch(matchInfo):


def isWinWhenFarm(player,robot):

    robotType = getRobotType(robot)
    if isNormalRobot(robotType):
        print("You have meet a normal robot")
        isWinResult = isWinAgainstNormalRobot(player,robot)
    elif isBossRobot(robotType):
        print("Oh No! you meet the city guardian")
        isWinResult = isWinAgainstBossRobot(player,robot)
    return isWinResult ## if player win against normal robot or boss robot

def getIsWinId(isWin):
    if isWin:
        return 1
    else:
        return 0

def insertMatchData(matchData):
    matchDataTuple = tuple(matchData)
    matchColumns = "player_id, robot_id, isWin"
    sql = f"INSERT INTO match_game ({matchColumns}) Value {matchDataTuple}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Match data inserted successfully")
    return result #result user answer as a

def showRobotInfo(robot):
    robotName = robot[1]
    robotStat = robot[3]
    robotDescription = robot[4]
    robotInfo = (f"robot: {robotName } -- Stat: {robotStat}  "
                 f"-- Description: {robotDescription}")
    print(robotInfo)
    return




def match(player,robot,boss,playerDefaultStat):
    playerUtil.showPlayerInfo(player)
    showRobotInfo(robot)
    playerStat = player[2]
    bossStat = boss[3]
    isBoss = isBossRobot(robot)
    # robotStat = robot[3]
    # robotType = getRobotType(robot)
    win = isWinWhenFarm(player,robot)

    if win and isBoss:
        # if isBoss:
        print("Boss walks away")
    elif win and not isBoss :
        print("Congrat! You have win")
        playerStat += 1
        playerStat = min(playerStat,bossStat)

    else:
        print("Poor you! You have loses")
        playerStat -= 1
        playerStat = max(playerStat,playerDefaultStat)
    return  [playerStat,win]


# def isWinBoss(player, boss):  # have we defeat boss
#     winBoss = isWinAgainstBossRobot(player, boss)
#     if winBoss:
#         return True
#     else:
#         return False


# return new player Stat if win
def fightBossGuardian(isWinBoss,player):
    playerStat = player[2]
    if isWinBoss:
        print("You have defeat the Boss Robot")
        playerStat += 1
    return playerStat

# def defeatBoss(player,boss):
#     #edit logic so that player Stat go to boss Stat + 1
#     # isClean = city[3] # return stat of isClean
#     # playerStat= player[2]
#     # bossStat = boss[3]
#     win = robotUtil.isWinAgainstBossRobot(player,boss)
#     if win:
#         return True
#     # print("You have defeate the guardian",win)
#     ## insert match
#     else:
#         return False





def fightBoss(player,boss):
    # boss = getCurrentBossData(player)
    ## up date player stat to 6:
    isWinBoss = isWinAgainstBossRobot(player,boss)
    if isWinBoss:
        newPlayerStat = fightBossGuardian(isWinBoss,player)
        playerUtil.updateStat(player,newPlayerStat)
        print(newPlayerStat)

    else:
        print(" you are not strong enough")
        print(" the boss letting you go!.:")
    return isWinBoss

def meetBoss(player,boss,city,country):
    ## update player stat to the lowest of next location
    # and return the result of the match with boss
    resultFromMeetBoss = fightBoss(player,boss)

    isClean = city[3]# fetch current city isClean status
    if resultFromMeetBoss: ##
        ## when defeat the guardian
        ## update both boss status and isClean status
        ## return newIsClean status, and update it to database, from 0 to 1
        newIsClean = cityUtil.cleanCity(city)
        newLocationId = playerUtil.movetoNewCity(newIsClean,player,city,country)
        print(newLocationId)


        # return isClean
    else:
        # return isClean
        return



    # if winBoss:
    #change and update bossStatus
    # start to clean city
# change city.isClean from 0 to 1 :
# update new city.isClean status
# check if this city is the last one in the city list >> all city clean >> win:
# else:
# change player.location to next 1 ( check
# update player.location to database

    # isCleanCity(player,boss)

def fight(player,boss,defaultStat):

    player_name = player[1]
    robotList = getRobotsByLocation(player)  # get robot List at a location
    # boss = get_current_boss_data(player)  # get boss at a location
    # print("This is boss data",boss)
    filteredList = filterRobotList(player, robotList)  # filter robot list based on player stat
    # print("Robot List",filteredList)
    # defaultStat =1
    # print("This is a new robot list based on player",filterRobotList(player,robotList))

    randomRobot = getRandomRobot(filteredList)  # get random robot from filtered list
    # print("This is random robot", getRandomRobot(filteredList))
    # print("Wait here")
    # newPlayerStat = match(player, randomRobot, boss)
    result = match(player, randomRobot, boss,defaultStat) ##result = [newStat, isWin]
    newStat = result[0]
    isWin = result[1]
    isWinId = getIsWinId(isWin)
    playerId = player[0]
    robotId = randomRobot[0]
    matchData = [playerId,robotId,isWinId]

    insertMatchData(matchData)

    # print("This is match with robot), ",newPlayerStat)
    playerUtil.updateStat(player, newStat)

    newPlayerData = playerUtil.getPlayerByName(player_name)
    # print("This is new player data",newPlayerData)
    # return newPlayerData
    return

#player meet robot
# print("THis is robot List", robotList)
# player_name = "Trung"
# player = playerUtil.getPlayerByName(player_name)
# boss = getCurrentBossData(player)
# city = cityUtil.getCurrentCityData(player)
# # # robots = getRobotsByLocation(player)
# # # print(robots)
# # print(boss)
# # # bossInfo = showRobotInfo(boss)
# # # # updatePlayerData = fight(player,boss)
# print(player)
# player[2] = 5
# print(player)
# resultOfFightBoss = meetBoss(player,boss,city)
# print(resultOfFightBoss)


import utils.city as cityUtil
import utils.player as playerUtil
