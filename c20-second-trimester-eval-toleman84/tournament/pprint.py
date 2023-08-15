#!/usr/bin/env python3
"""doc"""
def pprint(teams):
    print("{:<35} {:<1} {:<1} {:<1} {:<1} {:<1}".format('Team', '| MP', '|  W', '|  D', '|  L', '|  P'))
    for team, points in teams.items():
        print(f"{team:<30}      | MP |  {points['W']} |  {points['D']} |  {points['L']} |  {points['P']}")
