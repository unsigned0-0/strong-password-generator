from ntpath import join
import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

num_of_int = input('how many digits do want: ')


while True:
    try:
        num_of_int = int(num_of_int)
        if num_of_int < 10:
            print('at least 10 digits  ')
        else:
            break
    except:
        print('please type int only  ')
        num_of_int = input('how many characters for the pass word: ')
       
        
        
random.shuffle(s1)        
random.shuffle(s2)    
random.shuffle(s3)        
random.shuffle(s4)        

p1 = round(num_of_int * (30/100))
p2 = round(num_of_int * (20/100))


password = []            

for i in range(p1):
    password.append(s1[i])
    password.append(s3[i])         
   
for i in range(p1):
    password.append(s4[i])      
    password.append(s2[i])  
###############################

password = ''.join(password[0:])
input('there you go !' + password + 'have fun with your password' )

print(password)    

    