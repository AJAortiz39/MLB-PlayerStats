# MAIN
#import numpy as np
#import matplotlib.pyplot as plt

from MLB_Player_Object import MLB_Player



def main():
    file_name = input(" Please enter name of the file\n ") #asking user to choose their file(player file)
    #print(in_player)
    player = MLB_Player(file_name) 
    player.read_in_data()
    player.years_in_mlb()
    
    #prompts user to select 1 of the following options
    print("\n S : Stats\n P : Plot")
    option = input(" Please choose an option.\n ")
    option = option.lower() # converts option into lowercase letter to avoid input error
    #if user selets to show player's stats
    if option == "s":
        #shows Players Stats
        #want to show years 
        print('\n',player.mlb_term) # prints years that the player has been in mlb service
        show = int(input(" Please select player's MLB term\n ")) #user selects the year of which stats to be shown
        
        for year in player.mlb_term: #looping through the years of mlb serive
            if year == show: #if the year chosen matches the year in the loop
                index_of_year = player.mlb_term.index(year)
                #print(player.player_stats[index_of_year])
                print("\n Showing %i Stats for %s \n" % (show,player.player_name))
                print(" Age: %i, Team: %s, Games: %i, Plate Appearences: %i, At Bats: %i, Runs: %i, Home Runs: %i, Runs Batted In: %i, Stolen Bases: %i" % (player.player_stats[index_of_year][0], player.player_stats[index_of_year][1], player.player_stats[index_of_year][2],player.player_stats[index_of_year][3],player.player_stats[index_of_year][4],player.player_stats[index_of_year][5],player.player_stats[index_of_year][6], player.player_stats[index_of_year][7],player.player_stats[index_of_year][8]))
                print(" Caught Stealing: %i, Base on Balls: %s, Strikeouts: %i, Batting Average: %f, On Base Plus Slugging: %f, Awards: %s" % (player.player_stats[index_of_year][9], player.player_stats[index_of_year][10], player.player_stats[index_of_year][11],player.player_stats[index_of_year][12],player.player_stats[index_of_year][13],player.player_stats[index_of_year][14]))
                                  
                      
                    
        
        
    elif option == "p":
        #Will Show Player's plot options
        pt = input(" Select stat to be compared vs MLB average.\n OPS\n Homeruns\n ")
        pt = pt.lower()
        if pt == 'ops':
            player.plot_ops()
        if pt == "homeruns":
            player.plot_hrs()
        
    

    
main()
