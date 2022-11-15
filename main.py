from expense import Expense
import os
import csv
import argparse
from prettytable import PrettyTable

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
            reader = csv.reader(file_db)
            print('Дата\t\tЦіна\t\tНазва\t\tТип')
            for row in reader: 
                print(f'{row[0],}   |{row[1],10}   |{row[2],10}   |{row[3]}')
    else:
        print('Файла поки що не існує. Спочатку стфоріть файл')    
        
#def append_file():
    

def open_file(): # на видалення, а поки що для розбору на запчастини :)
    if(os.path.exists(file_path)):     
        with open(file_path, 'a', newline='') as file_db:
            x = int(input('Скільки строчок введемо? '))
            for i in range(x):
                write_file(file_db)             
    else:
        print('Файла ще немає. Створити його? (Y/n) ', end='')
        answer = input()

        with open(file_path, 'w', newline='') as file_db:
            print('Файл створено. Зараз введемо щось нове.')
            x = int(input('Скільки строчок введемо? '))
            for i in range(x):
                write_file(file_db) 

def write_file(file_db): #також на переробку і на запчастини
    writer = csv.writer(file_db)
    print('Додамо нову витрату...\nЗапишіть параметри цього запису (можна залишати пустими)')
    new_Expense = Expense()
    new_Expense.date = input('Запишіть дату (якщо залишити пустим буде записано сьогоднішня дата): ')
    new_Expense.cost = float(input('Запишіть ціну: '))
    new_Expense.name = input('Запишіть назву: ')
    new_Expense.type = input('Запишіть тип: ')
    writer.writerow(new_Expense.list())

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
    
    parser.add_argument('--write', '-w',
                        help='Записати у файл',
                        
                        action='store_true',
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
        
    print(file_path+file_name)

if __name__ == '__main__':

    main()


print(file_path)
print(file_name)
