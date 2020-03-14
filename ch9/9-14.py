from random import choice
lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']
winners = ('3', '4', 'b', 'a')

temp = []
for i in range(0, 4):
    x = choice(lottery)
    temp.append(x)

lose = 0
for i in range(0, 4):
    if (temp[i] != winners[i]):
        lose = 1
        break

print("Winner:")
print(winners)
print("Yours:")
print(temp)
if (not lose):
    print("You win!")
else:
    print("Try it again!")


