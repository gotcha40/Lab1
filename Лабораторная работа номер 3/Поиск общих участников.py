# TODO Напишите функцию find_common_participants

sep = input('Введите разделитель для формирования списка общих человек:')
p_1_gr = "Иванов|Петров|Сидоров"
p_2_gr = "Петров|Сидоров|Смирнов"
n_1_gr = p_1_gr .replace('|', sep)
n_2_gr = p_2_gr.replace('|', sep)
def find_common_participants(gr_1, gr_2, sep):
    uniq_gr_1=set(gr_1.split(sep))
    uniq_gr_2 = set(gr_2.split(sep))
    uniq_gr_all=uniq_gr_1.union(uniq_gr_2)
    return uniq_gr_all
sorted_set=sorted(find_common_participants(n_1_gr,n_2_gr,","))

print(sorted_set)