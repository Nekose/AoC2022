def maxcal(datafile):
    #Collect values from data text file
    outputtable = []
    with open(datafile) as file:
        for line in file:
            outputtable.append(line.replace("\n",""))
    #create list of sums for each elf
    sumtable = []
    runningsum = 0
    for value in outputtable:
        if value == "":
            sumtable.append(runningsum)
            runningsum = 0
        else:
            runningsum += int(value)
    #return max of table
    return max(sumtable)

def top3cal(datafile):
    #Collect values from data text file
    outputtable = []
    with open(datafile) as file:
        for line in file:
            outputtable.append(line.replace("\n",""))
    #create list of sums for each elf
    sumtable = []
    runningsum = 0
    for value in outputtable:
        if value == "":
            sumtable.append(runningsum)
            runningsum = 0
        else:
            runningsum += int(value)
    sumtable.sort(reverse=True)
    #find sum of top 3
    return sumtable[0] + sumtable[1] + sumtable[2]