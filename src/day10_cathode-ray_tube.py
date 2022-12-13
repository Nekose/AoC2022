import itertools

def import_data(datafile:str) -> list:
    commands = []
    with open(datafile) as file:
        for line in file:
            value = line.rstrip("\r\n")
            commands.append(value)
    return commands

def recieve_command(commands):
    cycle_dict = {}
    current_x = 1
    current_cycle = 1
    for command in commands:
        if command == "noop":
            cycle_dict[current_cycle] = current_x
            current_cycle += 1
        else:
            value = int(command.split(" ")[1])
            cycle_dict[current_cycle] = current_x
            current_cycle += 1
            cycle_dict[current_cycle] = current_x
            current_cycle += 1
            current_x += value
    return cycle_dict

def return_interesting_signals(dict,interesting_cycles):
    sum = 0
    for value in interesting_cycles:
        sum += (value * dict[value])
    return sum

def draw_image(data):
    output = []
    cycledata = [data[x] for x in range(1,241)]
    for pixel,sprite in zip(itertools.cycle(range(0,40)),cycledata):
        if pixel <= sprite +1 and pixel >= sprite -1:
            output.append("#")
        else:
            output.append(".")
    lines = [[],[],[],[],[],[]]
    for pos,val in enumerate(output):
        lines[pos//40] += val
    for line in output:
        print(line)


data = import_data("data/day10input.txt")
print(data)
testdict = recieve_command(data)
print(testdict)
print(return_interesting_signals(testdict,[20,60,100,140,180,220]))
for line in draw_image(testdict):
    print(line)