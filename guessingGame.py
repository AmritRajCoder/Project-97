import random
play = True
while(play):
   num = random.randint(1,9)
   print("Number guessing game: \n Guess a number between 1 and 9")
   play = True
   ch =5
   while ch>0:
      inp = int(input("Enter your guess: "))
      if(inp==num):
         print("YOU WON!!! HURRAY!!!")
         break
      elif inp<num:
         print("Guess higher, a number greater than ", inp)
      else:
         print("Guess lower, a number less than ", inp)
      ch-=1
   if(ch==0):
      print("You Lost! Better Luck Next Time\n The number was: \n", num)
   agn = input("Would you like to play again? Y/N : ")
   if(agn=='N'):
      play = False
