def biggest_and_index(nums, start, remaining):
    end = len(nums) - remaining
    biggest = -1
    biggest_index = -1

    for i in range(start, end + 1):
        if nums[i] > biggest:
            biggest = nums[i]
            biggest_index = i

    return biggest, biggest_index

def get_n_biggest_digits(nums):
    index_list = []
    start = 0
    total = 12

    for i in range(total):
        biggest, index = biggest_and_index(nums, start, total - i)
        index_list.append(index)
        start = index + 1

    misc = "".join(str(nums[i]) for i in index_list)
    return misc

def main():
    ans = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            nums = list(map(int, line))
            digits = get_n_biggest_digits(nums)
            ans.append(int(digits))

    print(sum(ans))

main()
