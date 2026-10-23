def student_info(name, age, grade):
    return f"Name: {name}, Age: {age}, Grade: {grade}"

# Chiamata con argomenti posizionali:
print(student_info("Orazio", 19, 'A'))

# Chiamata con keyword:
print(student_info(name = "Orazio" , age = 19, grade = 'A'))