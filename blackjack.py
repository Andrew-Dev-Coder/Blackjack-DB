"""
This python code is a game of blackjack using CLI for input.
The computer is referred to as the "dealer" or "house".
The user is referred to as the "player".
The user can choose to have their score added to a database which is used to create a leaderboard.
"""

#Import modules
from random import choice as ch #Used for randomising
import argon2 #For error handling 
from argon2 import PasswordHasher #Used for hashing passwords
import sqlite3 #Used for querring a database
import os #Used to get the folder path
from getpass import getpass #Used to hide the user's input

#Define functions
#Asks the user if they want to play again
def PlayAgain():
    restart = False
    
    #Use a conditioned while loop to check if the user wants to play again.
    while restart == False:
        again = stringInput("\nWould you like to play again?")
        again = again.lower()
        
        if again == "yes" or again == 'y':
            return True
        elif again == "no" or again == 'n':
            return False
        else:
            print("\nPlease enter yes or no.")
        #end if
    #end while
#end def

#Function to randomly pick a card
def NewCard():
    global deck
    card = ch(deck)
    return card
#end def

#Function to get the user's desicion
def Choice():
    global PTotal, playerDeck, deck, CardValues, DTotal, PScore, HScore
    
    run = False
    
    #Use a conditioned while loop to ask if the user wants to hit or stand
    while run != True:
        choice = stringInput("Hit or Stand?")
        choice = choice.lower()
        
        if choice == "hit":
            Card = (NewCard())
            playerDeck.append(Card)
            
            #Recualte the players hand
            PTotal = Calculate(playerDeck, PTotal)
            print(f"\nThe value of your cards is {PTotal} and your cards are {', '.join(playerDeck)}.")
            Check = ValueCheck()
            if Check == True:
                run = True
            
        elif choice == "stand":
            run = True
        else:
            print("\nPlease pick hit or stand.")
        #end if
    #end while
#end def

#Fuction to make the hand of all players
def CreateHand():
    global deck
    
    decks = []
    i = 1
    
    #Use a for loop to only give 2 cards to the hand.
    for i in range(2):
        card = NewCard()
        decks.append(card)
        i += 1
    #end for
    return decks
#end def

#Function to caculate the value of the cards given to the player and dealer
def Calculate(hand, total):
    global CardValues
    total = 0
    aces = []

    #use a for loop to go through the whole deck to caulate the value of the deck
    for card in hand:
        rank = card.split(" ")[0]
        total += CardValues[rank]
        if rank == "Ace" or rank == 'ace':
            aces.append(card)
        #end if
    #end for

    #Use a while loop to make an ace worth one if the total value has gone over 21
    while total > 21 and len(aces) >= 1:
        for ace in aces:
            for card in aces:
                total -= 10
                aces.pop()
    #end while

    return total
#end def

#A function to check if the dealer or player has gone bust.
def ValueCheck():
    global PTotal, DTotal, PScore, HScore, Bust
    
    if PTotal == 21 and DTotal == 21:
        print("\nYou have both got blackjack (over 21).\nThis game is a draw.")
        HScore += 1
        PScore += 1
        Bust = True
        return True
            
    elif PTotal > 21:
        print("\nYou have gone bust (over 21).\nHouse Wins")
        HScore += 1
        DisplayScores()
        Bust = True
        return True
        
    elif DTotal > 21:
        print("\nDealer has gone bust (over 21).\nYou Win.")
        PScore += 1
        DisplayScores()
        Bust = True
        return True
    
    elif DTotal == 21:
        print("\nThe dealer has won with blackjack (21).")
        HScore += 1
        DisplayScores()
        Bust = True
        return True
    
    elif PTotal == 21:
        print("\nYou have won with blackjack (21).")
        PScore += 1
        DisplayScores()
        Bust = True
        return True
    else:
        return False
        #end if
    #end while
#end def

#A function to see who has the highest score
def TotalCheck():
    global PTotal, DTotal, PScore, HScore
    check = False
    
    while check != True:
        if PTotal > DTotal:
            print(f"\nYou Win.")
            PScore += 1
            DisplayScores()
            check = True
            
        elif PTotal < DTotal:
            print(f"\nHouse Wins.")
            HScore += 1
            DisplayScores()
            check = True
        
        elif PTotal == DTotal:
            print(f"\nThe game is a draw.")
            HScore += 1
            PScore += 1
            DisplayScores()
            check = True
            
        else:
            print("\nAn error has occured.")
        #end if
    #end while
#end def

#A function for the computer to decide wether to "hit" or "stand".
def DelearChoice():
    global DTotal, dealerHand, deck, CardValues, PTotal, PScore, HScore
    run = True
    
    while run == True:
        if DTotal >= 17:
            return DTotal, dealerHand
        elif DTotal <= 16:
            Card = (NewCard())
            dealerHand.append(Card)
            DTotal = Calculate(dealerHand, PTotal)
            if ValueCheck() == True:
                run = True
        #end if
    #end while
#end def

