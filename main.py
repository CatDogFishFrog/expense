from expense import Expense
from prettytable import PrettyTable
from prettytable import from_csv
import os
import csv
import argparse


file_path = ''
file_name = '\\data.csv'

if os.path.exists('data.txt'):
    with open('data.txt', 'r') as file:
        file_path = file.readline().strip()
        file_name = file.readline().strip()
        
def set_file_name(new_name:str):
    global file_name
    file_name = '\\'+new_name+'.csv'
    replase_row_in_file(1, 'data.txt', file_name)
    
def set_file_path(new_path:str):
    global file_path
    file_path = new_path
    replase_row_in_file(0, 'data.txt', new_path)
    
def replase_row_in_file(row_count:int, file_p:str, new_data:str):
    with open(file_p, 'r') as file:
        old_file = file.readlines()
    old_file[row_count] =  new_data+'\n'
    with open(file_p, 'w') as file:
        file.writelines(old_file)

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
    if file_path != '': upd_text =  f'Наразі обрано разташування файлу:\n{file_path}{file_name}'
    else:               upd_text =   'Наразі не обрано розташування файлу'
    
    parser = argparse.ArgumentParser(description=f'Програма обліку домашніх вітрат. {upd_text}',
                                    prog='Expense',
                                    usage='expens [options]',
                                    epilog='Ну все, кінеь',
                                    argument_default=False
                                    )
    parser.add_argument('--path', '-p', 
                        help='Обрати розташування файла',
                        default=None,
                        type=str,
                        required=False
                        )
    parser.add_argument('--name', '-n',
                        help='Обрати назву файла',
                        default=None,
                        type=str,
                        required=False
                        )
    parser.add_argument('--write', '-w',
                        help='Записати у файл нову строку. Якщо не вказано дату, то записує сьогоднішню. Якщо не вказано тип, то записує "Різне" Приклад: -w <name> <cost> (optional): -d <date> -t <type>',
                        nargs=2,
                        metavar=('name', 'cost'),
                        required=False
                        )
    parser.add_argument('--date', '-d',
                        help='Доповнення до аргументу WRITE, дозволяє записати дату запису',
                        required=False
                        )  
    parser.add_argument('--type', '-t',
                        help='Доповнення до аргументу WRITE, дозволяє додати тип запису',
                        required=False
                        )
    parser.add_argument('--read', '-r',
                        help="Прочитати файл",
                        action='store_true',
                        required=False
                        )
    
    args = parser.parse_args()
        
    if args.path != None:
        set_file_path(args.path)
        
    if args.name != None:
        set_file_name(args.name)
        
    if args.read == True:
        read_file()
        
    if args.write != False:
        name, cost = args.write
        if args.date != False and args.type != False:
            append_file(name, float(cost), args.date, args.type)
        elif args.date != False:
            append_file(name, float(cost), args.date)
        elif args.type != False:
            append_file(name, float(cost), type=args.type)
        else: append_file(name, float(cost))
            


if __name__ == '__main__':
    main()
