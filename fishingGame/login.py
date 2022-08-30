import menu

# The login system, to gain access to the application
# Creating and storing a username and password in a text file
def register():
  db = open("data_base.txt", "r")
  userName = input("Enter a username: ")
  password = input("Enter a password: ")
  password1 = input("Confirm password: ")
  d = []
  f = []
  
  for i in db:
    a,b = i.split(", ")
    b = b.strip()
    d.append(a)
    f.append(b)
    
  data = dict(zip(d,f))
  
  if password != password1:
    print("Passwords do not match")
    register()
  else:
    if len(password)<=6:
      print("Password is too short")
      register()
    elif userName in d:
      print("User name already exists")
      register()
    else:
      db = open("data_base.txt", "a")
      db.write(userName+", "+password+ "\n")
      print("Sucess")
      print()
      menu.gameMenu()
      

# Checking if the username and password is in the text file
def access():
  db = open("data_base.txt", "r")
  userName = input("Enter your username: ")
  password = input("Enter your password: ")
  
  if not len(userName or password) <1:
    d = []
    f = []
  
    for i in db:
      a,b = i.split(", ")
      b = b.strip()
      d.append(a)
      f.append(b)
    
    data = dict(zip(d,f))
  
    try:
      if data[userName]:
        try:
          if password == data[userName]:
            print("Logic Sucessful")
            print("Hello, ", userName)
            print()
            menu.gameMenu()
            
          else:
            print("Username or passoword is incorrect")
        except:
          print("Incorrect password of username")
      else:
        print("User name does not exists")
    except:
      print("Username or password is does not exist")
      
  else:
    print("Enter a value")
  
   
# Main menu          
def home(option=None):
  option = input("Login | Signup: ")
  if option == "Login":
    access()
  elif option == "Signup":
    register()
  else:
    print("Enter an option")
      

    


  