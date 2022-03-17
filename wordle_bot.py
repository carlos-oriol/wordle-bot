import sys
import pandas as pd

# play_wordle plays the wordle game using the dataset provided as a csv
def play_wordle():
    words_df = pd.read_csv('/Users/carlosoriol/Desktop/Projects/WORDLE/worlde-bot/five_letters.csv')
    attempt = 1

    while attempt < 6:
        
        word = 'TERAI'
        valid = False

        # Initial Guess if attempt == 1
        if attempt == 1:
            print("My first guess is: " + word)
        
        print('---------------------'+ '\n')
        print("What was the result?")
        print('Please enter a 5 letter string with either Y for yellow, G for green, or X for grey.')

        while True:
            
            result = input('Enter a word: ')

            # Edge case for when the input is null
            if result == '':
                print('Please enter a string.')
                continue

            # Edge case for when the input is not 5 digits
            if len(result) != 5:
                print()
                print('THIS STRING IS NOT VALID. TRY AGAIN!')
                continue

            else:
                break

        attempt += 1
        print('There are ' + str(6 - 1) + ' attempts remaining.')

    # Edge case for when attempts have run out
    if attempt == 6:
        print('We could not get it today. Try again tomorrow!')
        return None


def main():
    print()
    print('---------------------')
    print("Welcome! Are you ready for today's WORDLE?")
    play_wordle()
    
if __name__ == "__main__":
    main()
