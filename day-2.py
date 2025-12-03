def is_invalid(n: str):
    if len(n) % 2 == 0:
        # print(n)
        s1 = n[0:len(n)//2]
        s2 = n[len(n)//2:len(n)]
        if s1 == s2:
            return True
    return False

def main():
    input = "" # I wrote this on my phone, I copied the input directly in here
    ranges = input.split(',')
    invalidarray = []
    for arange in ranges:
        #print(type(arange))
        #print(dir(arange))
        bounds = arange.split("-")
        for i in range(int(bounds[0]), int(bounds[1]) + 1):
            #print (i)
            if is_invalid(str(i)):
                invalidarray.append(i)
    print(sum(invalidarray))

main()