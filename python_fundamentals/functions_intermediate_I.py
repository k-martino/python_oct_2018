# As part of this assignment, please create a function randInt() where

# randInt() returns a random integer between 0 to 100
# randInt(max=50) returns a random integer between 0 to 50
# randInt(min=50) returns a random integer between 50 to 100
# randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().



# helpful tips for the next assignment
import random
# print(random.random()) # returns a random floating number between 0.000 to 1.000
# print(random.random()*50) # returns a float between 0.000 to 50.000
# int( 3.654 ) # returns 3
# round( 3.654 ) # returns 4

def randInt(min='', max=''):
    print(int(random.random()*100))

randInt()
# randInt(max=50)
# randInt(min=50)
# randInt(min=50, max=500)