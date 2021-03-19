import sys

from classes import Pytts

pytts = Pytts()

def main():
    """
    Main function
    """
    try:
        words = sys.argv[1]
    except IndexError:
        # print('')
        # sys.exit(1)
        words = 'absolutely massive computer'
    
    pytts.speak(words)
    # pytts.speak_word('pizza')

if __name__ == "__main__":
    main()
