def import_data(datafile:str) -> list:
    commands = []
    with open(datafile) as file:
        for line in file:
            line = line.rstrip("\r\n")
            dir, num = line.split(" ")
            commands.append((dir,int(num)))
    return commands

def generate_moves(inputs):
    # x,y = 0,0
    tailvisited = [(0,0)]
    headvisited = [(0,0)]
    head = [0,0]
    tail = [0,0]
    for dir,num in inputs:
        for x in range(num):
            if dir == "R":
                head[0] += 1
            elif dir == "L":
                head[0] -= 1
            elif dir == "U":
                head[1] += 1
            elif dir == "D":
                head[1] -= 1
            headvisited.append((head[0],head[1]))
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                tail[0],tail[1] = headvisited[-2]
                tailvisited.append((tail[0],tail[1]))
    return tailvisited


