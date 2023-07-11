# delate_data
def delete_data():
    deleted_line = int(input('Введите номер строки: '))
    with open("data_second_variant.csv", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line_number, line in enumerate(lines):
            if line_number != deleted_line:
                file.write(line)
        file.truncate()

def delete_data():
    number = int(input('Введите номер данных: '))
    with open("data_first_variant.csv", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line_number, line in enumerate(lines):
            if line_number != range(number, number + 4):
                file.write(line)
        file.truncate()    
