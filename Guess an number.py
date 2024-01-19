#Ver 1.0.1

import math
import random

command_list = [0,"show answer",1,"restart",2,"set answer",3,"change range"]

def show_answer():
    print(f"The answer is {answer}")

def setup():
    global answer
    global player_guess
    global enter_press
    global in_command
    global command
    global range
    command = int(11)
    answer = int(random.randint(1, range))
    player_guess = int(0)
    in_command = str("flase")
    print(f"Game restart")
    game_on()

def check_number(player_guess):
    if player_guess != answer:
        check_gap()
    elif player_guess == answer:
        print(f"You got it!!!")

def game_on():
    global player_guess
    global in_command
    global range
    while player_guess != answer or in_command == "flase" :
        player_guess = int(input(f"Guess a number(1 to {range})"))
        check_number(player_guess)

def check_command():
    global command
    global answer
    global range
    global in_command
    if command == 0:
        show_answer()
    elif command == 1:
        setup()
    elif command == 2:
        answer = int(input("Set answer"))
    elif command == 3:
        range = int(input("Set range?"))
        setup()
    in_command = str("flase")

def command_mode():
    global in_command
    global command
    in_command = str("ture")
    print("Choose a command:")
    print(command_list)
    command = int(input())
    check_command()

def check_gap():
    global range
    global player_guess
    global answer
    if player_guess == 11111:
        command_mode()
    elif abs(player_guess) == 00000:
        show_answer()
    elif abs(answer-player_guess) <=5:
        print(f"Almost there!!!(<5)")
    elif abs(answer-player_guess) <=25:
        print(f"You are a lot close to the answer, keep going!(<25)")
    elif abs(answer-player_guess) <=49 >25:
        print(f"A little bit closer, gogogo!(<50 >25)")
    elif abs(answer-player_guess) >100:
        print(f"Hmm...(>100)")
    elif abs(answer-player_guess) >49 <=100:
        print(f"It's so far, keep going~(>=50 <100)")


#main code

range = int(100)
setup()