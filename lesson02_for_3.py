school_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4б', 'scores': [3,4,3,5,3]},
    {'school_class': '4в', 'scores': [4,4,5,5,3]},
    {'school_class': '4г', 'scores': [3,4,4,4,5]},
    {'school_class': '4д', 'scores': [3,4,3,3,3]}
] 

def list_average(register):
    try:
        return sum(register)/len(register)
    except (TypeError, ZeroDivisionError):
        print("Ошибка: ожидается не пустой список целых чисел")
        return None

# Вычисление через средние оценки по классам
class_average_list = []

for class_scores in school_scores:
    class_average = list_average(class_scores["scores"])
    class_average_list.append(class_average)
    print(f'Средняя оценка класса {class_scores["school_class"]}: {class_average}')

print(f'Среднее значение средних оценок по классам: {list_average(class_average_list)}')

# Вычисление средней оценки по общему списку школьных оценок
school_scores_list = []

for class_scores in school_scores:
    school_scores_list.extend(class_scores["scores"])
# Нашел интересный способ слияния двух списков через sorted. 
# Вроде как самый быстрый, т.к. реализован на С.
#    school_scores_list = sorted(school_scores_list + class_scores["scores"])
 
print(f'Среднее значение оценок по школе: {list_average(school_scores_list)}')