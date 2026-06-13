student_grades = {
    "Alice": 100,
    "Bob": 20,
    "Charlie": 85,
    "Diana": 92
}

#.values(): ប្រើសម្រាប់ទាញយកតែទិន្នន័យ (ក្នុងករណីនេះគឺពិន្ទុ) ពី dictionary ដើម្បីយកមកធ្វើការគណនា។
grades = student_grades.values()
# print(type(grades))
average_grades = sum(grades) / len(grades)
print(grades)
#មធ្យមភាគនៃពិន្ទុរបស់សិស្សទាំងអស់គឺ:
print(f"Average grade of all students is: {average_grades}")



