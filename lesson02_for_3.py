school_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4б', 'scores': [3,4,3,5,3]},
    {'school_class': '4в', 'scores': [4,4,5,5,3]},
    {'school_class': '4г', 'scores': [3,4,4,4,5]}
] 
# количество баллов: 2 * 1 + 3 * 6 + 4 * 8 + 5 * 5 = 77
# количество оценок: 20

def list_average(register):
    try:
        return sum(register)/len(register)
    except (TypeError, ZeroDivisionError):
        print("Ошибка: ожидается не пустой список целых чисел")
        return None

class_average_list = []

for class_scores in school_scores:
    class_average_list.append(list_average(class_scores["scores"]))

print(list_average(class_average_list))