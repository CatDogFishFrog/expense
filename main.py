from expense import Expense
from prettytable import PrettyTable
from prettytable import from_csv
import os
import csv
import argparse


file_path = ''
file_name = '\\data.csv'

if os.path.exists('name.txt'): #об'єднати у один файл
    with open('name.txt', 'r') as file:
        file_name = file.readline()

if os.path.exists('path.txt'): #об'єднати у один файл
    with open('path.txt', 'r') as file:
        file_path = file.readline()
        
def set_file_name(new_name:str): #об'єднати у один файл
    global file_name
    file_name = '\\'+new_name+'.csv'
    with open('name.txt', 'w') as file:
        file.write(file_name)

def set_file_path(new_path:str): #об'єднати у один файл
    global file_path
    file_path = new_path
    with open('path.txt', 'w') as file:
        file.write(new_path)
    
def read_file():
    global file_path
    global file_name
    path = file_path+file_name
    if(os.path.exists(path)):
        with open(path, 'r') as file_db:
            table = from_csv(file_db)
        print(table)
    else:
        print('Файла поки що не існує. Спочатку стфоріть файл') 

def append_file(name, cost, date=None, type=None):
    path = file_path+file_name
    new_row = Expense(name=name, cost=cost, date=date, type=type)
    with open(path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row.list())

def main():
    global file_path
    global file_name
    if file_path != '': upd_text =  f'Наразі обрано разташування файлу:\n{file_path}'
    else:               upd_text =   'Наразі не обрано розташування файлу'
    
    parser = argparse.ArgumentParser(
                                    description=f'Програма обліку домашніх вітрат. {upd_text}',
                                    prog='Expense',
                                    usage='expens [options]',
                                    epilog='Ну все, кінеь',
                                    argument_default=False
                                    )
    parser.add_argument('--path', '-p', 
                        help='Обрати розташування файла',
                        default=None,
                        type=str,
                        required=False)
    
    parser.add_argument('--name', '-n',
                        help='Обрати назву файла',
                        default=None,
                        type=str,
                        required=False)
    
    parser.add_argument('--write', '-w', #Розділити на декілька аргументів
                        help='Записати у файл',
                        nargs=4,
                        metavar=('name', 'cost', 'date', 'type'),
                        required=False)
    
    parser.add_argument('--read', '-r',
                        help="Прочитати файл у обраному шляху",
                        action='store_true',
                        required=False)
    
    args = parser.parse_args()
    
    
    if args.path != None:
        set_file_path(args.path)
        
    if args.name != None:
        set_file_name(args.name)
        
    if args.read == True:
        read_file()
        
    if args.write != False:
        print(args.write)
        name, cost, date, type = args.write
        append_file(name, float(cost), date, type)


if __name__ == '__main__':

    main()
