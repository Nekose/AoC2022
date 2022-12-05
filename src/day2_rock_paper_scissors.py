def score_match(elf:str,me:str) -> int:
    score = 0
    #calculate score for choice and determine match
    if me == "X": # I pick rock
        score += 1
        if elf == "A":
            return score + 3 #tie
        elif elf == "B":
            return score #lost
        elif elf == "C":
            return score + 6 #win

    elif me == "Y": #I pick paper
        score += 2
        if elf == "A":
            return score + 6 #win
        elif elf == "B":
            return score + 3 #tie
        elif elf == "C":
            return score #lost

    elif me == "Z": #I pick scissors
        score += 3
        if elf == "A":
            return score #lost
        elif elf == "B":
            return score + 6 #win
        elif elf == "C":
            return score + 3 #tie

def total_matches(datafile):
    runningtotal = 0
    with open(datafile) as file:
        for line in file:
            line = line.rstrip("\r\n")
            elf,me = line.split(" ")
            runningtotal += score_match(elf,me)
    return runningtotal


"""
Part Two
"""

def plan_match(elf:str,result:str):
    #x = lose, y = draw, z = win
    if elf == "A":
        if result == "X":
            return "Z"
        elif result == "Y":
            return "X"
        elif result == "Z":
            return "Y"
    elif elf == "B":
        if result == "X":
            return "X"
        elif result == "Y":
            return "Y"
        elif result == "Z":
            return "Z"
    elif elf == "C":
        if result == "X":
            return "Y"
        elif result == "Y":
            return "Z"
        elif result == "Z":
            return "X"

def total_strategy_matches(datafile):
    runningtotal = 0
    with open(datafile) as file:
        for line in file:
            line = line.rstrip("\r\n")
            elf, result = line.split(" ")
            me = plan_match(elf,result)
            runningtotal += score_match(elf, me)
    return runningtotal
