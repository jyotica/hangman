import random
class Hangman():
    #initializes the game and displays the rules of the game
    def __init__(self):
        print "Welcome to a game of..."
        print "H A N G M A N"
        print "How to play: \nYou need to guess the name of the country by entering various alphabets."
        print "Maximum number of mistakes you can make is 6."
        print ": \n: \n:"
        print "So, are you ready to play?"
        print "(1)YES, press 1! \n(2)NO, press 2!"
        user_input = input() #holds the value entered by the user to make a selection
        if (user_input == 1): #performs this when the user agrees to play
            print "Greattt, LETS BEGIN!"
            self.begin_game() #calls the function which begins the game
        elif (user_input == 2): #performs this when the user disagrees to play
            print "Goodbye </3..."
            exit() #ends the program/game
        else: #performs this when the user enters an incorrect selection 
            print "Sorry but you need to press either 1 or 2"
            self.__init__() #restarts the game

    #selects a random country name from the list which will be guessed by the user
    def get_random_country(self):
        countries = 'afghanistan albania algeria angola argentina armenia australia autria bahamas bahrain bangladesh barbados belgium bermuda bhutan bolivia brazil bulgaria burma cambodia cameroon canada chile china colombia congo croatia cuba denmark ecuador egypt england estonia ethiopia fiji finland france georgia germany ghana greece guatemala haiti honduras hungary iceland india indonesia iran iraq italy jamaica japan kazakhstan kenya kuwait laos latvia lebanon libya luxemborg madagascar malawi malaysia maldives malta mauritius mexico monaco mongolia montenegro morocco mozambique namibia nepal netherlands niger nigeria norway oman pakistan panama paraguay peru philippines poland portugal qatar romania serbia singapore slovenia somalia spain sudan sweden switzerland syria tanzania thailand tunisia turkey uganda ukraine uruguay uzbekistan venezuela vietnam yemen zambia zimbabwe'.split()
        country_index = random.randint(0, len(countries) - 1) #holds the index number of the country to be guessed, from the list
        return countries[country_index] #returns the country to be guessed to the appropriate function
    
    #displays the sturcture of the hangman according to the number of mistakes made
    def display_onscreen(self, mistakes):
        hangman_graphics_display = ['''
       ^
   +===|
   !   |
       |
       |
       |
       |
 =========''', '''

       ^
   +===|
   !   |
   O   |
       |
       |
       |
 =========''', '''

       ^
   +===|
   !   |
   O   |
   |   |
       |
       |
 =========''', '''

       ^
   +===|
   !   |
   O   |
  /|   |
       |
       |
 =========''', '''

       ^
   +===|
   !   |
   O   |
  /|\  |
       |
       |
 =========''', '''

       ^
   +===|
   !   |
   O   |
  /|\  |
  /    |

       |
 =========''', '''

       ^
   +===|
   !   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

        print(hangman_graphics_display[mistakes]) #prints the appropriate picture of the hangman (number of mistakes made = index of the hangman picture)

    #begins and controls all aspects of the game
    def begin_game(self):
        secret_country = self.get_random_country() #stores the name of the country to be guessed 
        print "No. of letters present in the name of the country is..."
        print len(secret_country)
        print ""
        progress = ['_']*len(secret_country) #creates a list of blanks according to number of letters in the country name to be guessed
        mistakes = 0 #initialisez the varibale that will hold number of mistakes made in guessing
        used_letters = "" #initializes the varibale that will hold the letters that are used while guessing
        updated = "" #initialized the variable that will be updated with correct letters (which will replace the blanks)
        while (mistakes<=5 and updated!=secret_country): #controls the number of chances to be allowed keeping in mind that the maximum number of mistakes is not exhausted
            guessed_letter = raw_input("Guess a letter : ") #stores the letter guessed by the user

            if(guessed_letter not in used_letters): #checks if the letter entered hasnt already been used

                if(guessed_letter in secret_country): #checks if the letter entered is in the country name to be guessed
                    print ""
                    print "GOOD CHOICE!!"
                    used_letters = used_letters + ' ' + guessed_letter #updates the string of used letters 
                    self.display_onscreen(mistakes) #calls the apporpriate function to display the suitable hangman picture
                    updated = self.update_country(guessed_letter, secret_country, progress) #calls the appropriate function to replace the blanks with correct letters 
                    print "YOUR PROGRESS:  " + updated #displays the updated word 
                    print "used letters: " + used_letters #displays the used letters
                    print ""

                else: #performs this if the guessed letter is not in the word to be guessed 
                    mistakes = mistakes + 1 #increases the number of mistakes made by the user 
                    print ""
                    print "...uh oh.. INCORRECT CHOICE"
                    used_letters = used_letters + ' ' + guessed_letter #updates the string of used letters 
                    self.display_onscreen(mistakes) #calls the appropriate function to display the suitable hangman picture after mistake made
                    print "YOUR PROGRESS:  " +"".join(progress) #displays the updated word till before the mistake was made
                    print "used letters: " + used_letters #displays the used letters
                    print ""

            else: #performs this if the entered letter is not valid  
                print "Enter an unused letter, PLEASE"
        
        if(updated == secret_country): #checks if the updated word matches the country name to be guessed 
            self.win_display() #calls the appropraite fucntion to display the final outcome of the game 
        if(mistakes==6): #checks if the number of mistakes has reached the upper limit 
            self.lose_display(secret_country) #calls the appropriate function to display the final outcome of the game and sends the name of the country which was to be guessed

    #updates the letters of the word to be guesss by replacing the blanks by the correctly guessed letter
    def update_country(self, guessed_letter, secret_country, progress):
        for j in range(0 , len(secret_country)): #performs relacement of every blank with the correctly guessed letter
            if (guessed_letter == secret_country[j]): #checks if the guessed letter is present in the word
                progress[j] = guessed_letter #letter replaces the blank according to its position in the word to be guessed 
        return "".join(progress) #returns the word after updating with correctly guessed letters 

    #displays the result of successfully winning the game 
    def win_display(self):
        print ""
        print ""
        print "Y O U  W O N"
        print "YAYYYAYAYY"
        print ""
        print"========================================================================="
        self.restart_game() #calls appropraite function to ask if user wishes to play another round of the game 

    #displays the result of losing the game
    def lose_display(self, secret_country):
        print ""
        print ""
        print "G A M E  O V E R"
        print "The country was "+secret_country #displays the country which was to be guessed 
        print ""
        print "Better luck next time!!"
        print ""
        print"========================================================================="
        self.restart_game() #calls appropriate function to ask if user wishes to play another round of the game

    #gives the option to the user to play another round of the game
    def restart_game(self):
        print "Do you want to play again?"
        print "YES? Press 'y' \nNO? Press 'n'"
        user_input2 = raw_input() #stores the selection made by the user
        if(user_input2 == 'y'): #checks entered value and perfoms this if user wishes to play another round 
            print "========================================================================="
            self.__init__() #calls fucntion to restart the game
        elif(user_input2 == 'n'): #checks enetered value and perfoms this if user wishes to discontinue the game
            exit() #ends the program/game
        else: #performs this when selection made by the user is invalid 
            print "press 'y' or 'n' only"
            self.restart_game() #asks the user again about playing another round of the game

    
game=Hangman()
