import bisect

left_list = []
right_list = []

with open("input.txt") as f:
    for line in f:
        left, right = map(int, line.split())
        bisect.insort(left_list, left)
        bisect.insort(right_list, right)
        
sum = 0
similarity = 0
for i in range(len(left_list)):
    sum += abs(right_list[i] - left_list[i])
    for j in range(len(right_list)):
        count = 0
        if left_list[i] == right_list[j]:
            count += 1
        similarity += left_list[i] * count

print(f"Sum of the differences between the left and right list is: {sum}")
print(f"The similarity between the left and right list is: {similarity}")
