def writer():
    file = open("/Users/osmantirpan/PycharmProjects/Cost-Averaging/Database/table_names.txt", "w", encoding='utf-8')

    file.writelines(["\nMerhaba","\nnaber"])
    file.close()

def reader():
    file = open("/Users/osmantirpan/PycharmProjects/Cost-Averaging/Database/table_names.txt", "r", encoding='utf-8')
    table_list = []
    for i in file:
        table_list.append(i)
    return table_list

writer()
print(reader())

