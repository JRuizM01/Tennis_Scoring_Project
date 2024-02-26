#To improve:

#Match setup + customization
    # 3rd set setper tie break
    
    #Graphical user interface
    
    #Problems:
        #When second serve is not in, it still asks for the shot
        #Wrong player is assigned the ace in the match log
        


import random
import time
import pandas as pd

#Make sure that the full dataframes get displayed
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

class TennisScoring:
    #tennis scoring system
    #Initial values
    def __init__(self):
        #match start
        self.p1_sets = 0
        self.p2_sets = 0
        self.p1_games = 5
        self.p2_games = 4
        self.p1_points = 0
        self.p2_points = 0
        self.set_scores = []
        
        #The target for now is 6 but can be changed in the future
        self.target_games = 6
        
        #Statistics
        self.p1_tot_pts = 0
        self.p2_tot_pts = 0
        self.p1_tot_games = 0
        self.p2_tot_games = 0
        self.p1_breaks = 0
        self.p2_breaks = 0
        
        # Player 1 serve stats
        self.p1_1st_serve_made = 0
        self.p1_tot_1st_serves = 0
        self.p1_2nd_serve_made = 0
        self.p1_tot_2nd_serves = 0
        self.p1_df = 0

        # Player 2 serve stats
        self.p2_1st_serve_made = 0
        self.p2_tot_1st_serves = 0
        self.p2_2nd_serve_made = 0
        self.p2_tot_2nd_serves = 0
        self.p2_df = 0
        
        #Player 1 shot stats
        self.p1_aces = 0
        self.p1_winners = 0
        self.p1_uf_errors = 0
        self.p1_f_errors = 0
        
        #Player 1 stroke stats
        #FH BH V    #W UF F
        #Player 1
        self.p1_fh_winners = 0
        self.p1_bh_winners = 0
        self.p1_v_winners = 0
        self.p1_fh_uf = 0
        self.p1_bh_uf = 0
        self.p1_v_uf = 0
        self.p1_fh_f = 0
        self.p1_bh_f = 0
        self.p1_v_f = 0
        
        #Player 2 shot stats
        self.p2_aces = 0
        self.p2_winners = 0
        self.p2_uf_errors = 0
        self.p2_f_errors = 0
        
        #Player 2 stroke stats
        self.p2_fh_winners = 0
        self.p2_bh_winners = 0
        self.p2_v_winners = 0
        self.p2_fh_uf = 0
        self.p2_bh_uf = 0
        self.p2_v_uf = 0
        self.p2_fh_f = 0
        self.p2_bh_f = 0
        self.p2_v_f = 0
    
        #Names
        self.p1_name = ''
        self.p2_name = ''
        
        self.ask_stroke = None
        self.second_serve_in = None
        
        #start the match with a random server
        self.current_server = 0
    
    def customize_match(self):
        self.ask_name()
        self.customize_length()
        self.customize_ads()
        self.track_serve_stats()
        self.track_shot_stats()
        if self.shot_stats_enabled == True:
            self.track_stroke_stats()
        self.match_log()
        self.current_server_func()
        
    
    def match_start(self):
        ask_customize = input("Would you like to customize the match? ") 
        if ask_customize == 'y':
            self.customize_match()
        else:
            print("Using default settings for the match (Best of 1 sets, with ad-scoring)")
            self.p1_name = 'Player 1'
            self.p2_name = 'Player 2'
            self.target_sets = 1    #Defualt length is best of 3
            self.ads_enabled = True     # Ad scoring is defualt
            self.serve_stats_enabled = False
            self.shot_stats_enabled = False
            self.stroke_stats_enabled = False
            self.match_log_enabled = False
            self.current_server = random.randint(1,2)   #random server is chosen
            
        print("Let the match begin")
        
        print(f'PLayer {tennis_game.current_server} will begin the match serving!\n')
        
    def customize_length(self):
        while True:
            match_length = input("Select match length, best of 1, 3 or 5 sets: ")
            if match_length == '1':
                self.target_sets = 1
                break
            elif match_length == '3':
                self.target_sets = 2
                break
            elif match_length == '5':
                self.target_sets = 3
                break
            else:
                print("The match length was invalid")
                continue
        print(f"Best of {match_length} sets was selected.")
        print(f"The first player to win {self.target_sets} sets wins")
            


    def current_server_func(self):
        while True:  
            serve_start = input("Who will serve first? Type player name or 1/2. If blank, random: ")
            if serve_start == '1' or serve_start == self.p1_name:
                self.current_server = 1
                return False
            elif serve_start == '2' or serve_start == self.p2_name:
                self.current_server = 2
                return False
            elif serve_start == '':
                self.current_server = random.randint(1,2)
                return False
            else:
                print('Invalid input, enter a player name, or leave blank')
                continue
    
    #first step, the program prints the initial score
    
    def ask_name(self):
        while True:
            ask_names = input("Would you like to assign names? (y/n) ")
            if ask_names == 'y':
                p1_name_input = input("What is Player 1's Name? ")
                if p1_name_input == '' or p1_name_input == ' ':
                    self.p1_name = 'Player 1'
                else:
                    self.p1_name = p1_name_input
                p2_name_input = input("What is Player 2's Name? ")
                if p2_name_input == '' or p2_name_input == ' ':
                    self.p2_name = 'Player 2'
                else:
                   self.p2_name = p2_name_input
                return False
             
            elif ask_names == 'n':
                print("No problem, default names were assigned")
                self.p1_name = 'Player 1'
                self.p2_name = 'Player 2'
                return False
            else:
                print("Invalid input. Please enter (y/n) ")
                continue
         
    #FORMAT NEEDS TO BE REWORKED    
    def print_score(self):
        data = {
            'Player': [f'{self.p1_name}*' if self.current_server == 1 else self.p1_name,
                       f'{self.p2_name}*' if self.current_server == 2 else self.p2_name],
            'Points': [self.point_to_score(self.p1_points), self.point_to_score(self.p2_points)],
            'Games': [self.p1_games, self.p2_games],
            'Sets': [self.p1_sets, self.p2_sets]   
        }
        
        df = pd.DataFrame(data)
        
        if self.p1_points >= 3 and self.p2_points >= 3:
            if self.p1_points == self.p2_points:
                df['Points'] = ['40', '40']
            elif self.p1_points > self.p2_points:
                df['Points'] = ['Adv', '40']
            elif self.p2_points > self.p1_points:
                df['Points'] = ['40', 'Adv']

        
        print(df)
        
        
    def start_match_time(self):
        self.timer_start = time.time()
        
    def end_match_time(self):
        self.timer_end = time.time()
    
    def calc_match_time(self):
        elapsed_time_seconds = tennis_game.timer_end - tennis_game.timer_start
        hours, remainder = divmod(int(elapsed_time_seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f'The match time was {hours} hours, {minutes} minutes, and {seconds} seconds')

    
    def new_point(self):
        self.point_won = input("Who won the point? (1 or 2): ")
           
        
        #When a player wins a point, a point is added to the game and to the overall match points
        if self.point_won == "1":
            self.p1_points += 1
            self.p1_tot_pts += 1
            
            #check if ads are enabled, if ads enabled is True, then check if its 3-3
            if self.p1_points == 3 and self.p2_points == 3:
                if self.ads_enabled:
                    self.handle_ads()
                
        elif self.point_won == "2":
            self.p2_points += 1
            self.p2_tot_pts += 1
            
            #check if ads are enabled, if ads enabled is True, then check if its 3-3
            if self.p1_points == 3 and self.p2_points == 3:
                if self.ads_enabled:
                    self.handle_ads()
        else:
            print("Invalid input. Please enter '1' or '2'.")
            return
        
        #If the tracking for serve stats is enable, do the whole logic every time
        if self.serve_stats_enabled == True:
            self.handle_track_serves()
        
        
        #Do not ask for shot stats if it's a double fault
        if self.shot_stats_enabled == True:
            if self.second_serve_in == 'n':
                pass
            else:
                self.handle_shot_stats()
        #Do not as for a stroke stat if the serve was an ace
                if self.ask_shot == 'a' and self.stroke_stats_enabled == True:
                    pass
                else:
                    self.handle_stroke_stats()
                  
        # When ads are enabled - play deauce if needed
        if self.ads_enabled == True:
            #handle deuce 
            if self.p1_points == 3 and self.p2_points == 3:
                self.handle_ads()
            #win a game by 2 points only
            #p1 wins the game
            if self.p1_points >= 4 and (self.p1_points - self.p2_points) >= 2:
                 self.handle_game_win(1) 
            #p2 wins the game
            if self.p2_points >= 4 and (self.p2_points - self.p1_points) >= 2:
                 self.handle_game_win(2) 
        
        #if ads are not enabled
        #p1 wins a game by
        if self.ads_enabled == False:
            if self.p1_points == 4:
                self.handle_game_win(1)
                
            #p2 wins the game
            elif self.p2_points == 4:
                self.handle_game_win(2)
        
        #When everything has been inputted, print the match_log
        if self.match_log_enabled == True:
            self.handle_match_log()
            
        
        #Match finished when a player reaches the target sets
        if self.p1_sets == self.target_sets or self.p2_sets == self.target_sets:
            
            #Print match winner
            if self.p1_sets == self.target_sets:
                print(f"{self.p1_name} wins the match!")
            if self.p2_sets == self.target_sets:
                print(f"{self.p2_name} wins the match!")
                
            print(f"The match score was {' '.join(self.set_scores)}")
            self.print_statistics()
            return True
        return False
    
    def switch_server(self):
        self.current_server = 3 - self.current_server
    
    def handle_game_win(self, player):
        #when a game is won, the following happens
        self.p1_points = 0
        self.p2_points = 0
        
        #Increment games won for the player that won the game
        #player 1 wins the game
        if player == 1:
            self.p1_games += 1
            self.p1_tot_games += 1
            #if player 2 was serving, that's a break
            if self.current_server == 2:
                self.p1_breaks += 1
                print("Break for player 1!")
        else:
            self.p2_games += 1
            self.p2_tot_games += 1
            if self.current_server == 1:
                self.p2_breaks += 1
                print("Break for player 2!")
            
        #Switch server
        self.switch_server()
        
        #check if there is a set win
        if self.p1_games in {6, 7} and self.p1_games - self.p2_games >= 2:
            self.handle_set_win(1)          
        if self.p2_games in {6, 7} and self.p2_games - self.p1_games >= 2:
            self.handle_set_win(2)
            
         # check if there is a tiebreaker    
        if self.p1_games == 6 and self.p2_games == 6:
            self.play_tiebreaker()
        
    
    def handle_set_win(self, player):
        self.set_scores.append(f"{self.p1_games}/{self.p2_games}")
        print(f"Player {player} won the set {' '.join(self.set_scores)}")    #({min(self.p1_tb_pts, self.p2_tb_pts) if min(self.p1_games, self.p2_games) == 6 else ''})
        self.current_server = 3 - player  # Switch between 1 and 2
        self.p1_games = 0
        self.p2_games = 0
        if player == 1:
            self.p1_sets += 1
        else:
            self.p2_sets += 1
    
    #def handle_match_win(self, player):
    
    def set_winner(self):
        return (
            (self.p1_games >= 7 and self.p1_games - self.p2_games >= 2) or
            (self.p2_games >= 7 and self.p2_games - self.p1_games >= 2)
        )
    
    def play_on_set(self):
        print("Play on set! First person to 7 games wins")
        while not self.set_winner():
            self.print_score()
            self.new_point()
            
    
    def play_tiebreaker(self):
            print("The score in the set is 6-6, The set will be decided with a Tie_break!")
            self.p1_tb_pts = 0
            self.p2_tb_pts = 0
            while True:
                print(f"The current Tie-Break score is {self.p1_tb_pts}-{self.p2_tb_pts}")
                tb_pt_won = input("Who won the TieBreak point? ")
                if tb_pt_won == "1":
                    self.p1_tb_pts += 1
                elif tb_pt_won == "2":
                    self.p2_tb_pts += 1
                else:
                    print("Wrong input, please enter 1 or 2")
                    continue
                
                #ENDING THE TIE BREAK
                #P1 wins
                if self.p1_tb_pts >= 7 and self.p1_tb_pts - self.p2_tb_pts >= 2:
                    print(f"{self.p1_name} wins the Tie-Break {self.p1_tb_pts}/{self.p2_tb_pts} and the Set!")
                    self.p1_games += 1
                    self.handle_set_win(1)
                    break
                    
                #P2 wins
                elif self.p2_tb_pts >= 7 and self.p2_tb_pts - self.p1_tb_pts >= 2:
                    print(f"{self.p2_name} wins the Tie-Break {self.p1_tb_pts}/{self.p2_tb_pts} and the Set!")
                    self.p2_games += 2
                    self.handle_set_win(2)
                    break
                
                
    def customize_ads(self):
        while True:
            #asking the player to set up the match with Ad or No Ad scoring
            ask_play_with_ads = input("Would you like to play with Ads? y/n ")
            if ask_play_with_ads == 'y':
                print('Ad scoring selected')
                #The function ads enabled keeps track if game is with ads or not
                self.ads_enabled = True
                self.handle_ads() #call handle ads if ads are enabled
                return False
            elif ask_play_with_ads == 'n':
                print('No-ad scoring selected')
                self.ads_enabled = False
                return False
            else:
                continue
                
    def handle_ads(self): 
        if self.p1_points >= 3 and self.p2_points >= 3:
            if self.p1_points == self.p2_points:
                print("Deuce!")
            elif self.p1_points > self.p2_points:
                print(f"Adv {self.p1_name}")
            elif self.p2_points > self.p1_points:
                print(f"Adv {self.p2_name}")    
                
                
        # Restart here       
    def track_serve_stats(self):
        ask_serve_stats = input("Do you want to keep track of serve statistics? (y/n): ")
        
        if ask_serve_stats.lower() == 'y':
            self.serve_stats_enabled = True
            print("Serve statistics tracking is enabled.")

        elif ask_serve_stats.lower() == 'n':
            self.serve_stats_enabled = False
            print("Serve statistics tracking is disabled.")
            
    def handle_track_serves(self):
        while True:
            if self.serve_stats_enabled == True:
                first_serve_in = input(f"Did {self.p1_name if self.current_server == 1 else self.p2_name} make the first serve in? (y/n): ")
                #Track first serve
                if first_serve_in == 'y':
                    if self.current_server == 1:
                        self.p1_1st_serve_made += 1
                        self.p1_tot_1st_serves += 1
                    else:
                        self.p2_1st_serve_made += 1
                        self.p2_tot_1st_serves += 1
                    break
                elif first_serve_in == 'n':
                    self.second_serve_in = input(f"Did {self.p1_name if self.current_server == 1 else self.p2_name} make the second serve in? (y/n): ") 
                    if self.second_serve_in == 'y':
                        if self.current_server == 1:
                        #If misses first serve, he still has a 1st serve served
                            self.p1_tot_1st_serves += 1
                            self.p1_2nd_serve_made += 1
                            self.p1_tot_2nd_serves += 1
                        else:
                            self.p2_tot_1st_serves += 1
                            self.p2_2nd_serve_made += 1
                            self.p2_tot_2nd_serves += 1
                        break
                    elif self.second_serve_in == 'n':
                        if self.current_server == 1:
                            self.p1_tot_1st_serves += 1
                            self.p1_tot_2nd_serves += 1
                            self.p1_df += 1
                        else:
                            self.p2_tot_1st_serves += 1
                            self.p2_tot_2nd_serves += 1
                            self.p2_df += 1
                        break
                    else:
                        print("Invalid input. Please enter y or n.")
                else:
                    print("Invalid input. Please enter y or n.")
        
    def track_shot_stats(self):
        ask_shot_stats = input("Do you want to keep track of the shot statistics? (y/n): ")
        
        if ask_shot_stats == 'y':
            self.shot_stats_enabled = True
            print("Shot statistics tracking is enabled.")
            
        elif ask_shot_stats == 'n':
            self.shot_stats_enabled = False
            print("Shot statistics tracking is disabled.")
    
    def handle_shot_stats(self):
        if self.shot_stats_enabled == True:
            while True:
                self.ask_shot = input("How did the point end? (W/UF/F/A) ")
                if self.point_won == '1':
                    if self.ask_shot == 'w':
                        self.p1_winners += 1
                        break
                    #if p1 wins the point and the input is UF or F, that means that Player 2 did the UF
                    elif self.ask_shot == 'uf':
                        self.p2_uf_errors += 1
                        break
                    elif self.ask_shot == 'f':
                        self.p2_f_errors += 1
                        break
                    elif self.ask_shot == 'a':
                        self.p1_aces += 1
                        break
                    else:
                        print("Invalid Input")

                elif self.point_won == '2':
                    if self.ask_shot == 'w':
                        self.p2_winners += 1
                        break
                    elif self.ask_shot == 'uf':
                        self.p1_uf_errors += 1
                        break
                    elif self.ask_shot == 'f':
                        self.p1_f_errors += 1
                        break
                    elif self.ask_shot == 'a':
                        self.p2_aces += 1
                        break
                    else:
                        print("Invalid input")  
    
    def track_stroke_stats(self):
        #FH BH V    #W UF F
        ask_stroke_stats = input("Would you like to keep track of stroke stats? (y/n) ")
        if ask_stroke_stats == 'y':
            print("Stroke stats are enabled")
            self.stroke_stats_enabled = True
        elif ask_stroke_stats == 'n':
            print("Stroke stats are disabled")
            self.stroke_stats_enabled = False
            
    def handle_stroke_stats(self):
        self.ask_stroke = input("What stroke did the point end with? (FH/BH/V) ")
        if self.point_won == '1':
            if self.ask_shot == 'w' and self.ask_stroke == 'fh':
                self.p1_fh_winners += 1
            #if the shot is won by player 1, it means that p2 made the uf
            elif self.ask_shot == 'uf' and self.ask_stroke == 'fh':
                self.p2_fh_uf += 1
            elif self.ask_shot == 'f' and self.ask_stroke == 'fh':
                self.p2_fh_f += 1
            elif self.ask_shot == 'w' and self.ask_stroke == 'bh':
                self.p1_bh_winners += 1
            elif self.ask_shot == 'uf' and self.ask_stroke == 'bh':
                self.p2_bh_uf += 1
            elif self.ask_shot == 'f' and self.ask_stroke == 'bh':
                self.p2_bh_f += 1
            elif self.ask_shot == 'w' and self.ask_stroke == 'v':
                self.p1_v_winners += 1
            elif self.ask_shot == 'uf' and self.ask_stroke == 'v':
                self.p2_v_uf += 1
            elif self.ask_shot == 'f' and self.ask_stroke == 'v':
                self.p2_v_f += 1
        elif self.point_won == '2':
            if self.ask_shot == 'w' and self.ask_stroke == 'fh':
                self.p2_fh_winners += 1
            elif self.ask_shot == 'uf' and self.ask_stroke == 'fh':
                self.p1_fh_uf += 1
            elif self.ask_shot == 'f' and self.ask_stroke == 'fh':
                self.p1_fh_f += 1
            elif self.ask_shot == 'w' and self.ask_stroke == 'bh':
                self.p2_bh_winners += 1
            elif self.ask_shot == 'uf' and self.ask_stroke == 'bh':
                self.p1_bh_uf += 1
            elif self.ask_shot == 'f' and self.ask_stroke == 'bh':
                self.p1_bh_f += 1
            elif self.ask_shot == 'w' and self.ask_stroke == 'v':
                self.p2_v_winners += 1
            elif self.ask_shot == 'uf' and self.ask_stroke == 'v':
                self.p1_v_uf += 1
            elif self.ask_shot == 'f' and self.ask_stroke == 'v':
                self.p1_v_f += 1
        
    def match_log(self):
        ask_match_log = input("Would you like to have an updated match log? (y/n) ")
        if ask_match_log == 'y':
            print('Match log is enabled')
            self.match_log_enabled = True
        elif ask_match_log == 'n':
            print('Match log is disabled')
            self.match_log_enabled = False
            
    def handle_match_log(self):
        if self.match_log_enabled == True:
            if self.ask_shot == 'w':
                print(f"{self.p1_name if self.point_won == 1 else self.p2_name} won the point with a {self.ask_stroke} winner")
            elif self.ask_shot == 'a':
                print(f"{self.p1_name if self.point_won == 1 else self.p2_name} won the point with an ace")
            elif self.ask_shot == 'uf':
                 print(f"{self.p2_name if self.point_won == 1 else self.p1_name} lost the point with a {self.ask_stroke} unforced error")
            elif self.ask_shot == 'f':
                print(f"{self.p2_name if self.point_won == 1 else self.p1_name} lost the point with a {self.ask_stroke} forced error")
            elif self.second_serve_in() == 'n':
                print(f"{self.p2_name if self.point_won == 1 else self.p1_name} lost the point with a double fault")

            
            
    def point_to_score(self, points):
        if points == 0:
            return "0"
        if points == 1:
            return "15"
        if points == 2:
            return "30"
        if points == 3:
            return "40"
        
    def print_statistics(self):
        #Statistics:
        if self.serve_stats_enabled == False and self.shot_stats_enabled == False:
            stats = {
                'Player': [f'{self.p1_name}', f'{self.p2_name}'],
                'Total Points': [self.p1_tot_pts, self.p2_tot_pts],
                'Total Games': [self.p1_tot_games, self.p2_tot_games],
                'Total Breaks': [self.p1_breaks, self.p2_breaks]
                }
            
        elif self.serve_stats_enabled == True and self.shot_stats_enabled == False: 
            stats = {
                'Player': [f'{self.p1_name}', f'{self.p2_name}'],
                'Total Points': [self.p1_tot_pts, self.p2_tot_pts],
                'Total Games': [self.p1_tot_games, self.p2_tot_games],
                'Total Breaks': [self.p1_breaks, self.p2_breaks],
                '1st serve in': [f'{self.p1_1st_serve_made}/{self.p1_tot_1st_serves}', f'{self.p2_1st_serve_made}/{self.p2_tot_1st_serves}'],
                '1st serve %': [f'{(self.p1_1st_serve_made/self.p1_tot_1st_serves)*100:.2f}%', f'{(self.p2_1st_serve_made/self.p2_tot_1st_serves)*100:.2f}%'],
                '2nd_serve in':[f'{self.p1_2nd_serve_made}/{self.p1_tot_2nd_serves}', f'{self.p2_2nd_serve_made}/{self.p2_tot_2nd_serves}'],
                '2nd serve %': [f'{(self.p1_2nd_serve_made/self.p1_tot_2nd_serves)*100:.2f}%', f'{(self.p2_2nd_serve_made/self.p2_tot_2nd_serves)*100:.2f}%'],
                'Double Faults': [self.p1_df, self.p2_df]
                }
        
        elif self.serve_stats_enabled == False and self.shot_stats_enabled == True:
            stats = {
                'Player': [f'{self.p1_name}', f'{self.p2_name}'],
                'Total Points': [self.p1_tot_pts, self.p2_tot_pts],
                'Total Games': [self.p1_tot_games, self.p2_tot_games],
                'Total Breaks': [self.p1_breaks, self.p2_breaks],
                'Winners': [self.p1_winners, self.p2_winners],
                'Unforced Errors': [self.p1_uf_errors, self.p2_uf_errors],
                'Forced Errors': [self.p1_f_errors, self.p2_f_errors]
                }
            
            
        elif self.serve_stats_enabled == True and self.shot_stats_enabled == True and self.stroke_stats_enabled == False:
            stats = {
                'Player': [f'{self.p1_name}', f'{self.p2_name}'],
                'Total Points': [self.p1_tot_pts, self.p2_tot_pts],
                'Total Games': [self.p1_tot_games, self.p2_tot_games],
                'Total Breaks': [self.p1_breaks, self.p2_breaks],
                '1st serve in': [f'{self.p1_1st_serve_made}/{self.p1_tot_1st_serves}', f'{self.p2_1st_serve_made}/{self.p2_tot_1st_serves}'],
                '1st serve %': [f'{(self.p1_1st_serve_made/self.p1_tot_1st_serves)*100:.2f}%' if self.p1_tot_1st_serves != 0 else 'N/A',
                                f'{(self.p2_1st_serve_made/self.p2_tot_1st_serves)*100:.2f}%' if self.p2_tot_1st_serves != 0 else 'N/A'],
                '2nd_serve in':[f'{self.p1_2nd_serve_made}/{self.p1_tot_2nd_serves}', f'{self.p2_2nd_serve_made}/{self.p2_tot_2nd_serves}'],
                '2nd serve %': [f'{(self.p1_2nd_serve_made/self.p1_tot_2nd_serves)*100:.2f}%' if self.p1_tot_2nd_serves != 0 else 'N/A',
                                f'{(self.p2_2nd_serve_made/self.p2_tot_2nd_serves)*100:.2f}%' if self.p2_tot_2nd_serves != 0 else 'N/A'],
                'Double Faults': [self.p1_df, self.p2_df],
                'Winners': [self.p1_winners, self.p2_winners],
                'Unforced Errors': [self.p1_uf_errors, self.p2_uf_errors],
                'Forced Errors': [self.p1_f_errors, self.p2_f_errors]
                }
        
        elif self.serve_stats_enabled == True and self.shot_stats_enabled == True and self.stroke_stats_enabled == True:
            stats = {
                'Player': [f'{self.p1_name}', f'{self.p2_name}'],
                'Total Points': [self.p1_tot_pts, self.p2_tot_pts],
                'Total Games': [self.p1_tot_games, self.p2_tot_games],
                'Total Breaks': [self.p1_breaks, self.p2_breaks],
                'Aces': [self.p1_aces, self.p2_aces],
                '1st serve in': [f'{self.p1_1st_serve_made}/{self.p1_tot_1st_serves}', f'{self.p2_1st_serve_made}/{self.p2_tot_1st_serves}'],
                '1st serve %': [f'{(self.p1_1st_serve_made/self.p1_tot_1st_serves)*100:.2f}%' if self.p1_tot_1st_serves != 0 else 'N/A',
                                f'{(self.p2_1st_serve_made/self.p2_tot_1st_serves)*100:.2f}%' if self.p2_tot_1st_serves != 0 else 'N/A'],
                '2nd_serve in':[f'{self.p1_2nd_serve_made}/{self.p1_tot_2nd_serves}', f'{self.p2_2nd_serve_made}/{self.p2_tot_2nd_serves}'],
                '2nd serve %': [f'{(self.p1_2nd_serve_made/self.p1_tot_2nd_serves)*100:.2f}%' if self.p1_tot_2nd_serves != 0 else 'N/A',
                                f'{(self.p2_2nd_serve_made/self.p2_tot_2nd_serves)*100:.2f}%' if self.p2_tot_2nd_serves != 0 else 'N/A'],
                'Double Faults': [self.p1_df, self.p2_df],
                'Winners': [self.p1_winners, self.p2_winners],
                'Unforced Errors': [self.p1_uf_errors, self.p2_uf_errors],
                'Forced Errors': [self.p1_f_errors, self.p2_f_errors],
                'FH Winners': [self.p1_fh_winners, self.p2_fh_winners],
                'FH UF Errors': [self.p1_fh_uf, self.p2_fh_uf],
                'FH F Errors': [self.p1_fh_f, self.p2_fh_f],
                'BH Winners': [self.p1_bh_winners, self.p2_bh_winners],
                'BH UF Errors': [self.p1_bh_uf, self.p2_bh_uf],
                'BH F Errors': [self.p1_bh_f, self.p2_bh_f],
                'V Winners': [self.p1_v_winners, self.p2_v_winners],
                'V UF Errors': [self.p1_v_uf, self.p2_v_uf],
                'VF Errors': [self.p1_v_f, self.p2_v_f],
                }
        
        stats_df = pd.DataFrame(stats)
        stats_df_transposed = stats_df.transpose()
        
        print(stats_df_transposed)
        
 
    
tennis_game = TennisScoring()

#print and assign the first server
tennis_game.match_start()
tennis_game.start_match_time()

print('This is the current score')
while True:
    tennis_game.print_score()
    if tennis_game.new_point():
        break
    
#end match time
tennis_game.end_match_time()
#calculate match time
tennis_game.calc_match_time()


    
    