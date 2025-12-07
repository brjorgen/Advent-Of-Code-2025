def read_file():
    with open("input.txt") as f:
        l = [line for line in f]
        return l

def read_ranges(lines):
    ranges = []
    for line in lines:
        if line == "\n":
            break
        ranges.append(line)
    return ranges, len(ranges)

def read_values(lines):
    i = 0
    while lines[i] != '\n':
        print(i)
        i += 1
    values = lines[i:]
    return values

def assess_freshness_for_each_range(ranges, values):
    is_fresh = []
    print("RANGE:", len(ranges))
    print("VALUE:", len(values))

    ranges = [r.strip() for r in ranges]
    values = [int(r.strip()) for r in values if r != '\n']

    for value in values:
        for arange in ranges:
            bounds = list(map(int, arange.strip().split('-')))
            if value in range(bounds[0], bounds[1] + 1):
                print(f"is fresh!! {value} is in interval {bounds[0]} {bounds[1]}")
                is_fresh.append(value)
                break
    return is_fresh

def main():
    lines = read_file()
    ranges, count = read_ranges(lines)
    values = read_values(lines)
    fresh_stuff = assess_freshness_for_each_range(ranges, values)
    print(len(fresh_stuff))

if __name__ == "__main__":
    main()
