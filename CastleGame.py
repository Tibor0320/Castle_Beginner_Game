# Welcome to the manor

import sys

print(r'''
*******************************************************************************
                                     ____                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____        


*******************************************************************************
''')
print("Thou hast arrived at that forsaken castle, where countless lost souls linger in eternal unrest")
print(r'''
For fifteen years, your wife has been but a memory. Every path, every whisper of fate has led you here—to 
this forsaken castle. Is she truly within… or merely another ghost in the dark?

*******************************************************************************
''')

# Options section

option1 = input('''
The castle looms before you, its iron gates slightly ajar. A chilling wind howls through the gaps, 
carrying whispers of the damned. The path forward splits:

A) Push open the grand iron doors, ignoring the whispers.
B) Take the narrow side passage shrouded in mist.

Choose by typing "A" or "B": ''').upper()

if option1 == "A":
    print('''

    ----------------------------------------------------------------------------------------------
    The doors groan as you push them open, revealing a dimly lit hallway beyond.
    The air is thick with dust and sorrow, and the castle’s cold embrace closes around you.
    ----------------------------------------------------------------------------------------------''')

    option2 = input('''
    ----------------------------------------------------------------------------------------------
    The hallway is lined with flickering candles, their flames dancing unnaturally.
    At the end, two staircases descend into the darkness.
    A cold draft seeps from the left, carrying the sound of distant sobbing. 
    The right is eerily silent, save for a single candle flickering at the base of the stairs.
    ----------------------------------------------------------------------------------------------

          A) Take the left staircase, where the faint sobbing echoes.
          B) Take the right staircase, where the lone candle flickers.
          You must choose! ''').upper()

    if option2 == "B":
        print(''' 
    -------------------------------------------------------------------------------------------------------------
    The candle’s flame flares up as you step toward it, illuminating a hidden inscription on the wall. 
    Following it, you descend safely into a grand chamber where a massive, dust-covered mirror stands before you.
    A gentle light guides you through the mansion. You come across a staircase.
    --------------------------------------------------------------------------------------------------------------
    ''')
        option3 = input('''
    -------------------------------------------------------------------------------
    The staircase leads into a crypt, the air thick with sorrow. 
    A massive, ancient door bars the way forward, inscribed with a single question:
    Does she wait… or does she weep? Or does she... deceive?
    ------------------------------------------------------------------------------


    A) "She waits."
    B) "She weeps."
    C) "She deceives." 
    Choose your answer!: ''').upper()
        if option3 == "A":
            print('''
            ---------------------------------------------------------------------------------------------
            The door groans in protest, then slams shut. 
            You hear a faint voice calling your name, but when you turn, the crypt is empty. 
            The walls close in, and your body freezes as you become one with the castle’s curse.
            ---------------------------------------------------------------------------------------------''')
            sys.exit("Game over")
        elif option3 == "B":
            print('''
            ---------------------------------------------------------------------------------------------------------
            The air thickens with sorrowful wails as the room begins to bleed. 
            Cold hands shoot from the cracks in the walls, dragging you into the depths. "Too late," a voice whispers. 
            You are consumed by the castle’s grief.
            ---------------------------------------------------------------------------------------------------------''')
            sys.exit("Game over")
        elif option3 == "C":
            print('''
            ----------------------------------------------------------------------------------------------------------------------------------
            The door creaks open, revealing a dim light. There, at the heart of the crypt, stands the one you’ve sought for fifteen long years. 
            But as you approach, her form flickers, revealing the truth—she is neither your wife nor a ghost. 
            She is the Duke's deception, a phantom forged from the darkest of spells. Her smile twists into a cruel grin, and she speaks:

            You’ve come so far, only to realize the truth. I was never meant to be found. You were always meant to be another lost soul in this place. 
            But now... now you have completed your journey."

            The crypt begins to shake, and the walls crack, but there’s a strange peace in your heart. Despite the torment, the struggle, and the pain, you’ve broken the cycle. 
            You’ve found the truth, and in a way, that was your victory.

            The voice whispers one last time as the light fades:
            "You won... but only in the way the lost can win—forever bound to the shadows of this forsaken place."
            -----------------------------------------------------------------------------------------------------------------------------------
            ''')

            sys.exit(
                "You have won the game... but at what cost? The castle’s curse is broken, but you will never leave. Your victory is forever stained by the truth. Farewell, lost soul.")
        else:
            print("Not an option")
            sys.exit("Game over")



    else:
        print('''
    --------------------------------------------------------------------------    
    The sobbing grows louder, then turns into shrill, agonized laughter. 
    Suddenly, unseen hands seize your ankles and drag you downward.
    You claw at the stone, but the darkness devours you whole.
    --------------------------------------------------------------------------
    ''')
        sys.exit("Game over")


else:
    print('''
    ----------------------------------------------------------------------------------------
     As you step into the mist, it thickens unnaturally. 
     You choke as unseen hands claw at your throat. 
     The whispers turn to laughter as you vanish into the fog, never to be seen again.
     ----------------------------------------------------------------------------------------''')
    sys.exit("Game over")

