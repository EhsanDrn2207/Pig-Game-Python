import random


class InvalidNumberInputException(Exception): # an exeption for entering number of participants
    pass


class InvalidInputException(Exception): # and exception for yes or no question in the game
    pass


def roll_dices():
    """ give us a random number of 2 diecs.

    Returns:
        _tuple_: the numbers of dices
    """
    min_number = 1
    max_number = 6
    roll_num1 = random.randint(min_number, max_number)
    roll_num2 = random.randint(min_number, max_number)
    return roll_num1, roll_num2


def player_number():
    """ user enter the number of participants
    Raises:
        InvalidNumberInputException: The number of players must be between 2 - 4, otherwise this exception will be raised
        ValueError: user input must be a number, otherwise this exception will be raised

    Returns:
        _int_: number of players
    """
    while True:
        player_num = input("Enter the number of players (2 - 4): ")
        try:
            if player_num.isdigit():
                player_num = int(player_num)
                if 2<= player_num <= 4:
                    return player_num
                else:
                    raise InvalidNumberInputException
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, try again.")
        except InvalidNumberInputException:
            print("Invalid number, must be between 2 - 4, try again.")
            
            
def pig_game(players:int) -> list:
    """This game looks like a gambling. if your dices show (1) your cerrent score will become zero.
    if your dieces show (1,1) your total number will become zero.
    maximan score is 100.
    
    Args:
        players (int): The number of players

    Raises:
        InvalidInputException: Your input must be yes or no, otherwise this excepxtion will be raised

    Returns:
        list: players score
    """
    max_score = 100
    global players_score
    players_score = [0 for _ in range(players)]
     
    while max(players_score) < max_score:
        for player_idx in range(players):
            print(f"\nPlayer number {player_idx+1} turn just started!\n")
            current_number = 0
            while True:
                should_roll = input("Would like to roll the dices (y/n): ")
                try:
                    if should_roll.lower() not in['y', 'n']:
                        raise InvalidInputException
                    else:
                        if should_roll.lower() != "y":
                            break
                        else:
                            value  = roll_dices()
                            if value.count(1) == 1:
                                print("You rolled: ", value)
                                current_number = 0
                                break
                            elif value.count(1) == 2:
                                print("You rolled: ", value)
                                current_number = 0
                                players_score[player_idx] = 0
                                break
                            else:
                                print("You rolled: ", value)
                                current_number += sum(value)
                                print("You score is: ", current_number)
                      
                except InvalidInputException:
                    print("Invalid input, must be y or n, try again.")
            players_score[player_idx] += current_number
            print("Your total score is: ",  players_score[player_idx])
            print("-" * 30)
        
    return players_score

players = player_number()
scores = pig_game(players=players)
winner = max(scores)
print(f"The winner is player {players_score.index(winner) + 1} with the score of: {winner}")

with open("file1.txt", "a") as f:
    f.write(f"\nThe winner is player {players_score.index(winner) + 1} with the score of: {winner}\n")
    f.write("---------------------------------------------------\n")
    