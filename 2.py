def part_1(lines):
    depth = 0
    pos =  0
    for line in lines:
        spl = line.split()
        spl[1] = int(spl[1])
        if spl[0] == "forward":
            pos += spl[1]
        elif spl[0] == "down":
            depth += spl[1]
        elif spl[0] == "up":
            depth -= spl[1]

    return pos*depth    

def part_2(lines):
    depth = 0
    aim = 0
    pos =  0
    for line in lines:
        spl = line.split()
        spl[1] = int(spl[1])
        if spl[0] == "forward":
            pos += spl[1]
            depth += aim*spl[1]
        elif spl[0] == "down":
            aim += spl[1]
        elif spl[0] == "up":
            aim -= spl[1]
    return pos*depth 

lines = open("inputs/2", "r").readlines()



print("part 1:", part_1(lines))
print("part 2:", part_2(lines))