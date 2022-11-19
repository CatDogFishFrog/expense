import argparse
from table_in_terminal import Table

class CommandLine:
    pass

    def main():
        if Table.file_path != '': upd_text =  f'Наразі обрано разташування файлу:\n{Table.file_path}{Table.file_name}'
        else:               upd_text =   'Наразі не обрано розташування файлу'
        
        parser = argparse.ArgumentParser(description=f'Програма обліку домашніх вітрат. {upd_text}',
                                        prog='Expense',
                                        usage='expens [options]',
                                        epilog='Ну все, кінеь',
                                        argument_default=False
                                        )
        parser.add_argument('--path', '-p', 
                            help='Обрати розташування файла з таблицею. Приклад: -p "C:\\Users\Public\\Documents"',
                            default=None,
                            type=str,
                            required=False
                            )
        parser.add_argument('--name', '-n',
                            help='Обрати назву файла з таблицею. Приклад: -n new_file',
                            default=None,
                            type=str,
                            required=False
                            )
        parser.add_argument('--write', '-w',
                            help='Записати у файл нову строку. Якщо не вказано дату, то записує сьогоднішню. Якщо не вказано тип, то записує "Різне" Приклад: -w "Молоко та сир" 268   (за бажанням): -d 25.09.2022 -t Їжа',
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
        parser.add_argument('--sortcost', '-sc',
                            help="Доповнення до аргументу READ. Сортування за ціною. Приклад: -r -sc",
                            action='store_true',
                            required=False
                            )
        parser.add_argument('--sortname', '-sn',
                            help="Доповнення до аргументу READ. Сортування за назвою. Приклад: -r -sn",
                            action='store_true',
                            required=False
                            )
        parser.add_argument('--sortdate', '-sd',
                            help="Доповнення до аргументу READ. Сортування за датою. Приклад: -r -sd",
                            action='store_true',
                            required=False
                            )
        parser.add_argument('--revers', '-re',
                            help="Доповнення до аргументу READ. Вмикає зворотнє сортування. Приклад: -r -sc -re",
                            action='store_true',
                            required=False
                            )
        parser.add_argument('--range',
                            help="Доповнення до аргументу READ. Виводить діапазон дат (або конкретну, якщо вкажете лише одну). Приклад: -r -sc -re --range 21.12.2022 30.12.2022",
                            metavar='N',
                            nargs='+',
                            required=False
                            )
        parser.add_argument('--ty',
                            help='Доповнення до аргументу READ. Виводить лише окремий тип',
                            default=None,
                            required=False)
        
        args = parser.parse_args()
            
        if args.path != None:
            Table.set_file_path(args.path)
            
        if args.name != None:
            Table.set_file_name(args.name)
            
        if args.read == True:
            
            range_start = None
            range_end = None
            if args.range != False:
                range_start = args.range[0]
                try:
                    range_end = args.range[1]
                except:
                    range_end = None
                    
            if args.sortcost != False: sort = 'Ціна'
            elif args.sortname != False: sort = 'Назва'
            elif args.sortdate != False: sort = 'Дата'
            else: sort = None
                
            Table.print_table_with_sort(sort, args.revers, range_start,  range_end, args.ty)
    
        if args.write != False:
            name, cost = args.write
            if args.date != False and args.type != False:
                Table.append_file(name, float(cost), args.date, args.type)
            elif args.date != False:
                Table.append_file(name, float(cost), args.date)
            elif args.type != False:
                Table.append_file(name, float(cost), type=args.type)
            else: Table.append_file(name, float(cost))
    