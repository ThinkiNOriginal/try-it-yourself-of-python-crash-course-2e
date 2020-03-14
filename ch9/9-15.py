from random import choice
lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']
winners = ['3', '4', 'b', 'a']


temp = []
cnt = 0
while (winners != temp):
    cnt += 1
    temp = []
    for i in range(0, 4):
        x = choice(lottery)
        temp.append(x)


print(f"1 in {cnt}")
