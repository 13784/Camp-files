import random 
def main():
    print("Welcome to six sided dice roll.")
    answer= random.randint(1,6)
    print("You rolled a " + str(answer))
    
if __name__ == "__main__":
    main()