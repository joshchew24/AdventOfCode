import sys
import re

cd_command = "\$\scd\s"

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent: Dir = parent
        self.total_size = 0
        self.child_dirs: dict[str: Dir] = {}
        self.files: list[File] = []

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name

    def get_solution_size(self):
        soln = 0
        if self.total_size < 100000:
            soln += self.total_size
        for child in self.child_dirs.values():
            soln += child.get_solution_size()
        return soln

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return self.name

def read_input(mode):
    lines = []
    with open(f"{mode}.txt") as input:
        for line in input:
            lines.append(line.strip())
    return lines

def solve(input):
    home = Dir("home", None)
    cwd = home
    for line in input:
        if line[0] == "$":
            if line[2:4] == "cd":
                if line[5:7] == "..":
                    cwd.parent.total_size += cwd.total_size
                    cwd = cwd.parent
                    continue
                trash, dir = re.split(cd_command, line)
                cwd = cwd.child_dirs[dir]
                continue
            else: # ls
                continue
        if line[0:3] == "dir":
            dir_name = line[4:]
            new_dir = Dir(dir_name, cwd)
            cwd.child_dirs.update({dir_name: new_dir})
        else: # if not a command, and not a dir, it must be a file
            cursor = len(line)
            while not line[cursor - 1].isnumeric():
                cursor -= 1
            name = line[cursor:].strip()
            size = int(line[:cursor].strip())
            cwd.files.append(File(name, size))
            cwd.total_size += size 
    print(home.get_solution_size())

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()