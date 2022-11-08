display = ""
 
with open("books.txt", "r") as file:
    display = file.read()
file.close()
 
display_splt = display.split("--")
length = len(display_splt)
print(display_splt[0])
count = 0
 
page_input = input("[enter - read more or page number, press q to quit]: ")
 
while True:
    if page_input == 'q':
        print("Exited succesfully!")
        break
   
    if page_input == '':
        count = count + 1
        if count+1 > length:
            print('Sorry that page does not exist!\nGoing back to page 1!')
            print(display_splt[0])
           
        else:
            print(display_splt[count])
   
    else:
        print("Give correct input and try again!")
        print(display_splt[count])
           
    page_input = input("[enter - read more, press q to quit]: ")