from pystyle import *

print(Box.Lines('[+] Multiplication table [+]'))
Write.Print('this app for doing Multiplication table of any Number ', Colors.blue_to_purple,interval=0.1)
print('\n')


while True:
    number = int(Write.Input('[+] inter your number : ' , Colors.blue_to_purple, interval = 0.1))

    for i in range(1,11):
        print(number ,'X' , i , '=', number * i )

      
