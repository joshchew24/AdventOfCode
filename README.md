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

## Day 13:
### Initial thoughts
Thinking of different ways to implement. Could use numpy arrays but seems like a big waste of memory. If I go this route, can numpy arrays be dynamically sized for a generalized puzzle input? i.e. do I need to initialize to a fized size and populate from the input? Another possible approach would be just using the list and mathematically calculating their mirror image across the fold and removing duplicates. Maybe use a dictionary to optimize. Seems like the fold instructions always fold in half.

### Reflection (bit of an incoherent rambling of thoughts)
Took longer than I expected but I flip-flopped between a couple ideas and took a dinner break in the middle. Initially pursued class-based implementation but realized I could probably do the whole thing as a dictionary of tuples (hashmap for quicker indexing, don't actually need the values). Tried using a defaultdict but I don't think it was necessary since the values were entirely ignored, though I think it simplifies creation of new keys. Tried splitting various procedures into their own functions but I think it complicated things a little. (using axis 0 or 1 for indexing the tuple caused a headache as I realized this approach wouldn't work since tuples are immutable. Had to implement explicit workaround rather than using the anonynmity of the axis index) Drawing the final picture was an interesting challenge and I thought I might use a binary drawing in the command line but that seemed annoying to implement and ineffective at displaying the information. I went with the easiest method of searching stack overflow for how to display coordinates and found a matplotlib solution that worked fantastic. I'm glad I had a bit of experience using mpl from Kardium. Overall enjoyed this problem :)

## Day 14:
### Initial thoughts
Seems pretty straight forward. Dictionary to store the pair insertion rules, sliding window loop. Problem 2 will probably test for optimisation so will have to think of something clever.
