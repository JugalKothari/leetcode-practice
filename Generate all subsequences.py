from typing import List


def generate_aps(index: int, sub_seq: List[int], n: int):
    if index==n:
        print(sub_seq)
        return

    sub_seq.append(nums[index])
    generate_aps(index+1, sub_seq, n)
    sub_seq.remove(nums[index])
    generate_aps(index+1, sub_seq, n)


nums = [1, 2, 3, 4]
n = len(nums)
generate_aps(0, [], n)
