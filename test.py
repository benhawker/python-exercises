# Write a function that compresses a string from aaabbcc => a3b2c2
text = "aaabbcc"
last_value = 0
last_index = 0
output = []

as_list = list(text)
for idx, val in enumerate(as_list):
    if len(as_list) == idx + 1:
        break

    if val != as_list[idx + 1]:
        output.append(val)
        output.append((idx + 1) - last_index)

        last_value += idx
        last_index = idx + 1

# Handle last element(s)
if as_list[-2] == as_list[-1]:
    # It matches
    output.append(as_list[-1])
    output.append(len(as_list) - last_index)
else:
    output.append(as_list[-1])
    output.append("1")

print(output)


# Find the element that occurs only once in a given set of integers
# while all the other numbers occur thrice.
# Example 1:
# Input : 3 3 3 4
# Output: 4
# Example 2:
# Input : 5 5 4 8 4 5 8 9 4 8
# Output: 9
# array = %w(5 5 4 8 4 5 8 9 4 8).map(&:to_i)
input_array = [5, 5, 4, 8, 4, 5, 8, 9, 4, 8]
seen = {}
for val in input_array:
    if val in seen:
        seen[val] += 1
    else:
        seen[val] = 1

for k, v in seen.items():
    if v == 1:
        print(f"{k} appears once")


# For the given array [1,4,3,6,7,5,9,1] return the elements that have the peak difference
# vs the previous element
# array = [1,4,3,6,7,5]
# Should return 4 and 6.
input_array = [1, 4, 3, 6, 7, 5]
diff_map = {}

for idx, val in enumerate(input_array):
    if idx == 0:
        continue
    difference = abs((val - input_array[idx - 1]))

    # print(diff_map)
    if difference in diff_map:
        (diff_map[difference]).append(idx)
    else:
        (diff_map[difference]) = [idx]


sorted_keys = sorted(diff_map.keys())
results = diff_map[sorted_keys[-1]]

for i in results:
    print(input_array[i])


# Given an array of n integers where n > 1, nums,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve it without division and in O(n).
# For example, given [1,2,3,4], return [24,12,8,6].
# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
def calculate_product(list, idx):
    sum = 1
    for val in list:
        sum *= val

    return round(sum / list[idx])


input_list = [1, 2, 3, 4]
output = []

for idx, val in enumerate(input_list):
    output.append(calculate_product(input_list, idx))

print(output)
