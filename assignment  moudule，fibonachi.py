nterms = int(input("where do you want to start？"))
n1 = 0
n2 = 1
count = 2
if nterms <= 0:
    print("pls input a integer")
elif nterms == 1:
    print(n1)
else:
    print(n1, ",", n2, end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=" , ")
        n1 = n2
        n2 = nth
        count += 1
#exercise 1 part1

import random
import string
def random_user_id():
    return ''.join(random.sample(string.ascii_letters + string.digits, 6))
print(random_user_id())
#exercise 1 part2
a=int(input("pls enter how many ID u want"))
b=int(input("pls enter how many letters u want in a single ID"))
def user_id_gen_by_user():
    c=[random.sample(string.ascii_letters + string.digits, b) for i in range(a)]
    for l in c:
        print(''.join(l))
user_id_gen_by_user()
#exercise 1 part3
def rgb_color_gen():
    return [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
print(rgb_color_gen())
#exercise 2 part 1
def list_of_hexa_colors():
    letter=["1","2","3","4","5","6","7","8","9","0","a",'b','c','d','e','f']
    hex="#"+"".join(random.sample(letter,6))
    return hex
print(list_of_hexa_colors())
#exercise 2 part 2
def list_of_rgb_colors():
    return(random.randint(0,255),random.randint(0,255),random.randint(0,255))
print(list_of_rgb_colors())
#exercise 2 part 3

def generate_colors(input,times):
    list=[]
    if input == 'hexa':
        while times != 0:
            list.append(list_of_hexa_colors())
            times-=1
        return list
    elif input =='rgb':
        while times != 0:
            list.append(list_of_rgb_colors())
            times -= 1
        return list
    else:
        print("error")
print(generate_colors('hexa',3))
print(generate_colors('hexa',1))
print(generate_colors('rgb',1))
print(generate_colors('rgb',3))


def shuffle_list(seq) :
    return random.shuffle(seq)

def func():
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    return random.sample(num,6)
print(func())







