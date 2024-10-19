from config import connection

import utils.menu as menuUtil
import utils.player as playerUtil
import utils.game as gameUtil
# import utils.quiz as quiz

def main():
    while True:

        player = menuUtil.menu()
        # print("hello from main",player)
        gameUtil.game(player)
        # print(option)



main()

