import random

from config import connection


# connection = mysql.connector.connect(
#     host = "127.0.0.1",
#     port = 3300,
#     database = "clean_world",
#     user = "root",
#     password = "",
#     autocommit = True
player = []
boss = []
city = ""
def getTables():
    sql = "SHOW tables"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("this is",result)
    # result =runSQL(sql)
    for table in result:
        print(table)

# getCurrentCity():
# sql= "Select city.name from player, city"
# finalSql = f"WHERE player."

def getPlayers():
    sql = "SELECT * from player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("this is",result)
    # result =runSQL(sql)
    return result

def getPlayerByID(id):
        sql = "SELECT * from player "
        finalSql = sql + "where id =" +str(id)
        cursor = connection.cursor()
        cursor.execute(finalSql)
        result = cursor.fetchall()
        # print("this is", result)
        # result =runSQL(sql)
        # for player in result:
        #     print(player)
        return result[0]

def loadingPlayerByID(playerId):
    playerTuple = getPlayerByID(playerId)
    # print(playerTuple)
    currentPlayer = []
    for value in playerTuple:
        currentPlayer.append(value)
    # print(currentPlayer)
    return currentPlayer

def getPlayerByName(name):
    sql = "Select * from player "
    finalSql = sql + "where name = '" +name + "'"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    return result

def getRobotsInCity(city):
    sql = "SELECT robot.id, robot.name, robot.type, robot.pollustat from robot,city"
    moreSql =f"{sql} WHERE robot.location = city.id"
    finalSql =f"{moreSql} AND city.name = '{city}'"
    cursor = connection.cursor()
    cursor.execute(finalSql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    return result

def getRobotById(robotId):
    sql = "SELECT * FROM robot "
    resultSql = f"{sql} WHERE id ={robotId}"
    cursor = connection.cursor()
    cursor.execute(resultSql)
    result = cursor.fetchall()
    print("this is one robot", result)
    return result

# def getBoss():
#     getRobotById()

# player_info = []
def getMatches():
    sql = "SELECT * from match_game"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    for match in result:
        print(match)

def getQuestions():
    sql = "SELECT * from quiz_question"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("this is",result)
    # result =runSQL(sql)
    for question in result:
        print(question)


def getOptionForQuestions(id):
    sql = "SELECT * from quiz_question_option "
    finalsql = sql + "where quiz_question_id = " + str(id)
    cursor = connection.cursor()
    cursor.execute(finalsql)
    result = cursor.fetchall()
    # print("this is", result)
    # result =runSQL(sql)
    for question in result:
        print(f"{question[0]} {question[1]}")
        # print(question)
    return result

def inCityGui():
    print("What do you want to do \n"
          "1. go meet the boss \n"
          "2. Go farm\n"
          "3. Go play quiz\n"
          "4. Do nothing\n")
    option = input("What do you want to do? (1-4) ")
    return int(option)
def chooseOptionInCity(number):
    if number == 1:
        print("meet boss")
    if number == 2:
        print("go farm")
    if number == 3:
        print("let's find some treasure")
    if number == 4:
        print("do nothing")

# update player
# set resStat = 2
# where id = 3;
# select * from player;
def updatePlayerStat(playerTuple):
    id = playerTuple[0]
    print(id)
    newStat = playerTuple[2]
    print(newStat)
    sql = " UPDATE player"
    finalsql = f"{sql} SET resStat = {newStat} where id = {id}"
    cursor = connection.cursor()
    cursor.execute(finalsql)
    result = cursor.fetchall()
    print("this is", result)

def playerToTuple(player):
    playerTuple = tuple(player)
    print(playerTuple)
    return playerTuple

def generateRandomRobotID():
    return random.randint(player[3],)

def goFarm():
    # generate random robot
    print(f"go farming: {player}")

def answerFromUser(question_id):
    sql = "select id, text from quiz_question_option where quiz_question_id = " + str(question_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result #result user answer as a

def userAnser(options):
    option_id = int(input("Type your answer(1-4)"))
    # options = getOptionForQuestions(question_id)
    user_option = options[option_id - 1]
    return user_option

def checking(userAnswer): ## return true or false for the user answer
    # options = getOptionForQuestions(question_id)
    # userAnswer = userAnser(question_id)
    # print(userAnswer)
    answerIsCorrect = userAnswer[3]## check if option is correct
    if answerIsCorrect == 1 :
        print(" You are correct!")
        return True
    else:
        print(" You are not correct")
        return False

def question(question_id):
    sql = "SELECT id, text FROM quiz_question WHERE id =" + str(question_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f'Question is: {row[1]}')

def insertUserOption(userOption):
    userOptionToTuple = tuple(userOption)
    userOptionColumn = "player_ID,quiz_question_ID,quiz_answer_option_ID,is_correct"
    sql = f"INSERT INTO quiz_user_answer({userOptionColumn}) Value {userOptionToTuple}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result #result user answer as a




# userId = 1
# questionId = 1
# question(questionId)
# options = getOptionForQuestions(questionId)
# # print(options)
# userAnswer = userAnser(options)
# userAnswer_Id = userAnswer[0]
#
# isCorrect = checking(userAnswer) ## have it
# userOption = [userId,questionId,userAnswer_Id,isCorrect] # Record of User Answer
# print(userOption)
# insertUserOption(userOption)


# user_answer = [1]
    #return a list of option with quiz_question_id = 1
# def InserUserAnswer(user_id,quiz_question_id,quiz_answer_option_id,isCorrect):
#     userAnswer = [user_id,quiz_question_id,quiz_answer_option_id,isCorrect]
#     userListToTupple = tuple(userAnswer)
#     sql = f"INSERT INTO quiz_user_answer Value {userListToTupple}"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     return result
#         # assign the id from user to fetch the
#             print('your answer is correct')
#             cursor.execute("SELECT MAX(id) FROM quiz_user_answer")
#             max_id = cursor.fetchall()
#             new_id = max_id[0][0] + 1
#             userAnswer = [userid,quizid,userAnswerid,isCorrect]
#             userAnswerTuple = tuple(userAnswer)
#             print(f'')
#             sql_update = f"INSERT INTO quiz_user_answer VALUES {userAnswerTuple}"
#
#             data = (new_id, question_id, player_answer)
#             cursor.execute(sql_update, data)
#
#         else:
#             print('your answer is incorrect')

# getTables()
# player_info = []
# getPlayers()
# print(getPlayerByName("Trung"))
# loadingPlayerByID(3)
# player =loadingPlayerByID(3)
# goFarm()

# print(f"old player${player}")
# player[2] = 5
# print(f"new player ${player}")
# newPlayerTuble = playerToTuple(player)
# # print(newPlayerTuble)
# # print(newPlayerTuble[0])
# updatePlayerStat(newPlayerTuble)
print(getPlayerByID(3))
# getRobots()
# getRobotById(1)
# getMatches()
# getQuestions()
# getOptionForQuestions(1)
# answer = int(input("user answer"))
# user_answer = getOptionForQuestions(1)[answer-1]
# print(user_answer)
# isCorrect = False
# if user_answer[3] == 1:
#     isCorrect = True
#
# userAnswer
# chooseOptionInCity(inCityGui())
# getRobotsInCity("Helsinki")