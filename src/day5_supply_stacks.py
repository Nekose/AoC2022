from typing import Tuple
def import_data(datafile: str) -> Tuple[list,list]:
    rawdata = []
    with open(datafile) as file:
        for line in file:
            line = line.rstrip("\r\n")
            rawdata.append(line)
    startingpositions = rawdata[:8]
    instructions = rawdata[10:]
    return startingpositions,instructions

def build_stacks(startingpositions:list) -> list:
    stacks = [[] for _ in range(9)] #generate empty lists
    flippedstartingpositions = startingpositions[::-1]
    for row in flippedstartingpositions:
        for stacknum,col in zip(range(0,9),range(1,34,4)):
            if row[col] != " ":
                stacks[stacknum].append(row[col])
    return stacks

def make_moves_9000(stacks:list, instructions:list) -> list:
    for line in instructions:
        line = line.split(" ")
        numcrates,origin,destination = int(line[1]),int(line[3])-1,int(line[5])-1
        for _ in range(numcrates):
            crate = stacks[origin].pop()
            stacks[destination].append(crate)
    return stacks

def make_moves_9001(stacks:list, instructions:list) -> list:
    for line in instructions:
        line = line.split(" ")
        numcrates, origin, destination = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
        crane = []
        for _ in range(numcrates):
            crate = stacks[origin].pop()
            crane.append(crate)
        for _ in range(numcrates):
            stacks[destination].append(crane.pop())
    return stacks

def return_tops(stacks:list) -> str:
    returnstring = ""
    for col in stacks:
        if len(col) > 0:
            returnstring += col[-1]
    return returnstring

def process(datafile: str="",method: str="9000"):
    startingpositions,instructions = import_data(datafile)
    stacks = build_stacks(startingpositions)
    if method == "9000":
        stacks = make_moves_9000(stacks,instructions)
    elif method == "9001":
        stacks = make_moves_9001(stacks,instructions)
    return return_tops(stacks)
