#!/usr/bin/env python3
# coding: latin-1
# ==========================================================================
# cd /home/jim/Documents/Python_Stuff/Tut_examples3_4/Edx2/Edx6
# cd /home/jim/Documents/Python_Stuff/Tut_examples3_4/Edx2/Edx6/ArjanCodes/examples-main_1-17-2025/examples-main/2024/pydantic_refresh
# python3 -m  March_madness3
#   or
# python3   March_madness3.py  "/home/jim/"  "example"
# python3   March_madness3.py
#   or
# pydoc3   March_madness3         # for documentation

# jcont = input("\n*** Enter to continue : [ok]") or "ok"
# ==========================================================================
#  March_madness3.py

import sys, os
import importlib
import subprocess
import webbrowser
import random
from dataclasses import dataclass

'''
subprocess.check_call('program <(command) <(another-command)',
                      shell=True, executable='/bin/bash')
subprocess.check_call('lscpu',
                      shell=True, executable='/bin/bash')
'''

# Get Header info from header_init in headerV (prefix_jw)
if sys.platform == 'ios':
    sys.path.insert(0, '/private/var/mobile/Containers/Shared/AppGroup/20F8FE41-CCEB-451E-9BB6-518237992DC2/Pythonista3/Documents/Jw_Utils_1')
    sys.path.insert(0, '/private/var/mobile/Containers/Shared/AppGroup/062764B7-2F0A-4107-8189-13F59EC37E24/Pythonista3/Documents')
else: 
    sys.path.insert(0, '/home/jim/Documents/Python_Stuff/Tut_examples3_4/Edx2/Edx6/relative_import-master/relative_imports') 
    sys.path.append('/home/jim/Documents/Python_Stuff/Tut_examples3_4/Edx2/Edx5')
    sys.path.insert(0, '/home/jim')

#import prefix_jw
try:
    import prefix_jw
    print(prefix_jw, '\n')
except Exception as e:     
    print('\n prefix_jw NOT imported!! \n')   
    print(' Error:', e)  
# =========================================================================
#  March_madness3.py

print('I Let Python Pick My March Madness Bracket - Bracket Simulation Tutorial by Corey Schafer')
print('\n video url: https://www.youtube.com/watch?v=4TFQD0ok5Ao')
print('\n github url: https://gist.github.com/CoreyMSchafer/27fcf83e5a0e5a87f415ff19bfdd2a4c')

@dataclass
class Team:
    name: str
    seed: int
    bracket: str

first_round = [
    # SOUTH
    (Team("Auburn", seed=1, bracket="South"), Team("Alabama ST/Saint Francis U", seed=16, bracket="South")),
    (Team("Louisville", seed=8, bracket="South"), Team("Creighton", seed=9, bracket="South")),
    (Team("Michigan", seed=5, bracket="South"), Team("UC San Deigo", seed=12, bracket="South")),
    (Team("Texas A&M", seed=4, bracket="South"), Team("Yale", seed=13, bracket="South")),
    (Team("Ole Miss", seed=6, bracket="South"), Team("San Deigo St/North Carolina", seed=11, bracket="South")),
    (Team("Iowa St.", seed=3, bracket="South"), Team("Lipscomb", seed=14, bracket="South")),
    (Team("Marquette", seed=7, bracket="South"), Team("New Mexico", seed=10, bracket="South")),
    (Team("Michigan St.", seed=2, bracket="South"), Team("Bryant", seed=15, bracket="South")),
    # WEST
    (Team("Florida", seed=1, bracket="West"), Team("Norfolk St.", seed=16, bracket="West")),
    (Team("UConn", seed=8, bracket="West"), Team("Oklahoma", seed=9, bracket="West")),
    (Team("Memphis", seed=5, bracket="West"), Team("Colorado St.", seed=12, bracket="West")),
    (Team("Maryland", seed=4, bracket="West"), Team("Grand Canyon", seed=13, bracket="West")),
    (Team("Missouri", seed=6, bracket="West"), Team("Drake", seed=11, bracket="West")),
    (Team("Texas Tech", seed=3, bracket="West"), Team("UNC Willington", seed=14, bracket="West")),
    (Team("Kansas", seed=7, bracket="West"), Team("Arkansas", seed=10, bracket="West")),
    (Team("St. John's", seed=2, bracket="West"), Team("Omaha", seed=15, bracket="West")),
    # EAST
    (Team("Duke", seed=1, bracket="East"), Team("America/Mount St Mary's", seed=16, bracket="East")),
    (Team("Mississippi St.", seed=8, bracket="East"), Team("Baylor", seed=9, bracket="East")),
    (Team("Oregon", seed=5, bracket="East"), Team("Liberty", seed=12, bracket="East")),
    (Team("Arizona", seed=4, bracket="East"), Team("Akron", seed=13, bracket="East")),
    (Team("BYU", seed=6, bracket="East"), Team("VCU", seed=11, bracket="East")),
    (Team("Wisconsin", seed=3, bracket="East"), Team("Montana", seed=14, bracket="East")),
    (Team("Saint Mary's", seed=7, bracket="East"), Team("Vanderbilt", seed=10, bracket="East")),
    (Team("Alabama", seed=2, bracket="East"), Team("Robert Morris", seed=15, bracket="East")),
    # MIDWEST
    (Team("Houston", seed=1, bracket="MidWest"), Team("SIU Edwardsville", seed=16, bracket="MidWest")),
    (Team("Gonzaga", seed=8, bracket="MidWest"), Team("Georgia", seed=9, bracket="MidWest")),
    (Team("ClemProvideson", seed=5, bracket="MidWest"), Team("McNeese", seed=12, bracket="MidWest")),
    (Team("Purdue", seed=4, bracket="MidWest"), Team("High Point", seed=13, bracket="MidWest")),
    (Team("Illinois", seed=6, bracket="MidWest"), Team("Texas/Xavier", seed=11, bracket="MidWest")),
    (Team("Kentucky", seed=3, bracket="MidWest"), Team("Troy", seed=14, bracket="MidWest")),
    (Team("UCLA", seed=7, bracket="MidWest"), Team("Utah St.", seed=10, bracket="MidWest")),
    (Team("Tennessee", seed=2, bracket="MidWest"), Team("Wofford", seed=15, bracket="MidWest")),
]

