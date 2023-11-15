#!/usr/bin/env python3
import collections
def tally(rows):
    """doc
    
    note: for tests use brackets for each match just like the following example
    
    rows = [["Allegoric Alaskans", "Blithering Badgers", "win"],
            ["Blithering Badgers", "Courageous Californians", "win"],
            ["Courageous Californians", "Allegoric Alaskans", "loss"]]
    """
    
    # home away result
    teams = collections.defaultdict(lambda: collections.Counter())
    for home, away, result in rows:
        if result == "win":
            teams[home]["W"] += 1
            teams[away]["L"] += 1
        elif result == "draw":
            teams[home]["D"] += 1
            teams[away]["D"] += 1
        elif result == "loss":
            teams[home]["L"] += 1
            teams[away]["W"] += 1
            
    for team, points in teams.items():
        points["P"] = 3 * points["W"] + points["D"]
    return teams

"""
if __name__ == "__main__":
    rows = [["Allegoric Alaskans", "Blithering Badgers", "win"],
               ["Blithering Badgers", "Courageous Californians", "win"],
               ["Courageous Californians", "Allegoric Alaskans", "loss"]]
    teams = tally(rows)
    print("{:<35} {:<1} {:<1} {:<1} {:<1} {:<1}".format('Team', '| MP', '|  W', '|  D', '|  L', '|  P'))
    for team, points in teams.items():
        print(f"{team:<30}      | MP |  {points['W']} |  {points['D']} |  {points['L']} |  {points['P']}")
"""
