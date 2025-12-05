def find_biggest_2_digit_pair(nums):
    biggest_value = max(nums)
    index = nums.index(max(nums))

    nums[index] = 0
    l = nums[0:index] if index != 0 else None
    r = nums[index:] if index != len(nums) - 1 else None

    if l == None:
        r = max(nums)
        ans = f"{biggest_value}{r}"

    elif r == None:
        l = max(nums)
        ans = f"{l}{biggest_value}"

    else:
        biggest_l = max(list(l))
        biggest_r = max(list(r))
        value_l = f"{biggest_l}{biggest_value}"
        value_r = f"{biggest_value}{biggest_r}"

        if value_l > value_r:
            ans = value_l
        else:
            ans = value_r

    # print("...", ans)
    return ans


def main():
    ans = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip("\n")
            line = list(map(int, line))
            biggest_2_digit_pair = find_biggest_2_digit_pair(line)
            if biggest_2_digit_pair != None:
                ans.append(biggest_2_digit_pair)

    print(sum(list(map(int, ans))))

main()
