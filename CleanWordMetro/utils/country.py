from config import connection
import utils.player as playerUtil

def getCurrentCountryData(player):
    playerId = player[0]
    sql = "select country.id, country.name, country.isClean from country, city, player"
    moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    finalSql = f"{moreSql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    return result[0]

def changeIsCountryClean(country):
    isCountryClean = country[2]
    print(isCountryClean)
    if isCountryClean == 0:
        isCountryClean = 1
    else:
        isCountryClean = 0
    return isCountryClean

def updateIsCountryClean(country):
    currentCountryId = country[0]
    newIsCountryClean = changeIsCountryClean(country)
    print(newIsCountryClean)


# currentPlayer = playerUtil.getPlayerByName("Trung")
#
# currentCountry = getCurrentCountryData(currentPlayer)
# # print(currentCountry)
# # newIsCountryClean = changeIsCountryClean(currentCountry)
# # print(newIsCountryClean)
# updateIsCountryClean(currentCountry)