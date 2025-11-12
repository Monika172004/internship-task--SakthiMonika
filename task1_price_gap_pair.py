def find_price_gap_pair(nums: list[int], k: int) -> tuple[int, int] | None:
    seen = {}
    best = None
    for j, num in enumerate(nums):
        for target in (num - k, num + k):
            if target in seen:
                i = seen[target]
                if i < j and (best is None or (i, j) < best):
                    best = (i, j)
        if num not in seen:
            seen[num] = j
    return best

if __name__== "_main_":
    print(find_price_gap_pair([4, 1, 6, 3, 8], 2))
    print(find_price_gap_pair([5, 5, 5], 0))
    print(find_price_gap_pair([-3, 7, 1, -1, 4], 2))
    print(find_price_gap_pair([10, 20, 30], 25))
