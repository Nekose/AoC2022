#Oh no, its recursion

sizedict = {}


def import_data(datafile: str) -> str:
    commandprompts = []
    with open(datafile) as file:
        for line in file:
            commandprompts.append(line.rstrip("\r\n"))
        return commandprompts

def build_file_tree(commandpromptlist: list) -> "Folder":
    top = Folder("Top", "root")
    cwd = top
    for command in commandpromptlist:
        commandphrases = command.split(" ")
        if commandphrases[0] == "$": #detect input command
            if commandphrases[1] == "cd": #change to subfolder
                if commandphrases[2] == r"/":
                    cwd = top
                elif commandphrases[2] == "..":
                    cwd = cwd.parentfolder
                else:
                    for folder in cwd.subfolders:
                        if folder.name == commandphrases[2]:
                            cwd = folder
        elif commandphrases[0] == "dir": #add new folders
            cwd.add_folder(commandphrases[1])
        else:
            cwd.add_file(Elf_File(commandphrases[1],int(commandphrases[0]))) #add new files
    return top

class Folder(object):
    def __repr__(self):
        return f"Folder called '{self.name}' containing {len(self.files)} files, {len(self.subfolders)} subfolders named {[folder.name for folder in self.subfolders]}," \
               f"and total files size of {self.totalfilesize} elfobytes."

    def __init__(self,name,parentfolder):
        self.parentfolder = parentfolder
        self.subfolders = []
        self.files = []
        self.totalfilesize = 0
        self.name = name

    def add_file(self,file):
        self.files.append(file)
        self._update_totalfilesize()

    def add_folder(self,name):
        for folder in self.subfolders:
            if folder.name == name:
                raise DuplicateFolderName
        self.subfolders.append(Folder(name,self))
        self._update_totalfilesize()

    def _update_totalfilesize(self):
        self.totalfilesize = sum(x.filesize for x in self.files) + sum(folder.totalfilesize for folder in self.subfolders)
        global sizedict
        sizedict[self.name] = self.totalfilesize

    def report_sizes(self):
        global sizedict
        return sizedict


class Elf_File(object):
    def __init__(self, name, size):
        self.filesize = size
        self.name = name
    def __int__(self):
        return self.filesize
    def __repr__(self):
        return f"File {self.name} - {self.filesize} elfobytes"

class DuplicateFolderName(Exception):
    pass

class UnknownFolderName(Exception):
    pass