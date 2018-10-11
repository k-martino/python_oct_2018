# Assignment: Functions Intermediate II
# Objectives:
# Practice writing functions and looping over dictionaries
# Better understand how to traverse through an array of dictionaries or through a dictionary of arrays.

# 1. Given:

x = [[5, 2, 3], [10, 8, 9]]

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]

sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}

z = [{"x": 10, "y": 20}]

# a) How would you change the value 10 in x to 15?  Once you're done, x should be:

x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)

# b) How would you change the last_name of the first student from 'Jordan' to "Bryant"?

students[0]["last_name"] = "Bryant"
print(students)

# c) For the sports_directory, how would you change 'Messi' to 'Andres'?

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

# d) For z, how would you change the value 20 to 30?
z[0]["y"] = 30
print(z)


# 2. Create a function that given a list of dictionaries, it loops through each dictionary
# in the list and prints each key and the associated value.  For example, given the following list:

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]


def iterateDictionary(dictList):
    for i in range(len(dictList)):
        string = ""
        for j, k in dictList[i].items():
            string += j + " - " + k + ", "
        print(string)


iterateDictionary(students)

# # should output:
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel


# # 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that
# #  key for each dictionary.  For example, iterateDictionary2('first_name', students) should output:

# # Michael
# # John
# # Mark
# # KB


def iterateDictionary2(dictList, key):
    for i in range(len(dictList)):
        print(dictList[i][key])


iterateDictionary2(students, "first_name")


# 4.  Say that:

dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"],
}

# Create a function that prints the name of each location and also how many locations the Dojo currently has.
# Have the function also print the name of each instructor and how many instructors the Dojo currently has.
# For example, printDojoInfo(dojo) should output:

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


def printDojoInfo():
    temp = ["locations", "instructors"]
    for x in temp:
        print(len(dojo[x]), x)
        for i in dojo[x]:
            print(i)


printDojoInfo()
