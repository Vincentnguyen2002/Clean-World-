import random
from config import connection
import utils.player as playerUtil
import utils.robot as robotUtil


def quizQuestionsAtLocation(location_id):
    selectedField = "quiz_question.id, quiz_question.text"
    sql = f"select {selectedField} from city,quiz_question"
    sql = sql + " where quiz_question.location_id=city.id and"
    sql = sql + " location_id='" + str(location_id) + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    return result
# questionList =  quiz_questions(location_id)
# currentQuestionList = quiz_questions(location_id)
def generateRandomQuestion(questionList):
    randomQuestion = random.choice(questionList)
    print(randomQuestion[1])
    return randomQuestion
# ('Which of the following is a (1, 'Helsinki', 1, 0, 4,
# "Finland's Everyman's Right (Jokamiehenoikeus) allows people to:",
# 1) eco-friendly cleaning practice in Finland?',)

def getOptionForQuestions(id):
    sqlField = "id, text, is_correct"
    sql = f"SELECT {sqlField} from quiz_question_option "
    finalsql = sql + "where quiz_question_id = " + str(id)
    cursor = connection.cursor()
    cursor.execute(finalsql)
    result = cursor.fetchall()
    # print("this is", result)
    # result =runSQL(sql)
    # resultList = enumerate(result, start=1)
    for index, question in  enumerate(result,start=1):
        print(f"{index} {question[1]}")

        # print(question)
    return result

def userAnswer(options):
    option_id = int(input("Type your answer(1-4): "))
    # options = getOptionForQuestions(question_id)
    # print(options)
    user_option = options[option_id - 1]
    print("This is your answer: ", user_option[1])
    return user_option

def checking(userAnswer): ## return true or false for the user answer
    answerIsCorrect = userAnswer[2]## check if option is correct
    if answerIsCorrect == 1 :
        print(" You are correct!")
        return True
    else:
        print(" You are not correct")
        return False

def returnCorrectId(checkingResult):
    if checkingResult:
        return 1
    else :
        return 0

# def answer(userAnswer,playerStat):
#     # when player answer right, stat +1, wrong stat -1
#     if checking(userAnswer): #
#         playerStat += 1
#     else:
#         playerStat -= 1
#     return playerStat

def insertUserOptionAnswer(userOption):
    userOptionToTuple = tuple(userOption)
    userOptionColumn = "player_ID,quiz_question_ID,quiz_answer_option_ID,is_correct"
    sql = f"INSERT INTO quiz_user_answer({userOptionColumn}) Value {userOptionToTuple}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result #result user answer as a

def answer(isCorrect,playerStat,bossStat):
    # when player answer right, stat +1, wrong stat -1
    if isCorrect: #
        playerStat += 1
        playerStat = min(playerStat,bossStat)
    else:
        playerStat -= 1
        playerStat = max(1, playerStat)
    # insertUserOption(userOption)
    return playerStat


# create a quiz def and return a new Data Tuple of Player
def quiz(playerData, bossData):
    #[id,name,resStat,location,isInCity,energy,isNew]
    formattedPlayerData = playerUtil.formatPlayerData(playerData)
    # ('Boss1', 2, 5, 1)
    bossStat = bossData[3]
    # [3, 'testPlayer', 5, 1, 1, 3, 0]
    # print(formattedPlayerData)
    userId = formattedPlayerData[0]
    playerUtil.showPlayerInfo(playerData)
    userName = formattedPlayerData[1]

    # print(userId)
    location_id = formattedPlayerData[3]
    # print(location_id)
    playerResStat = formattedPlayerData[2]
    # print(quizQuestionsAtLocation(1))
    questionList = quizQuestionsAtLocation(location_id)  # get question list from location id
    # print(questionList)
    questionId = generateRandomQuestion(questionList)[0]  # get questionID
    # # # print(generateRandomQuestion())
    options = getOptionForQuestions(questionId)  # get options from question ID

    userOptionAnswer = userAnswer(options)  # user choose answer
    # print(userOptionAnswer)
    userOptionAnswerId = userOptionAnswer[0]
    # print(userOptionAnswerId)
    userAnswerOptionId = userOptionAnswer[0]

    isCorrect = checking(userOptionAnswer)  ## have it
    isCorrectId = returnCorrectId(isCorrect)

    newPlayerResStat = answer(isCorrect,playerResStat,bossStat)

    # return new ResStat
    formattedPlayerData[2] = newPlayerResStat # asign

    userOptionAnswerData = [userId,questionId,userOptionAnswerId,isCorrectId]

    playerDataTuple = playerUtil.playerToTuple(formattedPlayerData)
    insertUserOptionAnswer(userOptionAnswerData) # insert to database
    playerUtil.updateStat(playerDataTuple,newPlayerResStat)# insert to database user answer

    return formattedPlayerData

# userName = "Huy"
# player = playerUtil.getPlayerByName(userName)
# # # print(player)
# currentLocationId = playerUtil.getCurrentPlayerLocationId(player)
# # print(currentLocationId)
# boss = robotUtil.get_current_boss_data(currentLocationId)
# # # print(player)
# # # print(boss)
# #
# print(quiz(player,boss))