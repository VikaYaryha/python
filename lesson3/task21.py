"""Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}"""

# Вариант 1 - Modified
unique_kyes = set()
for dict_item in list_1:
    for value_dict in dict_item.values():  # Сразу получи значения словаря, а не его ключ
        unique_kyes.add(value_dict)  # Кладём значение без обрашения по ключу (dict_item[key])
print(unique_kyes)


# Вариант 2
unique_kyes = set()
for value in list_1:
    unique_kyes.update(value.values())
print(unique_kyes)