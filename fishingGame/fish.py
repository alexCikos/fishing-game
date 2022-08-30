import csv

def getFish(randomNumber):

  dict_from_csv = {}
  file = "/Users/alexcikos/Desktop/fishingGame/fish.csv"

  with open(file, mode='r') as inp:
      reader = csv.reader(inp)
      dict_from_csv = {rows[0]:rows[1] for rows in reader}
      new_list = list(dict_from_csv.values())
      
      new_list = new_list[randomNumber]
          
      return new_list
  
      
      
      

      
  
    
    
    
    
    
    
    
    