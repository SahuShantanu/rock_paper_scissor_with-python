print('ROCK ,PAPER AND SCISSOR GAME')
print("lets play the game")
p1 = input('player 1 situation\n')
p2 = input('player 2 situation\n')
if p1 == p2:
    print('tie')
elif p1 == 'rock' and p2 == 'paper':
    print("player 2 win")
elif p1 == 'rock' and p2 == 'scissor':
    print("player 1 win")
elif p1 == 'paper' and p2 == 'scissor':
    print("player 2 win")
elif p1 == 'paper' and p2 == 'rock':
    print("player 1 win")
elif p1 == 'scissor' and p2 == 'paper':
    print("player 1 win")
elif p1 == 'scissor' and p2 == 'rock':
    print("player 2 win")
else:
    print("go to hell")
