def import_data(datafile: str) -> list:
    returntable = []
    with open(datafile) as file:
        for line in file:
            line = line.rstrip("\r\n")
            first,second = line.split(",")
            elf1,elf2 = first.split("-"),second.split("-")
            elf1 = [int(x) for x in elf1]
            elf2 = [int(x) for x in elf2]
            returntable.append([elf1,elf2])
    return returntable

def determine_nested_list(elf1:list,elf2:list) -> bool:
    #case elf1 inner
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        return True
    #case elf2 inner
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        return True
    else:
        return False

def determine_overlapped_list(elf1:list,elf2:list) -> bool:
    elf1assignments = set([x for x in range(elf1[0],elf1[1]+1)])
    elf2assignments = set([x for x in range(elf2[0], elf2[1]+1)])
    if len(elf1assignments & elf2assignments) > 0:
        return True
    else:
        return False

def return_number_of_nested_elves(elflist:list) -> int:
    totalcount = 0
    for elfpair in elflist:
        if determine_nested_list(elfpair[0],elfpair[1]):
            totalcount += 1
    return totalcount

def return_number_of_overlapped_elves(elflist:list) -> int:
    totalcount = 0
    for elfpair in elflist:
        if determine_overlapped_list(elfpair[0],elfpair[1]):
            totalcount += 1
    return totalcount