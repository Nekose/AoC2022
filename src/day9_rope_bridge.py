from typing import Tuple
def import_data(datafile:str) -> list:
    commands = []
    with open(datafile) as file:
        for line in file:
            line = line.rstrip("\r\n")
            dir, num = line.split(" ")
            commands.append((dir,int(num)))
    return commands

def generate_moves_with_n_knots(inputs, knots, debug=False, debuggridsize=10):
    knotslist = [[0,0] for _ in range(knots)]
    taillist = set()
    #move head
    for dir,num in inputs:
        for x in range(num):
            previous_position = knotslist[0][0],knotslist[0][1]
            if dir == "R":
                knotslist[0][0] += 1
            elif dir == "L":
                knotslist[0][0] -= 1
            elif dir == "U":
                knotslist[0][1] += 1
            elif dir == "D":
                knotslist[0][1] -= 1
            #check next nots
            for knot,coordinates in enumerate(knotslist):
                if knot == 0:
                    continue
                head = knotslist[knot-1][0],knotslist[knot-1][1]
                tail = coordinates[0],coordinates[1]
                tail = determine_tail_position(head,tail)
                knotslist[knot] = [tail[0],tail[1]]

            taillist.add((knotslist[-1][0],knotslist[-1][1]))
    #Debuggging
            if debug == True:
                debuggrid = []
                for _ in range(debuggridsize):
                    templist = []
                    for _ in range(debuggridsize):
                        templist.append(".")
                    debuggrid.append(templist)
                for pos,value in enumerate(knotslist):
                    debuggrid[value[1]][value[0]] = str(pos)
                for line in debuggrid:
                    print(line)
                print("")
    return len(taillist)

def determine_tail_position(head:Tuple[int,int],tail:Tuple[int,int]) -> Tuple[int,int]:
    headx,heady,tailx,taily = head[0],head[1],tail[0],tail[1]
    if headx == tailx and heady == taily:
        return head
    # deterime colume/row movement
    elif (headx == tailx and heady != taily) or (headx != tailx and heady == taily):
        if headx == tailx:
            if heady > taily:
                if heady - taily > 1:
                    taily += 1
            if taily > heady:
                if taily - heady > 1:
                    taily -= 1
        elif heady == taily:
            if headx > tailx:
                if headx - tailx > 1:
                    tailx += 1
            if tailx > headx:
                if tailx - headx > 1:
                    tailx -= 1
    # determine diagonal
    elif headx != tailx and heady != taily:
        if abs(headx - tailx) > 1 or abs(heady - tail[1]) > 1:
            if headx > tailx:
                tailx += 1
            elif headx < tailx:
                tailx -= 1
            if heady > taily:
                taily += 1
            elif heady < taily:
                taily -= 1

    return tailx,taily



