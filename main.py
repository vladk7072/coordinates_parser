import os

# Путь к файлу, в который будет записан результат
output_file_path = "result.txt"

# Удаление содержимого файла (если файл существует)
if os.path.exists(output_file_path):
    open(output_file_path, 'w').close()

# Папка с файлами
folder_path = "1"

# Главный массив для хранения всех кусков данных
main_array = []

# Функция для извлечения данных из файла и добавления их в список
def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        coordinates_start = "<coordinates>"
        coordinates_end = "</coordinates>"
        start_index = data.find(coordinates_start)
        end_index = data.find(coordinates_end)
        coordinates_list = []  # Создаем список для текущего файла
        while start_index != -1 and end_index != -1:
            coordinates_data = data[start_index + len(coordinates_start):end_index].strip()
            coordinates_data = coordinates_data.split("\n")
            coordinates_list.append(coordinates_data)
            start_index = data.find(coordinates_start, end_index)
            end_index = data.find(coordinates_end, start_index)
        main_array.extend(coordinates_list)

# Проход по всем файлам в папке
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  # Убедитесь, что файлы имеют расширение .txt
        file_path = os.path.join(folder_path, filename)
        parse_file(file_path)

# Запись результата в файл
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write("[\n")
    output_file.write("  [\n")
    for coordinates_list in main_array:
        output_file.write("    [\n")
        for coordinates_data in coordinates_list:
            output_file.write("      [")
            output_file.write(coordinates_data)
            output_file.write("],\n")
        output_file.write("    ],\n")
    output_file.write("  ],\n")
    output_file.write("]\n")

# Вывод сообщения о завершении
print("Результат записан в файл:", output_file_path)
