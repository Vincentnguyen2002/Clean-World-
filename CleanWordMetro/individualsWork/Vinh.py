import mysql.connector
import random
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'clean_world',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)
def quiz_question(location_id):
    sql = "select quiz_question.text from city,quiz_question"
    sql = sql + " where quiz_question.location_id=city.id and"
    sql = sql + " location_id='" + str(location_id) + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    random_quizz = random.choice(result)
    return result

def generateRandomQuestion(questionList):
    randomQuestion = random.choice(questionList)
    return randomQuestion[0]
def quiz_question_id(name):
    sql="select quiz_question.id from quiz_question"
    sql=sql + " where quiz_question.text='"+name+"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for id in result:
            return id[0]
def quiz_question_option(option):
    sql="select quiz_question_option.text from quiz_question_option,quiz_question"
    sql=sql + " where quiz_question_option.quiz_question_id=quiz_question.id and"
    sql=sql + " quiz_question_option.quiz_question_id='"+str(option)+"'"
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    if cursor.rowcount>0:
        for index,opt in enumerate(result,start=1):
            print(index,")",opt[0])
    return result
def comparing(official):
    sql="select is_correct from quiz_question_option"
    sql=sql + " where quiz_question_option.text='"+official+"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount>0:##result = [(1,),(0,)]
        return result[0]
location_id = 1
currentQuestionList = quiz_question(location_id)
question = generateRandomQuestion(currentQuestionList)
print(question)
question_id = quiz_question_id(question) ## lay id tu question
option=question_id
options = quiz_question_option(option) # lay toan bo option thuoc question_id
player=int(input("choose options: "))
 userOption = options[player-1]  #tuple
  onlyStringUserOption = userOption[0]
 official=options
 comparing(official)
x=options[player-1][0]
if comparing(x)[0]==1:
    print("correct")
else:
    print("incorrect")
# def getBossData():
# def getCurrentPlayerData():
# player = getCurrentPlayerData()
# boss = getBossData
# player= [name, stat, location]
# boss = [name,stat, location]
# def isWinBoss (player,boss):
# playerStat = player[x]
# bossStat = boss[x]
# if playerStat > bossStat:
#     return True
# else: return False
#  khi player thang boss >> print ng choi clean thanh pho thanh cong >>> qua tp tiep theo >> update location-id +=1
def getBossdata():
    sql="select * from robot"
    sql=sql+" where robot.id=5"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        return result[0]

def getcurrentplayerdata(player):
    sql="select * from player"
    sql=sql + " where player.name='"+player+"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        return result[0]
def isWinboss(player,boss):
    playerStat=player[2]
    bossStat=boss[3]
    if  playerStat>=bossStat:
        print("Successful in cleaning Helsinki")
        return True
    else:
        return False
def updating(player):
    location_id = player[3]
    sql="update player"
    moresql =sql + " set location="+str(location_id)+""
    finaSql= moresql + " where id="+str(player[0])+""
    cursor = connection.cursor()
    cursor.execute(finaSql)
    result = cursor.fetchall()
    if cursor.rowcount>0:
        return result
player_name="Huy"
player=getcurrentplayerdata(player_name)
updating(player)
boss=getBossdata()
isWinboss(player,boss)

