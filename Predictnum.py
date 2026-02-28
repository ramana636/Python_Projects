def main():
    while True:
        import random
        digits = random.sample("123456789",4)
        num = int("".join(digits))
        print('Enter 1 to enjoy the game')
        print('Enter 2 to quit the game')
        print('Enter 3 to know the rules of the game')
        print('\n')
        play=input('Enter the command:  ')
        if play == '1':
            game1(num)
        elif play == '3':
            print('1.you have to predict a four digit number without any repitition')
            print('2.It will display how many digits are present in entered number and also how many are in correct position')
            print('\n')
        else:
            print('Thanks for playing dude ,hope the game was fun')
            break
def game1(num):
    ram=num
    tom=[]
    jerry=[]
    exp=1
    score=0
    while ram != 0 :
        tom.append(ram % 10)
        jerry.append((ram % 10)*exp)
        exp*=10
        ram=ram//10
    while True :
        score+=1
        user=int(input('Enter the number 4 digit number without any repitition: '))
        m=int(user)
        u=[]
        while m !=0:
            if m % 10 not in u:
                u.append(m%10)
            m=m//10
        if len(u) == 4:
         if user == num :
              print(f'Hurray!!! The guessed the number in {score}th attempt')
              break
         else:
            count=0
            coun=0
            exp=1
            while user != 0:
                if user %10 in tom :
                    count +=1
                if (user %10)*exp in jerry:
                    coun +=1
                user=user//10
                exp*=10
            print(f'the number of correct digits present in your number is {count} and {coun} are in correct position')
        else:
            print("Enter a valid 4 digit number without repitition")
main()
                    
             
        
    
    
        

        

        
        
    
