import matplotlib.pyplot as plt

class MLB_Player(object):

    #attributes
    lg_avgs = [.700, .721, .739, .750, .728]#2014-2018 ops avgs
    mlb_term = [] #years in the mlb
    player_stats = [] #list will hold players stats

    def __init__(self, fn):
        self.fn = fn #file name
        self.player_name = str(self.fn[:-4]) #takes players name by using the file name

        #method will read in the file and parse it 
    def read_in_data(self):
        with open(self.fn, 'r') as f:     # file is ready to be read in
            for line in f:                       # for loop is usual for reading in text data
                if not line.startswith('Year'):  # if the first element in the string does not start with 'Year' then it goes on an executes the following
                    line = line.replace('\n','') # replacing new line chars with null values 
                    L = line.split(',')          # creating a new list where the values get seperated at the comma
                    AGE = int(L[1])   # Age
                    TM = L[2]         # Team
                    G = int(L[4])     # Games
                    PA = int(L[5])    # Plate Apperences
                    AB = int(L[6])    # At Bats
                    Runs = int(L[7])  # Runs
                    HR = int(L[11])   # Home Runs
                    RBI = int(L[12])  # Runs Batted In
                    SB = int(L[13])   # Stolen Bases
                    CS = int(L[14])   # Caught Stealing
                    BB = int(L[15])   # Base on Balls
                    SO = int(L[16])   # StrikeOuts
                    BA = float(L[17]) # Batting Average
                    OPS = float(L[20])# On base percentage + Slugging
                    Awards = L[-1]    # Awards 
                    self.player_stats.append([AGE,TM,G,PA,AB,Runs,HR,RBI,SB,CS,BB,SO,BA,OPS,Awards]) #data setlist contains 15 elements
                                            # 0   1  2  3  4   5  6   7  8  9  10 11 12  13  14

    #come up with the mlb service years
    def years_in_mlb(self):
        
        len_of_service = len(self.player_stats) - 1
        curn_year = 2018 #most current year that has a season's worth of stats
        rookie_year = curn_year - len_of_service
        self.mlb_term.append(rookie_year)
        while rookie_year < curn_year:
            rookie_year += 1
            self.mlb_term.append(rookie_year)

    def plot_ops(self):

        players_season = [i+1 for i in range(len(self.player_stats))] #list containing seasons
        ops_carrer_stat = [ e[-2] for e in self.player_stats]

        x2 = [i for i in range(len(self.lg_avgs))]
        
        plt.plot(players_season,ops_carrer_stat, 'bo-', x2, self.lg_avgs, 'ro-')
        plt.ylim(0.65, 1.3)
        plt.legend([self.player_name, "League Average OPS"])
        plt.xlabel('Seasons')
        plt.ylabel('OPS')
        plt.grid()
        plt.show()