#Made a function to correctly display game or games depeding on the score of the player and computer (House/Delear)
def DisplayScores():
    global PScore, HScore
    
    if len(playerDeck) == 2:
        if len(dealerHand) == 2:
            print(f"\nYou had {PTotal} with: {' and '.join(playerDeck)}. The dealer had {DTotal} with: {' and '.join(dealerHand)}")
        elif len(dealerHand) > 2:
            print(f"\nYou had {PTotal} with: {' and '.join(playerDeck)}. The dealer had {DTotal} with: {', '.join(dealerHand)}")
        #end if
    elif len(playerDeck) > 2:
        if len(dealerHand) == 2:
            print(f"\nYou had {PTotal} with: {', '.join(playerDeck)}. The dealer had {DTotal} with: {' and '.join(dealerHand)}")
        elif len(dealerHand) > 2:
            print(f"\nYou had {PTotal} with: {', '.join(playerDeck)}. The dealer had {DTotal} with: {', '.join(dealerHand)}")
        #end if
    #end if  
    
    if PScore > 1 or PScore == 0:
        if HScore > 1 or HScore == 0:
            print(f"\nThe game has ended.\nYou have won {PScore} games.\nThe computer has won {HScore} games.")
        elif HScore == 1:
            print(f"\nThe game has ended.\nYou have won {PScore} games.\nThe computer has won {HScore} game.")
        #end if
    elif PScore < 1:
        if HScore < 1:
            print(f"\nThe game has ended.\nYou have won {PScore} game.\nThe computer has won {HScore} game.")
        elif HScore > 1 or HScore == 0:
            print(f"\nThe game has ended.\nYou have won {PScore} game.\nThe computer has won {HScore} games.")
        #end if
    #end if
#end def

#Take a sting input and perform a presence check
def stringInput(reason):
    valid = False
    
    while valid != True:
        Input = input(f'{reason}: ')
        
        #Perform presence check
        if Input == '' or Input == ' ':
            print("\nPlease do not leave the input blank.")
        elif Input != '':
            return Input
        else:
            print("An error has occured")
        #end if
    #end while
#end def

#Make a deck of cards
def Deck(Cards):
    formed = False
    
    deck =[]
    i = 0
    x = 0
    for i in range(3):
        for x in range(11):
            Card = str(Cards[2][x])
            card = (Card.capitalize() + ' of ' + Cards[0][i].capitalize())
            deck.append(card)
        #end for
    #end for

    return deck
# end def

#Declare constants
CardValues = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'Ace' : 11,
  'Jack': 10,
  'King': 10,
  'Queen': 10
}

#Declare variables.
#The starting deck of cards
Cards = [
  #   0         1          2          3
  ["clubs", "diamonds", "hearts", "spades"],
  #  0        1
  ["red", "black"],
  #  0    1  2  3  4  5  6  7  8    9       10      11
  ["ace", 2, 3, 4, 5, 6, 7, 8, 9, "jack", "king", "queen"]
]

deck = Deck(Cards)
#Variables to keep track of who has won the most games.
PScore = 0
HScore = 0

#A variable to track loops
Run = True

#Ask the user if they want to connect to the database
choice = stringInput("Would you like to add your score to the leaderboard (Yes/No)?")
choice = choice.lower()

#Get the folder path
folder_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(folder_path, 'Database', 'data.db')
        
#Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
        
#Start passwordHasher
ph = PasswordHasher()

while Run == True:
    #Only connect to the database if the user wants to add to the leaderboard
    if choice == "yes" or choice == "y":
        
        #Variables to control loops
        commit = True
        verfied = False
        
        #Check if the user has an account
        check = stringInput("Do you have an account (Yes/No)?")
        check = check.lower()
        
        if check == "yes" or check == 'y':
            #Get the users username
            username = stringInput("What is your username?")
            
            cursor.execute(" SELECT username FROM Players WHERE username = '%s' " % username)
            search = cursor.fetchone()
            
            #Allow the user to sign in if the username exists
            if search:
                password = getpass()
                
                cursor.execute(" SELECT password FROM Players WHERE username = '%s' " % username)
                search = cursor.fetchall()
                
                for hash in search:
                    try:
                        ph.verify(hash[0], password)
                        
                        userData = ({'hash': hash[0], 'username': username})
                        
                        print("\nLogin successful")
                        
                        cursor.execute("SELECT userID FROM Players WHERE password = :hash AND username = :username; ", userData)
                        userID = cursor.fetchone()
                        userID = userID[0]
                        
                        if ph.check_needs_rehash(hash[0]):
                            userData = ({'hash': new_hash, 'userID': userID})
                            new_hash = ph.hash(password)
                            cursor.execute("UPDATE Players (password) SET password = :hash WHERE userID = :userID; ", userData)
                        #end if
                        
                        print(f"Your user ID is {userID}.")
                        verfied = True
                        Run = False
                    except argon2.exceptions.VerifyMismatchError:
                            continue
                        #end try except`
                    #end while
                #end for
                
                if verfied == False:
                    print("Inccorrect password")
                #end if
            else:
                print("\nThere is no account with that username.")
            #end if
            
        #Allow the user to create a new account if they don't currently have one
        elif check == 'no' or check == 'n':
            username = stringInput("What do you want your username to be?") 
            
            password = getpass()
            passwordCheck = getpass("Confirm Password:")
            
            #ensure the passwords match
            if password == passwordCheck:
                #Hash the password
                password = ph.hash(password)
                
                #commit the data to the database
                userData = ({'username': username, 'password':password})
                cursor.execute("INSERT INTO Players (username, password) VALUES (:username, :password); ", userData)
                conn.commit()
                print("\nCommited to database")
                
                #Get the userID
                cursor.execute("SELECT userID FROM Players WHERE password = :password AND username = :username; ", userData)
                userID = cursor.fetchone()
                userID = userID[0]
                print(f"Your user ID is {userID}.")
                
                cursor.execute("INSERT INTO Data (playerID) VALUES ('%s') " % userID)
                conn.commit()
                
                Run = False
            elif password != passwordCheck:
                print("Your passwords do not match.")
            else:
                print("An error has occured")
            #end if       
        else:
            print("Please only enter yes or no.")
        #end if
        
    elif choice == "no" or choice == "n":
        conn.close()
        commit = False
        Run = False
    else:
        print("Please only enter yes or no.")
    #end if
