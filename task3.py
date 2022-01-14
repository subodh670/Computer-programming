from random import choice
def check_email(mail_usr, domain="pop.ac.uk"):
    """Checking the user if mail of user is valid or not for specific domain"""

    global flag                 #declaring flag variable in global 
    flag = False                #initilizing flag with boolean value of False
    if("@" in mail_usr):        #only if mail of user contains @
        splitted_mail = mail_usr.split("@")
        usr_domain = splitted_mail[1]         #if user domain equal to default domain
        if(len(splitted_mail[0]) > 2 and usr_domain == domain):
            flag = True                         #flag assigned to true if all condition match
        else:
            print(f"{mail_usr} is not valid at {domain}")    
    else:
        print("The email address is not valid")     #only if first condition is failed

def chat_box():
    """ A chat conversations between user and a bot of random name with appropriate respose to a query """

    print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")
    usr_email_address = input("Please enter your Poppleton email address: ")#Taking user email address as input
    check_email(usr_email_address)                  #calling the function and checking validity of the email address
    random_names = ["Janice","Fiona","Alexa","Bixby","Siri","Arthur","Google"]
    chosen_name = choice(random_names)              #choosing the random bot name

    if(flag):                                       #in case flag is true
        usr_name_function = lambda usr1: usr1.split("@")[0].capitalize()
        usr_name = usr_name_function(usr_email_address)                 #processing the user name from email address
        print(f"Hi {usr_name}! Thank you and welcome to Popchat! ")     
        print(f"My name is {chosen_name}, and it will be my pleasure to help you.")

        query_reply = {                                             #queries keys and response inside dictionary
            ("wifi","internet","web"):["Wifi is excellent across campus.","Internet and wifi is working in all labs","Some of the websites in the web are restricted at some access points of wifi."],
            ("library","book","read"):["The library is closed today.","You need to have the library card to enter library.", "Library is open at 10'o clock in the morning."],
            ("deadline","submission","assesement"):["Your deadline has been extended by two working days.", "Your deadline is finished.", "Your deadline for assesement is postponed for two weeks."],
            ("payment","invoice","bills"):["Your payment has been done and bills will be sent ASAP.", "You haven't paid total student fees till date.", "You will be given notice to pay next due soon."],
            ("facilities","services","equipment"):["You have all facilities like library, cafe, study room in our campus.","You will be provided all services under the provisions of campus.","All students are provided facilities and equipments after admission."],
            ("activities","curricular","events"):["We organize extra-curricular activities once a week.","The events are held under the supervision of sports department.","Interested people can fill the form to participate in the extra curricular activities."],
            ("administration","office","authority"):["You can't visit office today, it's saturday.", "Administration office closes at 5'o clock in the evening.", "All authorities are busy today."]
        }

        random_reply = ("Mmmm","Oh, yes, I see","Tell me more","I don't know that","You should try working on this system.","Oh, my.","That is interesting.","Don't worry about that.")#response for query not matching any existing keys
        exit_key = ("bye","see you","exit","see ya","good bye","help")        #keys to exit from program
        breaking_connection = ["f","f","f","f","t","f","f","f","f","f"]         #breaking connection when list element is "t"
        
        while(True):
            exit_status = False                     #initializing exit status to false
            query = input("--->").lower()           #taking query input from user
            network_error = choice(breaking_connection)     #random choosing connection status
            if(network_error == "t"):
                print("*** NETWORK ERROR ***\n")
                print(f"Thanks, {usr_name}, for using PopChat. See you again soon!")
                break                                            #breaking from system due to connection break

            for i,j,k in query_reply.keys():
                if(i.lower() in query or j.lower() in query or k.lower() in query): #if elements in tuple is in query
                    print(choice(query_reply[(i,j,k)]))
                    break
            else:
                for i in exit_key:                                
                    if(i in query):
                        print(f"Thanks, {usr_name}, for using PopChat. See you again soon!")
                        exit_status = True
                        break                               #exit from system if user ask to exit
                else:
                    for j in random_reply:
                        print(choice(random_reply))         #showing random reply
                        break                               
            if(exit_status == True):
                break                                       #exiting from system 

if __name__ == "__main__":                          #when file is run as script
    chat_box()


