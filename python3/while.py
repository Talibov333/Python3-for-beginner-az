# import random

# randomnumber = random.randint(1, 5)
# guesscount = 0
# guesslimit = 2

# while guesscount < guesslimit:
#     guess = int(input('enter your guess: '))
#     guesscount += 1
#     if guess == randomnumber:
#         print("you won!")
#         break
# else:
#      print('you are failed')       
   
menu = """(1) single
(2) plural 
(3) exit"""  
print(menu)

while True:
    choose = input('choose one option: 1/2/3  ')
    if (choose == "1"):
        count = int(input('enter a number: '))
        numbtype = 1
        for bolen in range(2, count):
            if count % bolen == 0:
                print('your number is plural ')
                numbtype = 0 
                break
        if numbtype == 1:
            print('single')

