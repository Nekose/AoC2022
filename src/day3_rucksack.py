def import_data(datafile: str) -> list:
    returntable = []
    with open(datafile) as file:
        for line in file:
            line = line.rstrip("\r\n")
            returntable.append(line)
    return returntable

def scoreitem(item:str) -> int:
    scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return scores.index(item) + 1

def splitandcompare(contents:str) -> str:
    matched = ""
    firsthalf = set(contents[:len(contents)//2])
    secondhalf = set(contents[len(contents)//2:])
    for value in firsthalf:
        if value in secondhalf:
            matched += value
    return matched

def checkpacks(listofpacks: list) -> int:
    finalscore = 0
    for pack in listofpacks:
        duplicates = splitandcompare(pack)
        finalscore += sum([scoreitem(x) for x in duplicates])
    return finalscore

def determinebadgetype(listofpacks: list) -> str:
    badgesetlist = []
    for y in range(0,len(listofpacks),3):
        a = set(listofpacks[y])
        b = set(listofpacks[y + 1])
        c = set(listofpacks[y + 2])
        badgesetlist.append(a & b & c)
    return sum(scoreitem(x.pop()) for x in badgesetlist)