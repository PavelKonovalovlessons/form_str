team1_num = 6
team2_num = 5
score_1 = 12
score_2 = 13
team1_time = 1830.12
team2_time = 1850.311
tasks_total = 25
time_avg = 147.22
challenge_result = "победа команды Мастера кода!"

print("В команде 'Мастера кода' участников: %s" % team1_num)
print( "Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print("Команда 'Волшебники данных' решила задач: {}!".format(score_2))
print("'Волшебники данных' решили задачи за {} c!".format(team1_time))
print(f"Команды решили {score_1} и {score_2} задач.")
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f"Результат битвы: {result}!")
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')