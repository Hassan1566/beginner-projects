"""
Implementation of rock, paper, scissors by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    if user not in ('r', 'p', 's'):
        print("Invalid choice. Please enter 'r', 'p' or 's'.")
        return play_again()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("It's a tie")
        return play_again()

    # r > s, s > p, p > r
    if is_win(user, computer):
        print('You won!')
        return play_again()

    print('You lost!')
    return play_again()

def play_again():
    choose = input("Do you want to play again? (y/n)\n").lower()
    if choose == 'y':
        return play()
    elif choose == 'n':
        return 'Thanks for playing!'
    else:
        print("Please enter 'y' or 'n'.")
        return play_again()

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
