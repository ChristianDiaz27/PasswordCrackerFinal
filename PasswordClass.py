# Takes a string of numbers (or all characters) and systematically searches, finds, and outputs the password
# Simulates a brute-force password cracking method
class PasswordCracker():

    # Takes the inputted password and stores it
    # Declares needed character bank and count variables
    def __init__(self, password):
        self.__password = password
        self.__CHARACTERBANK = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # To allow the program to look for letters and symbols then replace the current characterBank with this one
        # Replace the corresponding line in the Python Final file to allow the for other passwords to be inputted
        #self.__CHARACTERBANK = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         #"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H",
          # "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "~", "`", "!", "@",
           #"#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "'",
           #"<", ",", ">", ".", "?", "/"]
        self.__guess = ""
        self.__count1 = 0
        self.__count2 = 0
        self.__count3 = 0
        self.__count4 = 0
        self.__count5 = 0
        self.__count6 = 0
        self.__count7 = 0
        self.__count8 = 0
        self.__count9 = 0
        self.__count10 = 0

    # private method used to set all count variables to zero
    def __reset(self):
        self.__count1 = 0
        self.__count2 = 0
        self.__count3 = 0
        self.__count4 = 0
        self.__count5 = 0
        self.__count6 = 0
        self.__count7 = 0
        self.__count8 = 0
        self.__count9 = 0
        self.__count10 = 0

    # Initial method of the password cracking process
    # If the user-inputted password is only one character then it will output the password
    # Otherwise it calls for the next method
    def crackPassword(self):
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1])
            self.__count1 += 1
            if self.__count1 >= len(self.__CHARACTERBANK):
                break
          # Remove the comment marker to make the program show the cracking process
          # WARNING this can result in significantly increased processing times
          # Especially for methods testing for more characters
          #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char2Check())

    # Checks if the user-inputted password is two characters long
    # Outputs the password if it is, otherwise calls for next method
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char2Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2])
            self.__count2 += 1
            if self.__count2 >= len(self.__CHARACTERBANK):
                self.__count2 = 0
                self.__count1 += 1
                if self.__count1 >= len(self.__CHARACTERBANK):
                    break
            # Remove the comment marker to make the program show the cracking process
            # WARNING this can result in significantly increased processing times
            # Especially for methods testing for more characters
            #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char3Check())

    # Checks if the user-inputted password is three characters long
    # Outputs the password if it is, otherwise calls for next method
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char3Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2] +
                          self.__CHARACTERBANK[self.__count3])
            self.__count3 += 1
            if self.__count3 >= len(self.__CHARACTERBANK):
                self.__count3 = 0
                self.__count2 += 1
                if self.__count2 >= len(self.__CHARACTERBANK):
                    self.__count2 = 0
                    self.__count1 += 1
                    if self.__count1 >= len(self.__CHARACTERBANK):
                        break
          # Remove the comment marker to make the program show the cracking process
          # WARNING this can result in significantly increased processing times
          # Especially for methods testing for more characters
          #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char4Check())

    # Checks if the user-inputted password is four characters long
    # Outputs the password if it is, otherwise calls for next method
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char4Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2] +
                          self.__CHARACTERBANK[self.__count3] + self.__CHARACTERBANK[self.__count4])
            self.__count4 += 1
            if self.__count4 >= len(self.__CHARACTERBANK):
                self.__count4 = 0
                self.__count3 += 1
                if self.__count3 >= len(self.__CHARACTERBANK):
                    self.__count3 = 0
                    self.__count2 += 1
                    if self.__count2 >= len(self.__CHARACTERBANK):
                        self.__count2 = 0
                        self.__count1 += 1
                        if self.__count1 >= len(self.__CHARACTERBANK):
                            break
            # Remove the comment marker to make the program show the cracking process
            # WARNING this can result in significantly increased processing times
            # Especially for methods testing for more characters
            #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char5Check())

    # Checks if the user-inputted password is five characters long
    # Outputs the password if it is, otherwise calls for next method
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char5Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2] +
                          self.__CHARACTERBANK[self.__count3] + self.__CHARACTERBANK[self.__count4] +
                          self.__CHARACTERBANK[self.__count5])
            self.__count5 += 1
            if self.__count5 >= len(self.__CHARACTERBANK):
                self.__count5 = 0
                self.__count4 += 1
                if self.__count4 >= len(self.__CHARACTERBANK):
                    self.__count4 = 0
                    self.__count3 += 1
                    if self.__count3 >= len(self.__CHARACTERBANK):
                        self.__count3 = 0
                        self.__count2 += 1
                        if self.__count2 >= len(self.__CHARACTERBANK):
                            self.__count2 = 0
                            self.__count1 += 1
                            if self.__count1 >= len(self.__CHARACTERBANK):
                                break
            # Remove the comment marker to make the program show the cracking process
            # WARNING this can result in significantly increased processing times
            # Especially for methods testing for more characters
            #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char6Check())

    # Checks if the user-inputted password is six characters long
    # Outputs the password if it is, otherwise calls for next method
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char6Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2] +
                          self.__CHARACTERBANK[self.__count3] + self.__CHARACTERBANK[self.__count4] +
                          self.__CHARACTERBANK[self.__count5] + self.__CHARACTERBANK[self.__count6])
            self.__count6 += 1
            if self.__count6 >= len(self.__CHARACTERBANK):
                self.__count6 = 0
                self.__count5 += 1
                if self.__count5 >= len(self.__CHARACTERBANK):
                    self.__count5 = 0
                    self.__count4 += 1
                    if self.__count4 >= len(self.__CHARACTERBANK):
                        self.__count4 = 0
                        self.__count3 += 1
                        if self.__count3 >= len(self.__CHARACTERBANK):
                            self.__count3 = 0
                            self.__count2 += 1
                            if self.__count2 >= len(self.__CHARACTERBANK):
                                self.__count2 = 0
                                self.__count1 += 1
                                if self.__count1 >= len(self.__CHARACTERBANK):
                                    break
            # Remove the comment marker to make the program show the cracking process
            # WARNING this can result in significantly increased processing times
            # Especially for methods testing for more characters
            #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char7Check())

    # Checks if the user-inputted password is seven characters long
    # Outputs the password if it is, otherwise calls for next method
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char7Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2] +
                          self.__CHARACTERBANK[self.__count3] + self.__CHARACTERBANK[self.__count4] +
                          self.__CHARACTERBANK[self.__count5] + self.__CHARACTERBANK[self.__count6] +
                          self.__CHARACTERBANK[self.__count7])
            self.__count7 += 1
            if self.__count7 >= len(self.__CHARACTERBANK):
                self.__count7 = 0
                self.__count6 += 1
                if self.__count6 >= len(self.__CHARACTERBANK):
                    self.__count6 = 0
                    self.__count5 += 1
                    if self.__count5 >= len(self.__CHARACTERBANK):
                        self.__count5 = 0
                        self.__count4 += 1
                        if self.__count4 >= len(self.__CHARACTERBANK):
                            self.__count4 = 0
                            self.__count3 += 1
                            if self.__count3 >= len(self.__CHARACTERBANK):
                                self.__count3 = 0
                                self.__count2 += 1
                                if self.__count2 >= len(self.__CHARACTERBANK):
                                    self.__count2 = 0
                                    self.__count1 += 1
                                    if self.__count1 >= len(self.__CHARACTERBANK):
                                        break
            # Remove the comment marker to make the program show the cracking process
            # WARNING this can result in significantly increased processing times
            # Especially for methods testing for more characters
            #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char8Check())

    # Checks if the user-inputted password is eight characters long
    # Outputs the password if it is, otherwise calls for next method
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char8Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2] +
                          self.__CHARACTERBANK[self.__count3] + self.__CHARACTERBANK[self.__count4] +
                          self.__CHARACTERBANK[self.__count5] + self.__CHARACTERBANK[self.__count6] +
                          self.__CHARACTERBANK[self.__count7] + self.__CHARACTERBANK[self.__count8])
            self.__count8 += 1
            if self.__count8 >= len(self.__CHARACTERBANK):
                self.__count8 = 0
                self.__count7 += 1
                if self.__count7 >= len(self.__CHARACTERBANK):
                    self.__count7 = 0
                    self.__count6 += 1
                    if self.__count6 >= len(self.__CHARACTERBANK):
                        self.__count6 = 0
                        self.__count5 += 1
                        if self.__count5 >= len(self.__CHARACTERBANK):
                            self.__count5 = 0
                            self.__count4 += 1
                            if self.__count4 >= len(self.__CHARACTERBANK):
                                self.__count4 = 0
                                self.__count3 += 1
                                if self.__count3 >= len(self.__CHARACTERBANK):
                                    self.__count3 = 0
                                    self.__count2 += 1
                                    if self.__count2 >= len(self.__CHARACTERBANK):
                                        self.__count2 = 0
                                        self.__count1 += 1
                                        if self.__count1 >= len(self.__CHARACTERBANK):
                                            break
            # Remove the comment marker to make the program show the cracking process
            # WARNING this can result in significantly increased processing times
            # Especially for methods testing for more characters
            #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char9Check())

    # Checks if the user-inputted password is nine characters long
    # Outputs the password if it is, otherwise calls for next method
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char9Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2] +
                          self.__CHARACTERBANK[self.__count3] + self.__CHARACTERBANK[self.__count4] +
                          self.__CHARACTERBANK[self.__count5] + self.__CHARACTERBANK[self.__count6] +
                          self.__CHARACTERBANK[self.__count7] + self.__CHARACTERBANK[self.__count8] +
                          self.__CHARACTERBANK[self.__count9])
            self.__count9 += 1
            if self.__count9 >= len(self.__CHARACTERBANK):
                self.__count9 = 0
                self.__count8 += 1
                if self.__count8 >= len(self.__CHARACTERBANK):
                    self.__count8 = 0
                    self.__count7 += 1
                    if self.__count7 >= len(self.__CHARACTERBANK):
                        self.__count7 = 0
                        self.__count6 += 1
                        if self.__count6 >= len(self.__CHARACTERBANK):
                            self.__count6 = 0
                            self.__count5 += 1
                            if self.__count5 >= len(self.__CHARACTERBANK):
                                self.__count5 = 0
                                self.__count4 += 1
                                if self.__count4 >= len(self.__CHARACTERBANK):
                                    self.__count4 = 0
                                    self.__count3 += 1
                                    if self.__count3 >= len(self.__CHARACTERBANK):
                                        self.__count3 = 0
                                        self.__count2 += 1
                                        if self.__count2 >= len(self.__CHARACTERBANK):
                                            self.__count2 = 0
                                            self.__count1 += 1
                                            if self.__count1 >= len(self.__CHARACTERBANK):
                                                break
            # Remove the comment marker to make the program show the cracking process
            # WARNING this can result in significantly increased processing times
            # Especially for methods testing for more characters
            #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return(self.__char10Check())

    # Checks if the user-inputted password is two characters long
    # Outputs the password if it is, otherwise outputs error message
    # All char#Check methods systematically guess every possible combination
    # Once a character at a position has reached nine and the password was not found
    # The position will be reset to 0 and the character at the position to the left of it will
    # go up by one until the character at the first position has exceeded nine
    def __char10Check(self):
        self.__reset()
        while self.__guess != self.__password:
            self.__guess = (self.__CHARACTERBANK[self.__count1] + self.__CHARACTERBANK[self.__count2] +
                          self.__CHARACTERBANK[self.__count3] + self.__CHARACTERBANK[self.__count4] +
                          self.__CHARACTERBANK[self.__count5] + self.__CHARACTERBANK[self.__count6] +
                          self.__CHARACTERBANK[self.__count7] + self.__CHARACTERBANK[self.__count8] +
                          self.__CHARACTERBANK[self.__count9] + self.__CHARACTERBANK[self.__count10])
            self.__count10 += 1
            if self.__count10 >= len(self.__CHARACTERBANK):
                self.__count10 = 0
                self.__count9 += 1
                if self.__count9 >= len(self.__CHARACTERBANK):
                    self.__count9 = 0
                    self.__count8 += 1
                    if self.__count8 >= len(self.__CHARACTERBANK):
                        self.__count8 = 0
                        self.__count7 += 1
                        if self.__count7 >= len(self.__CHARACTERBANK):
                            self.__count7 = 0
                            self.__count6 += 1
                            if self.__count6 >= len(self.__CHARACTERBANK):
                                self.__count6 = 0
                                self.__count5 += 1
                                if self.__count5 >= len(self.__CHARACTERBANK):
                                    self.__count5 = 0
                                    self.__count4 += 1
                                    if self.__count4 >= len(self.__CHARACTERBANK):
                                        self.__count4 = 0
                                        self.__count3 += 1
                                        if self.__count3 >= len(self.__CHARACTERBANK):
                                            self.__count3 = 0
                                            self.__count2 += 1
                                            if self.__count2 >= len(self.__CHARACTERBANK):
                                                self.__count2 = 0
                                                self.__count1 += 1
                                            if self.__count1 >= len(self.__CHARACTERBANK):
                                                break
            # Remove the comment marker to make the program show the cracking process
            # WARNING this can result in significantly increased processing times
            # Especially for methods testing for more characters
            #  print("Trying " + self.__guess)
        if self.__guess == self.__password:
            return str("Your password was found! It was " + self.__guess)
        else:
            return str("I was unable to guess your password, sorry!")