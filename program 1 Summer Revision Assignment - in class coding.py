students = int(input('how many students are there:  '))
coach = 550
ticket = 30
adding = 550 + 30 * 15
students_free = students / 11
rtc = adding - 30 * students_free
cost_per_student = rtc / students
print(cost_per_student)