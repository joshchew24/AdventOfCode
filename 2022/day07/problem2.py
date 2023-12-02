import sys
import re

cd_command = "\$\scd\s"

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent: Dir = parent
        self.child_dirs: dict[str: Dir] = {}
        self.files: list[File] = []
        self._total_size = 0

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name

    def get_solution_size(self, required):
        soln = self._total_size
        diff = soln - required  
        if diff < 0: # too small, return max size to eliminate self from consideration
            return sys.maxsize
        for child in self.child_dirs.values():
            child_smallest_soln = child.get_solution_size(required)
            child_smallest_soln_diff = child_smallest_soln - required
            if child_smallest_soln_diff - required < diff:
                diff = child_smallest_soln_diff
                soln = child_smallest_soln
        return soln
        
    def calc_total_size(self):
        self._total_size = 0
        for file in self.files:
            self._total_size += file.size
        for child in self.child_dirs.values():
            self._total_size += child.calc_total_size()
        return self._total_size

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
                    cwd.calc_total_size()
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
    empty = 70000000 - home.calc_total_size()
    required = 30000000 - empty
    print(home.get_solution_size(required))

def main():
    solve(read_input(sys.argv[1]))

if __name__ == "__main__":
    main()