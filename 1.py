

def part_1(lines):
    count = 0
    prev = int(lines[0])
    for line in lines:
        num = int(line)
        if count == 0:
            count += 1
            continue
        
        if num > prev:
            count += 1
        prev = num
        
    return count-1

def part_2(lines):
    count = 0
    prev = int(lines[0]) + int(lines[1]) + int(lines[2])
    index = 0
    while index < len(lines)-2:
        num = int(lines[index]) + int(lines[index+1]) + int(lines[index+2])
        if count == 0:
            count += 1
            continue

        if num > prev:
            count += 1
        prev = num
        
        index += 1

    return count-1

lines = open("inputs/1", "r").readlines()

print("part 1:", part_1(lines))
print("part 2:", part_2(lines))