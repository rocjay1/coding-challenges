from datetime import date, time, datetime, timedelta
import random

def waiting_game():
    x = random.randint(2, 4)
    print("Your target time is", x, "seconds.")
    init = input("---Press ENTER to Begin---")
    print()
    if init == "":
        now = datetime.now()
        guess_input = input("...Press ENTER again after " + str(x) + " seconds...") 
        print()
        if guess_input == "":
            guess_time = datetime.now()
            elapsed_time = (guess_time - now).total_seconds()
            print("Elapsed time:", elapsed_time, "seconds")
            if elapsed_time >= x: print("(" + str(elapsed_time - x) + " seconds too slow)")
            else: print("(" + str(x - elapsed_time) + " seconds too fast)")

waiting_game()