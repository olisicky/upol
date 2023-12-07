n = int(input('Zadej celé číslo: '))

result = []    # as global for purpose of this task

def decompose_number(target, current_combination):
    if target == 0:
        result.append(sorted(current_combination.copy(), reverse=True))
        return
    for i in range(1, target + 1):
        if i <= target:
            current_combination.append(i)
            decompose_number(target - i, current_combination)
            current_combination.pop()

decompose_number(n, [])
unique_res = []
for comb in result:
    if comb not in unique_res:
        unique_res.append(comb)

for combination in sorted(unique_res):
    print(combination)