def simulate_game(team1, team2, file=None):
    team1_seed_weight = 1 / (team1.seed)
    team2_seed_weight = 1 / (team2.seed)

    # Uncomment the following lines to use a power for seed weighting (higher power means more weight to better seeds)
    # power = 1.1618
    # team1_seed_weight = 1 / (team1.seed**power)
    # team2_seed_weight = 1 / (team2.seed**power)

    # Convert to probabilities
    total = team1_seed_weight + team2_seed_weight
    team1_prob = 100 * (team1_seed_weight / total)
    team2_prob = 100 * (team2_seed_weight / total)

    # Get winner based on probabilities
    winner = random.choices([team1, team2], weights=[team1_prob, team2_prob], k=1)[0]

    result = (
        f"{team1.bracket}: \t {team1.name}-{team1.seed} ({team1_prob:.1f}%) vs {team2.bracket}: {team2.name}-{team2.seed} ({team2_prob:.1f}%),\t Winner: {winner.name}"
    )
    print(result)
    
    if file:
        file.write(result + "\n")

    return winner


def simulate_tournament(first_round, file=None):
    round_count = 1
    current_games = first_round
    winners = []
    while len(current_games) > 0:
        print(f"\n===== NEW ROUND  {round_count}  =====")
        if file:
            file.write(f"\n===== NEW ROUND  {round_count}  =====\n")
        round_count += 1
        round_winners = []

        for team1, team2 in current_games:
            winner = simulate_game(team1, team2, file)
            round_winners.append(winner)
            winners.append(winner)

        if len(round_winners) == 1:
            return winners, round_winners[0]

        next_round = []
        for i in range(0, len(round_winners), 2):
            next_round.append((round_winners[i], round_winners[i + 1]))

        current_games = next_round
    return winners, None


def save_winners_to_file(winners, filename="winners.txt"):
    with open(filename, "w") as file:
        for winner in winners:
            file.write(f"{winner.bracket}: {winner.name} (Seed: {winner.seed})\n")
    print(f"\nWinners saved to {filename}")


def main():
    """Main script execution."""
    print('\n Now in function "main") ...' ) 
    save = input("** Do you want to save the bracket results to a file? (yes/no): ").strip().lower()
    file = None
    if save == "yes":
        file = open("bracket_results.txt", "w")
        print('All results will be written to file "bracket_results.txt" ')

    winners, champion = simulate_tournament(first_round, file)
    print('\n', '=' *33)
    print(f"***  {champion.name} wins the tournament! ")
    print('=' *33)
    print()
    
    if file:
        file.close()


def generic_help() -> None:
    print('\n Now in function "generic_help") ...' ) 
    help()

def changes_made() -> None:
    print('\n Now in function "changes_made") ...' ) 
    print("""


    The key changes made:

    The simulate_game function now accepts an optional file parameter and writes the game result to the file if provided.
    The simulate_tournament function also accepts an optional file parameter and writes round headers to the file.
    The main function prompts the user if they want to save the bracket results to a file and opens the file for writing if the user responds "yes".
    The main function ensures the file is closed after the tournament simulation is complete.

    """)
    
#-------------------------------------------------------------
# M a i n   L i n e (added by jw)
#-------------------------------------------------------------
if __name__ == '__main__':  
    main()  
    #generic_help()
    
    print('\n video url: https://www.youtube.com/watch?v=4TFQD0ok5Ao')
    print('\n github url: https://gist.github.com/CoreyMSchafer/27fcf83e5a0e5a87f415ff19bfdd2a4c')
    
    import sys, os
    print('\n', sys.version_info)
    print ('\n  End of python ', sys.argv[0], '..... !!@)....\n')
    print( os.path.abspath(sys.argv[0]) )
