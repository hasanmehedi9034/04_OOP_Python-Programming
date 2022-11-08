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
 
    if page_input == "":
        count = count + 1
        if count+1 > length:
            print('Sorry that page does not exist!\nGoing back to page 1!')
            print(display_splt[0])
 
        else:
            print(display_splt[count])
 
    else:
        temp = int(page_input)
 
        if temp < 0:
            if temp == -1:
                if count == 0:
                    print("There is no previous page, this is the first page.\nNow exiting...\n")
                    break
                count = count - 1
                print(display_splt[count])
            else:
                print("You can only press -1 for going to previous page!\n")
 
        elif temp == 0:
            print("Please enter a number other than zero!\n")
            break
 
        elif temp > length:
            print("Not enough page!\nThis is the last page below!")
            print(display_splt[length-1], '\n')
 
        else:
            count = count + temp
            if count+1>length:
                print("Page does not exist.\n Goint back to page one!")
                count = 0
 
            print(display_splt[count])
 
    page_input = input("[enter - read more or page number, press q to quit]: ")
 
