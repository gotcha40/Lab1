main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
###Часть кода из которого создал функцию
#dic=dict()
#list=[]
#for val in main_str:
    #if val.isalpha():
        #val_low=val.lower()
        #list.append(val_low)
        #uniq_set=set(list)
#print(uniq_set)
#for el in uniq_set:
#    main_str_low=main_str.lower()
#   count_el=main_str_low.count(el)
#   dic[el]=count_el
#print(dic)
def count_letters(letter):
    list = []
    dic=dict()
    for val in letter:
        if val.isalpha():
            val_low = val.lower()
            list.append(val_low)
            uniq_set = set(list)
    for el in uniq_set:
        letter_low = letter.lower()
        count_el = letter_low.count(el)
        dic[el] = count_el
    return dic
print(count_letters(main_str))
def calculate_frequency(dictionary):
    sum_letters=sum(dictionary.values())
    print(sum_letters)
    for el in dictionary:
        dictionary[str(el)]=round(dictionary[str(el)]/sum_letters,2)
    return dictionary
print(calculate_frequency(count_letters(main_str)))


