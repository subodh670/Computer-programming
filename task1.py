print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see. ")
any_name = input("What is your name? ").lower()  #reading the name from the user
if(any_name == "arthur"):                        
    print("My liege! You may pass!")             #in case person is king arthur
else:
    seek = input("What is your quest? ")        
    if("grail" in seek.lower()):                 #in case person is seeking for grail
        color = input("What is your favourite colour? ").lower()
        print("You may pass!!") if(color[0] == any_name[0].lower()) else print("Incorrect! You must now face the Gorge of Eternal Peril.")                  #in case person name's letter is same as color's first letter
    else:
        print("Only those who seek the Grail may pass.")  #in case person is not seeking for grail

    

        
