# import utils.quiz as quiz
import sys

from config import connection

import utils.player as playerUtil
import utils.quiz as quizUtil
import utils.robot as robotUtil
import utils.city as cityUtil
import utils.country as countryUtil


def inCityGui():
    # print("What do you want to do \n"
    #       "1. go meet the boss \n"
    #       "2. Go farm\n"
    #       "3. Go play quiz\n"
    #       "4. Do nothing\n")
    print("What do you want to do \n"
          "1. go meet the boss \n"
          "2. Go farm\n"
          "3. Go play quiz\n"
          "4. Do nothing\n"
          "5. Quit\n")
    option = input("What do you want to do? (1-5) ")
    return int(option)


def chooseOptionInCity(number,player,boss,city,country):
    robotList = robotUtil.getRobotsByLocation(player)
    # print(robotList)
    defaultPlayerStat = playerUtil.getDefautlStat(player,robotList)
    # print("This is default PlayerStat",defaultPlayerStat)
    # print(defaultPlayerStat)
    if number == 1:
        print("Let go to boss room")
        robotUtil.meetBoss(player,boss,city,country)
    if number == 2:
        print("Let's defeat some robots!")
        robotUtil.fight(player,boss,defaultPlayerStat)
    if number == 3:
        print("let's answer some quiz!")
        quizUtil.quiz(player,boss,defaultPlayerStat)
    if number == 4:
        print("do nothing")
    if number == 5:
        print("Thank you for playing.")
        print("See you again.")
        sys.exit()

def getPlayers():
    sql = "SELECT * from player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("this is",result)
    # result =runSQL(sql)
    return result

def isExist(username,namesInDatabase ):
    if username in namesInDatabase:
        return True
    else:
        return False

def formatedNameList(nameListFromDatabase): # return onlyNameList
    onlyNameList = []
    for nameData in nameListFromDatabase:
        nameInData = nameData[1]
        # print(nameInData)
        onlyNameList.append(nameInData)
    # print(onlyNameList)
    return onlyNameList

def introducton(name):
    print(f"Background:\nOur world CLEAN WORLD has been deserted and polluted one since the great war between Humans and Robots."
          f"\nLuckily there are still some remaining clean cities.Our hero {name} is currently living at Helsinki ,"
          f"\nOn one sunny day, when our hero was going picnic with his mother, a robot was nearby and it attacked them.\n"
          f"Luckily, one of the city’s guard is nearby and he was able to save them."
          f"\nHowever, due to an overexposure with the polluted energy from the robot, our hero’s mother was not able to survive."
          f"\nIn order to revenge his mother, he decided to destroy all the robots in the world."
          f"\nThe elder told him that the sauce of all the robot is from the factory in a city beyond the hill."
          f"\nTherefore, he decided to go to the next city to destroy the robots there")
def showIntroduction(player):
    name = player[1]
    if playerUtil.isNewPlayer(player):
        introducton(name)
        playerUtil.updateIsNew(player)
def game(player):
    while True:
        playerId = player[0]
        boss = robotUtil.getCurrentBossData(player)
        city =  cityUtil.getCurrentCityData(player)
        country = countryUtil.getCurrentCountryData(player)
        updatedPlayer =playerUtil.getPlayerByID(playerId)

        # playerInfo = playerUtil.showPlayerInfo(updatedPlayer)
        print(f"Welcome to {city[1]}")
        playerUtil.showPlayerInfo(updatedPlayer)
        showIntroduction(updatedPlayer)

        playerOption = inCityGui()
        chooseOptionInCity(playerOption,updatedPlayer,boss,city,country)

    # return playerOption


# #
# player = playerUtil.getPlayerByName("Trung")
# print(player)
# newStat = player[2] = 5
# print(player)
#
# boss = robotUtil.getCurrentBossData(player)
# city = cityUtil.getCurrentCityData(player)
# country = countryUtil.getCurrentCountryData(player)
# cityList = cityUtil.getCityListInCurrentCountry(country)
# formattedCityList = cityUtil.formatCityList(cityList)
# robotUtil.meetBoss(player,boss,city,country)
# print(playerUtil.changeLocation())
# print(formattedCityList)
# # playerUtil.changeLocation(player,boss,city)


# # print(boss)
# formatedData = playerUtil.formatPlayerData(player)
# game(player)
