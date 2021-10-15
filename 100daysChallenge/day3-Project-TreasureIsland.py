print('''
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
         /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /

''')
#https://ascii.co.uk/art/treasure

print("Welcome to Treasure Island.\n Your mission is to find the treasure!\n")
proceed = input("Do you want to continue? (Y/N) ").lower()

if proceed == 'y':
    print("\nYour plane has crashed and you woke up in a deserted island. You went to the forest to find some food. ")
    a = input("You found two paths. Where do you want to go, left or right?\n").lower()
    if a == 'left':
        b = input("\nYou found a stream connecting to a waterfall. Do you want to swim or wait for sunrise?\n").lower()
        if b == "wait":
            print("\nFollowing day, you found a house with 3 doors - Red, Blue, and Yellow.")
            c = input("Which door do you want to open?\n").lower()
            if c == 'red':
                print('''
                              (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                ''')
                print("\nYou were burned by by fire. Game over.")
            elif c == 'blue' or c == 'Blue':
                print('''
                
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
                ''')
                print("\nYou were eaten by beasts. Game over.")

            elif c == ' Yellow' or c == 'yellow':
                print("\n\nYou win! Congratulations!")
                print('''

                *******************************************************************************
                          |                   |                  |                     |
                 _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|___________________
                          |                `"=._o`"=._      _`"=._                     |
                 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                /______/______/______/______/______/______/______/______/______/______/[TomekK]
                *******************************************************************************
                ''')
            else:
                "\n\nYou chose a door that doesn't exist. Game over."
        else:
            print("\n\nYou were attacked by an aggressive tribe. Game over.")
    else:
        print("\n\nYou fell into a hole. Game over.")
else:
    print("\n\nThanks for playing the game.")

