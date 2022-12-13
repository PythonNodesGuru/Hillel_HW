# Занятия проходят по понедельникам и четвергам в 19:15
# Первое занятие произошло 17.10.2022. Всего 32 занятия.
# Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю)


from datetime import timedelta, date

first_lesson = date(2022, 10, 17)
lessons_for_each_day = 16
date.today()
monday_lesson = first_lesson
lecture_dates = [first_lesson]

for i in range(lessons_for_each_day):
    monday_lesson += timedelta(days=3)
    lecture_dates.append(monday_lesson)
    thursday_lesson = monday_lesson + timedelta(days=4)
    monday_lesson = thursday_lesson
    lecture_dates.append(monday_lesson)
lecture_dates.pop()

for i, value in enumerate(lecture_dates):
    print('Lecture  ' + '{:>3}'.format(i + 1) + ': {: %d %b %Y}'.format(lecture_dates[i]) + ' 19:15')
