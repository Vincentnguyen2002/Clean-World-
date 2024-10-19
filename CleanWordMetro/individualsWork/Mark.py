import mysql.connector




player = []
boss = []

def question():
    sql = "SELECT id, text FROM quiz_question order by rand() limit 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #print(result)
    for row in result:
        print(f'Question is: {row[1]}')
        question_id = row[0]
        return question_id


def quiz_question_option(question_id):
    sql = "select id, text from quiz_question_option where quiz_question_id = " + str(question_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1):
            print(f"{index}) {row[1]}")
        return

def user_answer(question_id):
    answer = int(input('Your answer: '))
    actual_answer = answer - 1
    return actual_answer

def user_answer_checking(question_id, answer):
    sql = "select id, is_correct from quiz_question_option where quiz_question_id = " + str(question_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    options = []
    for row in result:
        answer_id = f'{row[1]}'
        answer_id_int = int(answer_id)
        options.append(answer_id_int)
    print(options)
    correct_answer = options.index(1)
    if correct_answer == answer:
        print('You are correct')
    else:
        print('Wrong')




def get_random_robot():
    sql = "SELECT id FROM robot order by rand() limit 1;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row[0])
        #return row[0]

def get_current_player_data(player_id):
    sql = "SELECT name,resStat, location,isInCity,energy, isNew FROM player where id=" + str(player_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #print(result)
    for row in result:
        player_stats =print(f'Name: {row[0]}\nStat: {row[1]}\nLocation: {row[2]}\nEnergy: {row[4]}')
        return player_stats


def get_current_boss_data(bot_id):
    sql = "SELECT name, type, pollustat,location FROM robot where id=" + str(bot_id)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    for row in result:
        boss_stats = print(f'Name: {row[0]}\nType: {row[1]}\nPollution Stats: {row[2]}\nLocation: {row[3]}')
        return boss_stats





#player_id = int(input('Player id: '))
#bot_id = int(input('bot id: '))
question_id = question()
quiz_question_option(question_id)
answer=user_answer(question_id)
user_answer_checking(question_id,answer)
#get_random_robot()
#get_current_player_data(player_id)
#get_current_boss_data(bot_id)