import os
import csv
from prettytable import PrettyTable
from datetime import datetime
from expense import Expense
from prettytable import SINGLE_BORDER

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

    def print_table_with_sort(key:str = None, revers = False, range_start = None, range_end = None, types = None):
        path = Table.file_path + Table.file_name
        if range_start != None:
            range_start_d = datetime.strptime(range_start, Expense.format_date)
            if range_end == None:
                range_end_d = range_start_d
                
        
        if(os.path.exists(path)):
            table = PrettyTable(field_names=['Дата', 'Ціна', 'Назва', 'Тип'])
            with open(path, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                stats = {'cost_sum':0,
                         'date_start':None,
                         'date_end':None,
                         'bigest_expanse':0,
                         'bigest_expanse_name':'',
                         'bigest_expanse_date':'',
                         'Average_day_cost':0,
                         'days':None}
                type_check = True
                for_once = True
                if range_start != None:
                    
                    for line in reader:
                        
                        if types != None:
                            type_check = types == line[3]
                        
                        line_date = datetime.strptime(line[0], Expense.format_date)  
                        if line_date >= range_start_d and line_date <= range_end_d and type_check:
                            line[1] = int(line[1])
                            stats['cost_sum']+=line[1]
                            if for_once:
                                stats['date_end'] = line_date
                                stats['date_start'] = line_date
                                for_once = False
                            if stats['bigest_expanse'] < line[1]:
                                stats['bigest_expanse'] = line[1]
                                stats['bigest_expanse_name'] = line[2]
                                stats['bigest_expanse_date'] = line[0]
                            if line_date > stats['date_end']: stats['date_end'] = line_date
                            if line_date < stats['date_start']: stats['date_start'] = line_date
                            table.add_row(line)
                else:
                    for line in reader:
                        line_date = datetime.strptime(line[0], Expense.format_date) 
                        line[1] = int(line[1])
                        stats['cost_sum']+=line[1]
                        if for_once:
                            stats['date_end'] = line_date
                            stats['date_start'] = line_date
                            for_once = False
                        if stats['bigest_expanse'] < line[1]:
                                stats['bigest_expanse'] = line[1]
                                stats['bigest_expanse_name'] = line[2]
                                stats['bigest_expanse_date'] = line[0]
                        if line_date > stats['date_end']: stats['date_end'] = line_date
                        if line_date < stats['date_start']: stats['date_start'] = line_date
                        table.add_row(line)
            stats['days'] = stats['date_end'] - stats['date_start']
            stats['Average_day_cost'] = stats['cost_sum'] / stats['days'].days
            
            table.align["Ціна"] = 'r'
            table.align["Назва"] = 'l'
            table.set_style(SINGLE_BORDER)
            if key != None:
                try: 
                    table.sortby = key    
                except:
                    print('Такого стовпця не існує, сортування відміняється')
            table.reversesort = revers
            print(table)
            print(f'Виведено дати з {datetime.strftime(stats["date_start"], Expense.format_date)} до {datetime.strftime(stats["date_end"], Expense.format_date)}. Це {stats["days"].days} днів.\n\nЗа цей проміжок витрачено {stats["cost_sum"]} грн. Це у середньому {round(stats["Average_day_cost"])} грн. {round((stats["Average_day_cost"]%1)*100)} к. за день.\n\nА найбільша витрата була зроблена {stats["bigest_expanse_date"]}, і це "{stats["bigest_expanse_name"]}", що коштувало {stats["bigest_expanse"]} грн.\n')
        else: print('Файла поки що не існує. Спочатку стфоріть файл') 

    def append_file(name, cost, date=None, type=None):
        path = file_path+file_name
        new_row = Expense(name=name, cost=cost, date=date, type=type)
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row.list())