import os


# Создадим функцию для работы с заданными файлами
def create_file_list(folder):
    file_list = os.listdir(folder)  # Получаем список имен файлов в папке
    merget_file_list = []  # Создаем список для хранения содержимого файлов
    for file in file_list:
        with open(f"{folder}/{file}", encoding='utf8') as temp_file:  # Поочередно считываем файлы
            # Добавляем в список название файла, значение для числа строк и список для содержимого файла
            merget_file_list.append([file, 0, []])
            for line in temp_file:
                merget_file_list[-1][2].append(line.strip())  # Добавляем в список содержимое файла построчно
                merget_file_list[-1][1] += 1  # Увеличиваем значение для числа строк
    # Возвращаем предварительно отсортированный по значению числа строк список с содержимым файлов
    return sorted(merget_file_list, key=lambda x: x[1], reverse=False)


# Создадим функцию для записи итогового файла
def create_merget_file(folder, filename):
    with open(f'{filename}.txt', 'w+', encoding='utf8') as merget_file:  # Откроем (создадим) итоговый файл с именем "filename".txt
        merget_file.write(f'Даны файлы:\n')
        for file in create_file_list(folder):
            merget_file.write(f'Назввание файла: {file[0]}\n')  # Записываем в итоговый файл имена начальных файлов
            merget_file.write(f'Количество строк: {file[1]}\n')  # Записываем в итоговый файл число строк файлов
            for string in file[2]:
                merget_file.write(string + '\n')  # Записываем в итоговый файл содержимое начальных файлов построчно
            merget_file.write('\n')
    return print('Файл создан')


create_merget_file('txt', 'merget_file')
