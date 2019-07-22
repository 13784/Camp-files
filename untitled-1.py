import random 
def main():
     print("Welcome to random number guesser, guess the number between 1 and 10")
     answer= random.randint(1,10)
     tries=4
     while (tries >0):
          guess=int(input("guess a number:"))
          if answer==guess:
               print("correct")
               break
          else:
               if guess>answer:
                    print("your guess was too big")
               else:
                    print("your guess was too small")
               tries= tries - 1
               print("You have" +str (tries)+ "tries left")
          if tries == 0:
               print("You lose ahahaha!")
if __name__=="__main__":
     main()     
   