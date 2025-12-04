def is_invalid(n: str) -> bool:
    len_n = len(n)

    # same as pt 1
    if len_n % 2 == 0:
        s1 = n[0:len_n//2]
        s2 = n[len_n//2:len_n]
        if s1 == s2:
            return True

    # check for repeated pattern
    for i in range(1, len_n // 2 + 1):
        if len_n % i == 0:
            substring = n[:i]
            if substring * (len_n // i) == n:
                return True

    return False

def main():
    inp = "" # input was copied and pasted in there (not on my phone for this part)
    ranges = inp.split(',')
    invalidarray = []
    for arange in ranges:
        bounds = arange.split("-")
        for i in range(int(bounds[0]), int(bounds[1]) + 1):
            if is_invalid(str(i)):
                invalidarray.append(i)
    print(sum(invalidarray))

main()
