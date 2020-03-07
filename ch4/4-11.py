pizzas = ['a', 'b', 'c', 'd']
for pizza in pizzas:
    print(f"I like {pizza} pizza")

friend_pizzas = pizzas[:]
friend_pizzas.append('E')
print("\nI really love pizza!")

print("My favorite pizzas are:")
for p in pizzas:
    print(p)

print("My friend's favorite pizzas are:")
for p in friend_pizzas:
    print(p)

