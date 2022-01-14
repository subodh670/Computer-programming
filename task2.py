def read_sentence():
    """The read_sentence helps to take user input of swallow speeds of birds and resolves average, min and max speed of the bird."""
    print("Swallow Speed Analysis: Version 1.0")
    speed_data = list()                      #An empty list
    while(True):
        readings = input("Enter the Next Reading: ")    #Reading the input in E/U format

        if(readings):                                   #Only readings is not empty
            if(readings[0] == "E"):                     #Slicing the first letter in readings and checking it
                speed_data.append(float(readings[1:])/1.60934)   #Appending to list in kilometre format by converting it
            elif(readings[0] == "U"):
                speed_data.append(float(readings[1:]))        #Appending to list in kilometre format
            print("Reading Saved")

        elif(readings == ""):                       #if readings is not given
            if(len(speed_data) == 0):               #if readings is not given from start break from loop
                print("No readings entered. Nothing to do.")
                break                               
            no_of_readings = len(speed_data)        #Total number of readings
            print("1 reading analyzed") if (no_of_readings == 1) else print(f"{no_of_readings} readings analyzed")                              #Displaying total number of readings and break from loop
            print("\nResults Summary")
            break

    if(len(speed_data)):                            #only list of speed data is not empty
        max_speed = max(speed_data)                 #maximum of all speed data
        min_speed = min(speed_data)                 #Minimum of all speed data
        aver_speed = sum(speed_data)/len(speed_data)#Average of all speed data
        print(f"The max is {max_speed:.1f} MPH, {max_speed*1.60934:.1f} KPH ")  #printing all the data in both MPH and KPH
        print(f"The min is {min_speed:.1f} MPH, {min_speed*1.60934:.1f} KPH")
        print(f"The average is {aver_speed:.1f} MPH, {aver_speed*1.60934:.1f} KPH")

if __name__ == "__main__":              #if script is running directly
    read_sentence()




            

