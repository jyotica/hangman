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
