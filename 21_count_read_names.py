with open('nameslist.txt', 'r') as open_file:
    all_names = open_file.read()

length = len(list(all_names.split('\n')))

all_names = list(set(all_names.split('\n')))

number_names = [0 for x in all_names]

dict_1 = zip(all_names, number_names)

dict_count = dict(dict_1)


with open('nameslist.txt', 'r') as open_file:

    line = open_file.readline().replace("\n", "")

    while length > 0:

        for x in all_names:
            if x == line:
                dict_count[line] += 1
                length -= 1
        line = open_file.readline().replace("\n", "")


print(dict_count)