#end while

Run = True
i = 1

#Explain the game.
print("\nThis is a game of Blackjack.\nYou are the player and the computer is the delear and house.")

#Main game
while Run == True:
    #A varibale to track game running
    gameRun = True
    
    #A varibale to track if someone has gone bust
    Bust = False
    
    #Make the hands of the player and dealer.
    playerDeck = []
    dealerHand = []
    playerDeck = CreateHand()
    dealerHand = CreateHand()

    #Calculate the values of the player and dealer decks.
    PTotal = 0
    DTotal = 0
    PTotal = Calculate(playerDeck, PTotal)
    DTotal = Calculate(dealerHand, DTotal)
    
    #Show the cards
    print(f"\nOne of the dealers cards is {dealerHand[0]}.\nThe value of your cards is {PTotal} and your cards are {' and '.join(playerDeck)}.")

    if ValueCheck() == False and gameRun == True:
        Choice()
        if Bust == False:
            DelearChoice()
        if Bust == False:
            TotalCheck()
        gameRun = False
    if Bust == True or gameRun == False:
        choice = PlayAgain()
        if choice == False:
            Run = False
        elif choice == True:
            continue
        else:
            print("\nAn error has occured.")
    else:
        print("\nAn error has occured.")
    #end if
#end while

DisplayScores()
#Update the database based on the new scores and display the leaderbaord to the user
if commit == True:
    #Get player wins
    cursor.execute("SELECT playerWins FROM Data WHERE playerID = '%s' " % userID)
    previousWins = cursor.fetchone()
    if previousWins:
        previousWins = previousWins[0]
    #end if
    
    #Get computer wins
    cursor.execute("SELECT houseWins FROM Data WHERE playerID = '%s' " % userID)
    houseWins = cursor.fetchone()
    if houseWins:
        houseWins = houseWins[0]
    #end if
    
    #Caculate total wins for the house and player
    updatedHouseWins = houseWins + HScore
    updatedPlayerWins = previousWins + PScore
    
    #Caculate the in percentage of the player
    totalWins = updatedPlayerWins + updatedHouseWins
    winPercantage = (updatedPlayerWins / totalWins) * 100
    winPercantage = round(winPercantage, 2)
    winPercantage = str(winPercantage) + '%'
    
    #Added it to a dictinoary for binding
    userData = ({'totalWins': updatedPlayerWins, 'houseWins': updatedHouseWins, 'winPercent': winPercantage , 'userID': userID})
    
    #Add the data to the database and then close the connection
    cursor.execute("UPDATE Data SET playerWins = :totalWins, houseWins = :houseWins, winPercentage = :winPercent WHERE playerID = :userID; ", userData)
    conn.commit()
    
    #Access the leaderboard and sort it by descending order
    cursor.execute("SELECT Players.username, Data.playerWins, Players.userID, Data.winPercentage FROM Players, Data WHERE Players.userID = Data.playerID ORDER BY Data.winPercentage DESC")
    search = cursor.fetchall()
    
    #Display the leaderbaord to the user
    print("\nThe leaderbaord as it stands: ")
    
    for name in search:
        if name[2] == userID:
            if name[1] > 1 or name[1] == 0:
                print(f"{i}: {name[0]} (you) with {name[1]} wins, at {name[3]} win rate.")
                
            elif name[1] == 1:
                print(f"{i}: {name[0]} (you) with {name[1]} win, at {name[3]} win rate. ")
            #end if
            
        elif name[2] != userID:
            if name[1] > 1 or name[1] == 0:
                print(f"{i}: {name[0]} with {name[1]} wins, at {name[3]} win rate.")
                
            elif name[1] == 1:
                print(f"{i}: {name[0]} with {name[1]} win, at {name[3]} win rate. ")
            #end if
        
        else:
            print("An error has occured.")
        #end if
        
        if i >= 10:
            print("This leaderboard only shows the top ten.")
            break
        #end if
        
        i += 1
    #end for
    
    #Close the connection
    conn.close()
#end if