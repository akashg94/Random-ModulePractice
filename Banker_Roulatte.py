import random

name = input("give me everybody's name spearated by coma")
names = name.split(" , ")

num_items = len(names)
random.randint = len(names)

random_choice = random.randint(0, num_items - 1)

person_will_pay = names[random_choice]

print((person_will_pay + "is going to buy meal today"))
