grades_str = input()
grades_str_list = grades_str.split(" ")
grades = list(map(int, grades_str_list))

max_grades = [100, 100, 200, 200, 300, 300, 400, 400, 500]

is_hacker = any(grade > max_grade for grade, max_grade in zip(grades, max_grades))

if is_hacker:
    print("hacker")
elif sum(grades) >= 100:
    print("draw")
else:
    print("none")