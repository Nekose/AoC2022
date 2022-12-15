def import_data(datafile:str) -> list:
    commands = [[]]
    with open(datafile) as file:
        for line in file:
            value = line.strip("\r\n ")
            if value == "":
                commands.append([])
            else:
                commands[-1].append(value)
    return commands

class Monkey(object):

    def __init__(self,monkeydata) -> None:
        super().__init__()
        parseddata = self.monkeyparse(monkeydata)
        self.name,self.items,self.operation,self.test = parseddata

    def monkeyparse(self,monkeydata):
        name,items,operation,test = None,None,None,None
        #name
        name = monkeydata[0][-2]
        #items
        itemraw = monkeydata[1].split(": ")
        itemsplit = itemraw[1].split(",")
        items = [int(x) for x in itemsplit]
        #operation
        rawoperation = monkeydata[2].split(" ")
        operation = self.monkey_operation

        return name,items,operation,test

    def monkey_operation(self,var1,operation,var2):
        if operation == "+":
            return var1 + var2
        elif operation == "-":
            return var1 - var2
        elif operation == "/":
            return var1 / var2
        elif operation == "*":
            return var1 * var2
