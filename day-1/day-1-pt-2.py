lock_current_state = 50
lock_wrap = 100

def l(n: int):
    return (lock_current_state - n) % lock_wrap

def r(n: int):
    return (lock_current_state + n) % lock_wrap

def wraps(value, delta):
    tmp = value + delta

    if delta > 0: # r
        clicks = (tmp // lock_wrap) - (value // lock_wrap)
    else: # l
        clicks = ((value - 1) // lock_wrap) - ((tmp - 1) // lock_wrap)

    return abs(clicks)

def main():
    global lock_current_state
    function_array = {"R" : r, "L": l}
    counter = 0

    with open("input.txt") as t:
        for line in t:
            n = int(line[1::])
            lock_wrap_count = wraps(lock_current_state, n) if line[0] == 'R' else wraps(lock_current_state, -n)
            print(f"{lock_current_state} {line[0]} {n} times, which wraps {lock_wrap_count}")
            counter += lock_wrap_count
            lock_current_state = function_array[line[0]](n)

    print(f"answer: {counter}")

if __name__ == "__main__":
    main()
