unsorted_list = [5, 2, 9, 1, 5, 6]

for i in range(len(unsorted_list)):
    for j in range(i + 1, len(unsorted_list)):
        if unsorted_list[i] > unsorted_list[j]:
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]

print("Відсортований список:", unsorted_list)