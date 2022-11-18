import os
import csv
from prettytable import PrettyTable
from datetime import datetime
from expense import Expense

class Table:
    pass

    file_path = ''
    file_name = '\\data.csv'

    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as file:
            file_path = file.readline().strip()
            file_name = file.readline().strip()
            
    def set_file_name(new_name:str):
        global file_name
        file_name = '\\'+new_name+'.csv'
        Table.replase_row_in_file(1, 'data.txt', file_name)
        
    def set_file_path(new_path:str):
        global file_path
        file_path = new_path
        Table.replase_row_in_file(0, 'data.txt', new_path)
        
    def replase_row_in_file(row_count:int, file_p:str, new_data:str):
        with open(file_p, 'r') as file:
            old_file = file.readlines()
        old_file[row_count] =  new_data+'\n'
        with open(file_p, 'w') as file:
            file.writelines(old_file)

    def print_table_with_sort(key:str = None, revers = False, range_start = None, range_end = None):
        path = Table.file_path + Table.file_name
        if range_start != None:
            if range_end != None:
                range_end_d = datetime.strptime(range_end, Expense.format_date)
                range_start_d = datetime.strptime(range_start, Expense.format_date)
            else:
                range_start_d = datetime.strptime(range_start, Expense.format_date)
                range_end_d = range_start_d
            
        if(os.path.exists(path)):
            table = PrettyTable(field_names=['Дата', 'Ціна', 'Назва', 'Тип'])
            with open(path, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                if range_start != None:
                    for line in reader:
                        if datetime.strptime(line[0], Expense.format_date) >= range_start_d and datetime.strptime(line[0], Expense.format_date) <= range_end_d:
                            line[1] = int(line[1])
                            table.add_row(line)
                else:
                    for line in reader:
                        line[1] = int(line[1])
                        table.add_row(line)
                table.align["Ціна"] = 'r'
                table.align["Назва"] = 'l'
            try: 
                table.sortby = key    
            except:
                print('Такого стовпця не існує, сортування відміняється')
            table.reversesort = revers
            print(table)
        else: print('Файла поки що не існує. Спочатку стфоріть файл') 

    def append_file(name, cost, date=None, type=None):
        path = file_path+file_name
        new_row = Expense(name=name, cost=cost, date=date, type=type)
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row.list())