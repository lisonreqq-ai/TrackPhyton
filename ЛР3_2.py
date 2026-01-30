# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sep=','):
    participants1 = set(group1.split(sep))
    participants2 = set(group2.split(sep))

    common = participants1 & participants2

    return sorted(common)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
