import sys     
file_as_argument = sys.path[1:]             #Slicing CLI argument taking after 1st argument

class Teams:            
    #five class attributes
    counter = -1
    specific_countries = ""
    football_league = "Euro 2020 Group D"
    rugby_nation = "Six Nations 2021"
    argument = ""
    
    def __init__(self):             #Constructor function
        with open("results.csv","r") as file:  #Handling results file in reading mode     
            self.nested_league = []                  #empty list to contain nested league with scores
            self.extended_list_with_scores= []      #empty list to contain scores and countries
            for i in file:
                self.nested_league.append(i.strip().split(","))   #removing new line, splitting it      
            file.seek(0)                                                #cursor at starting position
            for i in file:
                self.extended_list_with_scores.extend(i.strip().split(","))     #removing new line, splitting and extending list        

    def manage_countries(self):
            countries = [self.extended_list_with_scores[i] for i in range(len(self.extended_list_with_scores)) if i%2==0]                                   #filtered only countries
            Teams.specific_countries = list(set(countries))         #unique countries
            Teams.argument = Teams.rugby_nation if file_as_argument == Teams.rugby_nation else Teams.football_league if len(Teams.specific_countries) == 4 else Teams.rugby_nation             #command line argument
            self.main_list = [[]]
            for i in range(0,len(Teams.specific_countries)-1):
                self.main_list += [[]]                      #Nested list length

    def score_board(self):
        Teams.counter += 1                #counter increment
        self.main_list[Teams.counter].append(Teams.specific_countries[Teams.counter])           #countries participated
        self.main_list[Teams.counter].append(self.extended_list_with_scores.count(Teams.specific_countries[Teams.counter]))                         #Number of played match
        (win,lose,draw,scored,against,diff,points) = (0,0,0,0,0,0,0)     #initialized to zero
        for i in self.nested_league:
            if((Teams.specific_countries[Teams.counter] == i[0] and int(i[1]) > int(i[3])) or (Teams.specific_countries[Teams.counter] == i[2] and int(i[3]) > int(i[1]))):
                win += 1                                                                #increment of winning chance
            if((Teams.specific_countries[Teams.counter] == i[0] and int(i[3]) > int(i[1])) or (Teams.specific_countries[Teams.counter] == i[2] and int(i[1]) > int(i[3]))):
                lose+=1                                         #increment of loss chance
            if((Teams.specific_countries[Teams.counter] == i[0] and int(i[1]) == int(i[3])) or (Teams.specific_countries[Teams.counter] == i[2] and int(i[3]) == int(i[1]))):
                draw+=1                                         #increment of draw chance
            if(Teams.specific_countries[Teams.counter] == i[0]):
                scored += int(i[1])                                  #increment goals for
                against += int(i[3])                                 #increment goals against
            elif(Teams.specific_countries[Teams.counter] == i[2]):
                scored += int(i[3])                                   #increment goals for
                against += int(i[1])                                  #increment goals against
                
        self.main_list[Teams.counter].extend([win,draw,lose,scored,against])       
        diff = (self.main_list[Teams.counter][5]) - (self.main_list[Teams.counter][6])      #difference of for and against
        points = (3 * self.main_list[Teams.counter][2] + self.main_list[Teams.counter][3])  #points obtained
        self.main_list[Teams.counter].extend([diff,points])                                    

    def sorting_rank(self):         #sorting the rank based on points 
        for i in range(0,len(self.main_list)-1):
            for j in range(i+1, len(self.main_list)):
                if(self.main_list[i][7] < self.main_list[j][7]):
                    tmp = self.main_list[i]
                    self.main_list[i] = self.main_list[j]
                    self.main_list[j] = tmp
                elif(self.main_list[i][7] == self.main_list[j][7]):     #if difference is same
                    if(self.main_list[i][5] < self.main_list[j][5]):
                        temp = self.main_list[i]
                        self.main_list[i] = self.main_list[j]
                        self.main_list[j] = temp

    def display_table(self):
        print(f"{Teams.argument} ","================",sep="\n")
        categories = ["\t  ","P","W","D","L","F","A","Diff","Pts"]
        for i in categories:
            print(f"{i:^10}",end="")
        print()
        for i in self.main_list:        #table display by looping
            for j in i:
                if(type(j)=="str"):
                    print(f"{j}")
                else:
                    print(f"{j:>9}",end = " ")
            print()
            
teams1 = Teams()            #instance of class Teams
teams1.manage_countries()       #calling the method
i = 0
while(i<len(Teams.specific_countries)):     #looping over and calling scoreboard
    teams1.score_board()
    i+=1
teams1.sorting_rank()                   #sorting rank
teams1.display_table()                  #display table

