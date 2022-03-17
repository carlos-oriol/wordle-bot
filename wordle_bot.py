import sys
import pandas as pd

print("Welcome!")

def main():
    print("Are you ready for today's WORDLE?")
    
if __name__ == "__main__":
    main()

# play_wordle plays the wordle game using the dataset provided as a csv
def play_wordle():
    words_df = pd.read_csv('five_letters.csv')
    attempt = 1

    # Wordle allows only for 6 attempts (Initial Guess + 5)
    while attempt <= 5:
        
        return None

    return None