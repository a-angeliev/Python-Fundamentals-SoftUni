data = input()
exam_results = {}
language_statistics = {}

while not data == 'exam finished':
    data = data.split('-')
    if len(data) > 2:
        username, language, points = data
        points = int(points)
        if username not in exam_results:
            exam_results[username] = points
        else:
            if exam_results[username] < points:
                exam_results[username] = points
        if language not in language_statistics:
            language_statistics[language] = 1
        else:
            language_statistics[language] += 1
    else:
        username, command = data
        del exam_results[username]
    data = input()

exam_results_sorted = sorted(exam_results.items(), key=lambda x: (-x[1], x[0]))
language_statistics_sorted = sorted(language_statistics.items(), key=lambda x: (-x[1], x[0]))
print('Results:')
for key, value in exam_results_sorted:
    print(f'{key} | {value}')
print('Submissions:')
for key, value in language_statistics_sorted:
    print(f'{key} - {value}')