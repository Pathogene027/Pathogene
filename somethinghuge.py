import random
import time
import math

# title

print('*******************\n*******************')
print('* *             * *')
print('* *    Rock     * *')
print('* *    paper    * *')
print('* *    Scissor  * *')
print('* *             * *')
print('*******************\n*******************')


# main
def forrandom():
    global randomize
    randomize = random.choice(lst)
    print(randomize)


def oneplayer():
    print(f"Scores Player1 {Player1_score}\nScores Player CPU {cpu_score}")


def oneplayerfinalds():
    print(f"Scores Player1 {sum(Player1_score)}\nScores Player CPU {sum(cpu_score)}")

def twoplayers():
    print(f"Scores Player1 {Player1_score} \nScores Player2 {Player2_score}")

def twoplayersfinalds():
    print(f"Scores Player1 {sum(Player1_score)} \nScores Player2 {sum(Player2_score)}")

def threeplayers():
    print(
        f"Scores Player1{Player1_score} \nScores Player2 {Player2_score}\nScores Player3 {Player3_score}")

def threeplayersfinalds():
    print(
        f"Scores Player1 {sum(Player1_score)} \nScores Player2 {sum(Player2_score)}\n"
        f"Scores Player3 {sum(Player3_score)}")

check3 = True
while check3:
    check1 = True

    while check1:
        print('Only a maximum of three players are allowed in this game. A single player plays with cpu')
        print('1. Single Player\n2. Double Players\n3. Triple players')
        print("Let's Start")
        player_select = input('How many players will be playing ths game?: ')
        Player1_score = []  # keep scores of player
        Player2_score = []
        Player3_score = []
        cpu_score = []  # keep scores of cpu
        check2 = True

        while check2:
            lst = ['Rock', 'Paper', 'Scissors']  # holding the random three words
            # single player
            if player_select == '1' or player_select.lower() == 'single player':
                # create a random choice out of the list

                for i in lst:
                    print(i)  # display rock paper scissors
                    time.sleep(1)
                forrandom()
                # demanding for a guess
                print('Make your guess player1')
                guess = input('guess rock, paper or scissors: ')

                if guess.lower() == randomize.lower():  # what should happen if guess is right
                    Player1_score.append(1)  # add 1 to the single_score list
                    cpu_score.append(0)
                    oneplayer()

                elif guess.lower() != randomize.lower():
                    Player1_score.append(0)
                    cpu_score.append(1)
                    oneplayer()

                print("Press 'Enter to continue'\n1. Change number of players(p)\n2. Exit(e) ")
                question = input('Enter your choice: ')

                # options to continue, change number of players or quit
                if question == '':
                    continue
                elif question.lower() in ['change number of players', 'p'] or question == '1':
                    print(f"Total scores\n ")
                    oneplayerfinalds()
                    print('Lets start all over')
                    check2 = False
                    check3 = False
                # how do i get out of this to the initial while loop?
                elif question.lower() in ['exit', 'e'] or question == '2':
                    print(f"Total scores\n")
                    oneplayerfinalds()
                    check1 = False
                    check2 = False
                    check3 = False

                else:
                    print('choose an option')
            # double player
            elif player_select.lower() == 'double players' or player_select == '2':

                for i in lst:
                    print(i)  # display rock paper scissors
                    time.sleep(1)
                forrandom()
                print('Make your guess player1')
                guess = input('guess rock, paper or scissors: ')  # demanding for a guess
                if guess.lower() == randomize.lower():
                    Player1_score.append(1)  # add 1 to the single_score list
                    twoplayers()

                elif guess.lower() != randomize.lower():
                    Player1_score.append(0)
                    twoplayers()

                for t in lst:
                    print(t)  # display rock paper scissors
                    time.sleep(1)
                forrandom()
                print('Make your guess player2')
                guess = input('guess rock, paper or scissors: ')  # demanding for a guess
                if guess.lower() == randomize.lower():
                    Player2_score.append(1)  # add 1 to the single_score list
                    twoplayers()
                elif guess.lower() != randomize.lower():
                    Player2_score.append(0)
                    twoplayers()

                print("Press 'Enter to continue'\n1. Change number of players(p)\n2. Exit(e) ")
                question = input('Enter your choice: ')
                # options to continue, change number of players or quit
                if question == '':
                    continue
                elif question.lower() in ['change number of players', 'p'] or question == '1':
                    print(f"Total scores\n")
                    twoplayersfinalds()
                    print('Lets start all over')
                    check2 = False
                    check3 = False
                # how do i get out of this to the initial while loop?
                elif question.lower() in ['exit', 'e'] or question == '2':
                    print("Total scores")
                    twoplayersfinalds()
                    check1 = False
                    check2 = False
                    check3 = False

                    # triple players
            elif player_select.lower() == 'triple' or player_select == '3':
                for i in lst:
                    print(i)  # display rock paper scissors
                    time.sleep(1)
                forrandom()
                print('Make your guess player1')
                guess = input('guess rock, paper or scissors: ')  # demanding for a guess
                if guess.lower() == randomize.lower():
                    Player1_score.append(1)  # add 1 to the single_score list
                    threeplayers()
                elif guess.lower() != randomize.lower():
                    Player1_score.append(0)
                    threeplayers()

                for t in lst:
                    print(t)  # display rock paper scissors
                    time.sleep(1)
                forrandom()
                print('Make your guess player2')
                guess = input('guess rock, paper or scissors: ')  # demanding for a guess
                if guess.lower() == randomize.lower():
                    Player2_score.append(1)  # add 1 to the single_score list
                    threeplayers()
                elif guess.lower() != randomize.lower():
                    Player1_score.append(0)
                    print(
                        f"Scores Player1{Player1_score} \nScores Player2 {Player2_score}\n"
                        f"Scores Player3{Player3_score}")

                for t in lst:
                    print(t)  # display rock paper scissors
                    time.sleep(1)
                forrandom()
                print('Make your guess player3')
                guess = input('guess rock, paper or scissors: ')

                if guess.lower() == randomize.lower():
                    Player3_score.append(1)  # add 1 to the single_score list
                    threeplayers()
                elif guess.lower() != randomize.lower():
                    Player3_score.append(0)
                    threeplayers()

                # options to continue, change number of players or quit
                print("Press 'Enter to continue'\n1. Change number of players(p)\n2. Exit(e) ")
                question = input('Enter your choice: ')
                if question == '':
                    continue
                elif question.lower() in ['change number of players', 'p'] or question == '1':
                    print(f'Player1:')
                    threeplayersfinal()
                    print('Lets start all over')
                    check2 = False
                    check3 = False
                # how do i get out of this to the initial while loop?
                elif question.lower() in ['exit', 'e'] or question == '2':
                    print(f'Player1:')
                    threeplayersfinalds()

                    check1 = False
                    check2 = False
                    check3 = False