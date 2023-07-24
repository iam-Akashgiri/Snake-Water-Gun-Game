import random


def reetry():
    _round=1


    while True:
        def check(comp,user):
            if comp==user:
                return 0
            if(comp==1 and user==0) or (comp==2 and user==1) or (comp==0 and user==2):
                return -1
            return 1

        comp=random.randint(0, 2)


        print()
        print()
        print()
        print('                                                 ********WELCOME TO ROUND', _round ,'********')


        print()
        print()
        print()
        print()
        print()
        print()
        print()
        user=int(input('Enter 0 for water💧, 1 for snake🐍, 2 for gun🔫: '))

        print()
        print()
        score=check(comp, user)

        def users():
            if user==0:
                print('You choosen: 💧')
            elif user==1:
                print('You choosen: 🐍')
            elif user==2:
                print('You choosen: 🔫')
            else:
                print('Ooopps 🤯 INVALID SELECTION 🤯 Restarting from Round 1 "SELECT  OPTION"')
                reetry()
                
                
        users()
       
            
        def com():
            if comp==0:
                print('computer choosen: 💧')
            if comp==1:
                print('computer choosen: 🐍')
            if comp==2:
                print('computer choosen: 🔫')
        com()


        print()
        print()



        if score==0:
            print('                          🤯Its a draw🤯')
        elif score==1:
            print('                          😎You Won the match😎')
        else:
            print('                          😩You lose the match😩')

            
        print()
        print()
        print()
        print()
        print()

        
        
        print('👏👏WELL PLAYED...!!')
        
        retry=input('Wanna play again..???? ')
        if retry==('yes' or 'Yes' or 'YES'):
            _round+=1
            
            
        else:
            print('                                  🙏THANKS FOR PLAYING🙏')
            break

reetry()


    



