lock_current_state = 50
lock_wrap = 100

def l(n: int):
    return (lock_current_state - n) % lock_wrap

def r(n: int):
    return (lock_current_state + n) % lock_wrap

def main():
    global lock_current_state
    function_array = {"R" : r, "L": l}
    counter = 0

    with open("input.txt") as t:
        for line in t:
            lock_current_state = function_array[line[0]](int(line[1::]))
            if (lock_current_state == 0):
                counter += 1

    print(f"answer: {counter}")

if __name__ == "__main__":
    main()
