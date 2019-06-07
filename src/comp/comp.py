# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []

for human in humans:
    if human.name[0] == "D":
        a.append(human)

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []

for human in humans:
    if human.name[-1] == "e":
        b.append(human)

print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []

for human in humans:
    if human.name[0] == "C":
        c.append(human)
    elif human.name[0] == "D":
        c.append(human)
    elif human.name[0] == "E":
        c.append(human)
    elif human.name[0] == "F":
        c.append(human)
    elif human.name[0] == "G":
        c.append(human)

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []

for human in humans:
    if human.age > 10:
        d.append(human.age)

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []

for human in humans:
    name_with_age = f"{human.name}-{human.age}"
    e.append(name_with_age)

print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []

for human in humans:
    if human.age > 27 and human.age < 32:
        name_age_tuple = (human.name, human.age)
        f.append(name_age_tuple)

print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []

for human in humans:
    new_human = Human(human.name.upper(), human.age + 5)
    g.append(new_human)

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []

for human in humans:
    sqrt_of_age = math.sqrt(human.age)
    h.append(sqrt_of_age)

print(h)
