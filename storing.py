import student, pickle

list1=[student.student("Alice", 101, "CS"), student.student("Bob", 102, "EE"), student.student("Charlie", 103, "ME")]
with open("students.data", "wb") as f:
    for s in list1:
        pickle.dump(s,f) #object and file handler as arguments
