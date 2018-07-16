import random as rand
count = 0
try:
    num1 = int(input('Enter a no between 1-10: '))
    num2 = rand.randint(1,10)
    count += 1

    while num1 != num2:
        count += 1
        #print('number is :',num2,',you have entered:',num1)  
        if num1 < num2:
            print('sorry,Guess is Low,Try again')
            num1 = int(input('Enter a no between 1-10: '))
             
        elif num1 > num2:
            print('sorry,Guess is High,Try again')
            num1 = int(input('Enter a no between 1-10: ')) 
                   
        else:
            print('Congrats,You guessed it right')
            count +=1 
            break 

except:
    print('Please enter an interger number')    

print('No is' , num2, 'You have guessed it right in' , count, 'counts.')



