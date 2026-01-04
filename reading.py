import student,pickle

with open("students.data", "rb") as f:
    for i in range(3):
        s=pickle.load(f)
        s.display()