import sys
sys.path.insert(0, './chat_bot')

from bot import Calm_Bot
import numpy as np

# # command methods
# def exit():
#     pass

# COMMANDS = {
#         	"exit": lambda x: x.exit(),
#             "restart": lambda x: x.restart()
# }


def run():
    bot = Calm_Bot('chat_bot\weights\model_state_V4_6.pt')

    loop = 0
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["q", "quit", "e", "exit", "x"]:
            print("See you later! I hope you had fun ^^")
            break
        elif user_input in ["restart", "new"]:
            loop = 0
            bot.reload()
        else:
            print("Bot:", bot.inference(user_input, True))
        loop += 1

if __name__ == '__main__':
    run()