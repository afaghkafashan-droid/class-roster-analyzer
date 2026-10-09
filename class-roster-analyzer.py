students = [
    {"name": "Sara", "score": 92},
    {"name": "Ali", "score": 45},
    {"name": "Reza", "score": 78},
    {"name": "Neda", "score": 55},
    {"name": "Kian", "score": 88}
]


def passed(score):
    return score >= 60


passed_count = 0
failed_names = []


for student in students:
    if passed(student["score"]):
        passed_count += 1
    else:
        failed_names.append(student["name"])


print("total students:", len(students))
print("passed:", passed_count)
print("did not pass:", len(failed_names))
print("names needing extra help:", failed_names)