grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a_0 = sum(grades[0])
a_1 = len(grades[0])
average_a = (a_0 / a_1)
# print(average_a)
b_0 = sum(grades[1])
b_1 = len(grades[1])
average_b = (b_0 / b_1)
# print(average_b)
j_0 = sum(grades[2])
j_1 = len(grades[2])
average_j = (j_0 / j_1)
# print(average_j)
k_0 = sum(grades[3])
k_1 = len(grades[3])
average_k = (k_0 / k_1)
# print(average_k)
s_0 = sum(grades[4])
s_1 = len(grades[4])
average_s = (s_0 / s_1)
# print(average_s)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
name = sorted(students)
raitings = {name[0]: average_a, name[1]: average_b, name[2]: average_j, name[3]: average_k, name[4]: average_s}
print(raitings)
