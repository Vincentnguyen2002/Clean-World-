#  def quiz_question_option(quiz_question_id):
#      #1 get random id
#
#     get question based on that id
#
#     show answer with that id
#
#     let user choose option
#
#     # evaluate answer
#     # sql="select * from quiz_question_option where quiz_questionid;"
#     # moreSql = "where quiz_question_id =" +questionId
#     sql="select * from quiz_question_option;"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
#     if cursor.rowcount > 0:
#         for index,row in enumerate(result,start=1) :
#             print(index,")",f"{row[1]}")
#         player = int(input("what is the answer of this question (choose the number): "))
#     answer = result[player-1]
#     print(answer)
#     isCorrect = answer[3]
#     print(type(isCorrect))
#     if isCorrect == 1:
#         print(" your answer is correct")
#     else:
#         print("your answer is not correct")
#     # if player==row[0]:
#     #     print("correct")
#     # else:
#     #     print("incorrect")
#         return
# quiz_question_option()
location_id = 1
location_id += 1
player=1
sql="update player"
sql=sql + " set location='"+str(location_id)+"'"
sql=sql + " where id='"+str(player)+"'"
print(sql)