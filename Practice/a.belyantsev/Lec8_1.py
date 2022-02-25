# По заданному списку создать новый список, который содержит уникальные элементы изначального списка, расположенные
# в порядке возрастания количества вхождений этих элементов в изначальный список.
in_list = ['a', 'b', 'a', 'b', 'b', 'b', 'c', 'd']
temp_dict = {}
for element in in_list:
    temp_dict[element] = temp_dict.get(element, 0) + 1

out_list = list(sorted(temp_dict, key=temp_dict.get))
print(out_list)
