# Форматирование строк с использованием различных методов
# входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Определяем результат соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Использование %
output1 = "В команде Мастера кода участников: %d !" % team1_num
output2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Использование format()
output3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
output4 = "Волшебники данных решили задачи за {} с !".format(team2_time)

# Использование f-строк
output5 = f"Команды решили {score_1} и {score_2} задач."
output6 = f"Результат битвы: {challenge_result}"
output7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

# Вывод всех результирующих строк
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
print(output6)
print(output7)
