def printHello():
    print("Hello World")

def is_vowel(letter):
    if type(letter) == int:
        letter = str(letter)
    if letter in "aeiouy":
        return(True)
    else:
        return(False)

print(is_vowel(4))


def factorial(n):
    if n == 0:
        return 1
    else:
        N = 1
        for i in range(1, n+1):
            N *= i
    return(N)

print(factorial(5))


import string

alphabet = string.ascii_letters
print(alphabet)

sentence = 'Jim quickly realized that the beautiful gowns are expensive'


def countLetters(sentence):
    count_letters = {}
    for i in sentence:
        if i in count_letters:
            count_letters[i] += 1
        else:
            count_letters[i] = 1
    return count_letters

address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""
# print(sorted(countLetters(address)))
# print("\n",countLetters(address))

import math
print(math.pi / 4)

# ### 
import random

random.seed(1) # Fixes the seed of the random number generator.
list = []
def rand():
   return random.uniform(-1,1)

print(rand())

def in_circle(x, origin = [0,0]):
    # Define your function here!
    result = math.pow((abs(x[0] - origin[0]) + abs(x[1] - origin[1])), 2)
    if result < 1:
        return True
    else :
        return False
print(in_circle((1,1)))
for i in range(10000):
    x = rand()
    y = rand()
    list.append((x,y))
boolList = []
for i in list:
    if in_circle((i)):
        boolList.append(True)
    else:
        boolList.append(False)
print(boolList.count(True))
print(boolList.count(False))
print(len(boolList))
print(boolList.count(True) / len(boolList))

