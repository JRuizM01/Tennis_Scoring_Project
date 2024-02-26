# Tennis_Scoring_Project
Created a tennis scoring logic in Python.
The whole system is still updated and improved once in a while


**MATCH START**
The user can choose whether to customize the match or not:
- Add player names
- Play best of 1, 3 or 5 sets
- Play with Ads or No-Ads
- Track rally details
- Play with match log (Still under development)
- Track shot-by-shot (Still under development)
These are the defaults of a match setup:
- Player 1 and Player 2 are the assigned names
- Ad scoring, best of 1 set
- Matches will always have a tie-break when the scoring is 6-6 in the set
- Matches will always start after asking for the first server
    Servers will always switch after the end of a game

**DURING THE MATCH**
Tracking rally details:
- Stroke information
      Was the last shot hit a Forehand/Backhand/Volley/Ace)
- Rally end information
      Was the last shot hit a Winner/UnforcedError/ForcedError/DoubleFault
- The user input will then be added
Track shot-by-shot during the rally (FUTURE VERSION)
- Every shot during the rally can be tracked using @Jeff Sackmann's tracking method


**MATCH END**
- See total match time
- See statistics for each player
    Total Points and Games won
    Total Break Points won
    Shot Statistics (W/UF/F/Aces/DoubleFaults)
    Stroke Statistics (FH Winners/ BH Unforced Errors...)
  


