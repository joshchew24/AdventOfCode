import importlib
import sys

# USAGE: python3 main.py <day number> <problem number> <solve/test>
def main():
    day = sys.argv[1]
    problem = sys.argv[2]
    mode = sys.argv[3]

    # if single digit day entered, append 0 to front
    # leading zeros used for better sorting in file explorer
    if len(day) == 1:
        day = f"0{day}"

    solution_module = importlib.import_module(f"day{day}.problem{problem}")
    read_input = solution_module.read_input
    solve = solution_module.solve
    
    input = read_input(f"day{day}/{mode}{problem}")
    solve(input)

if __name__ == "__main__":
    main()