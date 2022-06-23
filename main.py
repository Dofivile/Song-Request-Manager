
print("Welcome to DJ Pythonic's Song Request Manger!")
print("Enter the song title to make a song request.")
print("To exit, enter Quit.")
print("-------------------------------------------------")
count=1
song=[]
option=input("Enter the song title: ")
while option.lower()!="quit":
    print('The song',option,'has been added to the list. It is song number',count,'on the list')
    song.append(option)
    count+=1
    option=input("Enter the song title: ")
   
  

print("Thank you for your requests. Enjoy the show! ")

     
def menu():
  orders=[]
  print("-- STARBUCKS MENU--")
  print("1. Iced Coffee ")
  print("2. Blonde Roast")
  print("3. Matcha Latte")
  print("4. Cold brew ")
  print("5. Caramel Macc ")
  print("6. Pumpkin Spice Latte")
  print("7. Peppermint Macha")
  print("8. Iced Green ")
  print("9. Mango Dragonfruit")
  print("10. Iced Dirty Chai")
  option=input("What would you like to order? (1_10): ")
  while(option.lower()!="Done"):
     if(option==1):
      orders.append("Iced Coffee")
     elif(option==2):
       orders.append("Blonde Roast")
     elif(option==3):
       orders.append("Matcha Latte")
     elif(option==4):
       orders.append("Cold brew ")
     elif(option==5):
       orders.append("Caramel Macc ")
     elif(option==6):
       orders.append("Pumpkin Spice Latte ")
     elif(option==7):
       orders.append("Peppermint Macha ")
     elif(option==8):
       orders.append("Iced Green ")
     elif(option==9):
       orders.append("Mango Dragonfruit")
     elif(option==10):
       orders.append("Iced Dirty Chai")
    
     option=input("Would you like anything else?: ") 
  print("Thank you for your order! Here is your order: ")
  print(orders)
       
        
menu()


