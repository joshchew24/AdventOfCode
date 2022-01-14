# AdventOfCode2021
Personal Solution Repository for 2021 Advent of Code problems. View all the associated problem statements here: https://adventofcode.com/

Solutions written using Python 3, some also use numpy 1.12.4.

## Day 11:
This is the first reflection I'm writing. Not really sure what I want these to be but for now I will just be jotting down some thoughts I had about the problem. I may retroactively do the same for the days I missed.  
This day felt like a more challenging combination of day 6 and day 9. I always run into bugs when switching between traditional x,y coordinates and indexing numpy 2-D arrays by row, then column. Found the flashing and energy distribution behaviour interesting to implement. Landed on a queue-based solution that I am quite pleased with, though the code is fairly verbose. 

## Day 12:
### Initial thoughts
Looks like a graph problem... not really looking forward to solving it. I feel like I struggled with this content in CPSC 221, so at this point I am even rustier on this subject. However, I think solving this will improve my confidence and it is also very important in general to be familiar with. 

### Reflection
That was annoying. Spent a few days recalling graph implementations (adjacency lists/matrices) and traversals (DFS/BFS). Tried implementing with no success. I had this goal in my head to avoid using recursion, because I really wanted to try to use a stack/queue for some reason... Was stuck for too long and decided to restart with a fresh implementation and found the recursive method to be incredibly simple to write. For part 2, I hacked together a boolean flag to track whether a single small cave has been double visited. Not a pretty solution but works and could definitely be cleaned up.