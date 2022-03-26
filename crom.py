import numbers
import os
from colorama import init, Fore, Back, Style
import re

os.system('clear')

bashrcc = ('/root/.bashrc')

init()

def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    print ('-----------------------------------------------------------------------------------------------------------------------------')
    print("      *******    *********    ************    **                ")
    print("    ***          **     **    ************    ****************  ")
    print("    ***          **           **        **    ****************  ")
    print("    ***          **           **        **    **     **     **  ")
    print("    ***          **           **        **    **     **     **  ")
    print("    ***          **           ************    **     **     **  ")
    print("      *******    **           ************    **     **     **  ")
    print ('-----------------------------------------------------------------------------------------------------------------------------')
    print ('|v0.0.1|   |nn - new comand|  |dm - reset the number|  |q - quit|  |c - clear|  |m - my command|  |u - backup|')
    print ('-----------------------------------------------------------------------------------------------------------------------------')
    print ('|vu - view backup|')
    print ('-----------------------------------------------------------------------------------------------------------------------------')
    
console_picture()

def mainn():
     cc = input('|Command| ')

     if(cc == 'nn'):
         main()

     if( cc == 'm'):
         m()

     if(cc == 'u'):
         u()

     if(cc == 'vu'):
         vu()

     if(cc == 'dm'):
         
         n = open('number.txt', 'r+')
         n.seek(0)
         n.write('0')
         n.close()
         os.system('clear')
         print ('-----------------------------------------------------------------------------------------------------------------------------')
         print (0)
         print ('-----------------------------------------------------------------------------------------------------------------------------')
         console_picture()
         mainn()

     if(cc == 'q'):
         os.system('clear')
         quit()

     if(cc == 'c'):
         os.system('clear')
         console_picture()
         mainn()

     else:
        print ('--No command!')
        mainn()

def main():

    os.system('clear')
    print ('-----------------------------------------------------------------------------------------------------------------------------')
    print ('New command')
    print ('-----------------------------------------------------------------------------------------------------------------------------')
    console_picture()


    global nameCommand
    global functionCommand
    global number

    nameCommand = input('|Name command|')

    functionCommand = input('|Function|')

    print(f'|Command {nameCommand}; functon {functionCommand}; [y/n]?|')
    yesOrNo = input('| ')

    if(yesOrNo == 'y'):

        n = open('number.txt', 'r+')
        num = n.read()
        number = int(num) + 1
        n.seek(0)
        n.write(str(number))
        n.close()
        

        y()

    else:
        os.system('clear')
        print ('-----------------------------------------------------------------------------------------------------------------------------')
        print (f'Main')
        print ('-----------------------------------------------------------------------------------------------------------------------------')
        console_picture()
        mainn()


def y():
    print('|COMPILE...')

    global comment
    global command
    global bashrc


    cv = open('command.txt', 'a')
    cv.write(f"{nameCommand}\n")
    cv.close()

    comment = ('#CROM COMMAND')
    command = (f'alias {nameCommand}="{functionCommand}" ')
    
    bashrc = ('/root/.bashrc')
    #bashrc = ('my.txt')

    file = open(f'{bashrc}', 'a')


    file.write(f"\n\n{comment}{number} \n")
    file.write(command+"\n")
    file.write(f"{comment}{number} \n")

    os.system(f'source ~/.bashrc')

    file.close()


    print('|END!')
    os.system('clear')
    print ('-----------------------------------------------------------------------------------------------------------------------------')
    print (f'OK {number}')
    print ('-----------------------------------------------------------------------------------------------------------------------------')
    console_picture()
    mainn()


def m():
    cv = open('command.txt', 'r+')
    
    os.system('clear')
    
    print ('-----------------------------------------------------------COMMAND-----------------------------------------------------------')
    print(cv.read())
    console_picture()
    mainn()

def u():
    print('BACKUP')
    rooot = open(f'{bashrcc}', 'r')
    r = rooot.read()
    backup = open('backup.txt', 'w')
    backup.write(r)
    rooot.close()
    backup.close()
    mainn()

def vu():
    os.system('clear')
    vu = open('backup.txt', 'r')
    vuu = vu.read()
    print('\n-----------------BACKUP----------------\n')
    print(vuu)
    print('\n-----------------BACKUP----------------\n')
    console_picture()
    mainn()


mainn()