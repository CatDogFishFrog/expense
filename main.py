from expense import Expense
import os
import csv

print('Ласкаво просимо у програму!\nУведіть help для довідки')


def write_file(file_db):
    writer = csv.writer(file_db)
    print('Додамо нову витрату...\nЗапишіть параметри цього запису (можна залишати пустими)')
    new_Expense = Expense()
    new_Expense.date = input('Запишіть дату (якщо залишити пустим буде записано сьогоднішня дата): ')
    new_Expense.cost = float(input('Запишіть ціну: '))
    new_Expense.name = input('Запишіть назву: ')
    new_Expense.type = input('Запишіть тип: ')
    writer.writerow(new_Expense.list())
    

def open_file():
    file_path = 'C://Users/vadim/OneDrive/projects/files/bd.csv'
    if(os.path.exists(file_path)):
        print('Файл вже існує. Відкрити його? (Y/n) ', end='')     
        answer = input()
        if answer == 'Y' or answer == 'y':
            print('Файл відкритий')
            answer = input('Прочитати файл чи ввести щось нове? (read/write)')
            
            match answer:
                case 'read':
                    with open(file_path, 'r', newline='') as file_db:
                        reader = csv.reader(file_db)
                        for row in reader:
                            print(row)
                    
                case 'write':
                    with open(file_path, 'a', newline='') as file_db:
                        x = int(input('Скільки строчок введемо? '))
                        for i in range(x):
                            write_file(file_db)             
        else: print('--------------------------')
    
    
    else:
        print('Файла ще немає. Створити його? (Y/n) ', end='')
        answer = input()
        
        if answer == 'Y' or answer == 'y':
            with open(file_path, 'w', newline='') as file_db:
                print('Файл створено. Зараз введемо щось нове.')
                x = int(input('Скільки строчок введемо? '))
                for i in range(x):
                    write_file(file_db) 
        else: print('--------------------------')

def main(arg:str):
        match arg:
            case 'help':
                print('<o> або  <open> - відкрити файл\n<c> або  <close> - закрити файл')
                return True
            case 'open':
                open_file()
                return True                
            case 'exit':
                print('Завершення програми...')
                return False
            case _:
                print("Щось не так...")
                return True
x = True
while x:
    x = main(input())