def gameMenu():
  def menu():
    print("[1] Catch some fish")
    print("[2] Show scores")
    print("[0] Exit application")
    
  menu()
  
  option = int(input("Enter your option: "))
  
  while option != 0:
    if option == 1:
      # catchFish()
      print("Catch Fish")
    elif option == 2:
      # showScore()
      print("Show score")
    else:
      print("Invalid option")
      
    print()
    menu()
    option = int(input("Enter your option: "))

    