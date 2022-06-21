import random
num = random.randrange(100)
print(num)
print('Welcome to Random Number Generator', end='')
input()
print("DON'T BELIEVE IN APPROXIMATE VALUES. THEY ARE FOOLING YOU!", end='')
input()


for tr in range(1, 5):
    if tr == 4:
        print('No of tries exceeded')
        break
    user = int(input('Enter number : '))
    num1 = random.randrange(10)
    if num != user:

        if num > user:
            cal = abs(num-user+num1)
            print('Your number is smaller by almost', cal)
            tr += 1
        elif num < user:
            cal = abs(num - user - num1)
            print('Your number is greater by almost', cal)
            tr += 1
    else:
        print('Both the numbers are same')
        break


print('The random number was', num)
if tr < 4:
    print('You guessed it in', tr, 'tries')

if tr == 1:
    print('WOW! Are you a psychic?')
if tr == 2:
    print('Well Done!')
if tr == 3:
    print('Phew! That was a close call.')
