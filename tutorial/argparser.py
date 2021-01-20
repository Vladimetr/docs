import argparse

# init argparser with discription
# run sctipt.py -h
# чтобы вывести описание программы
# и ее ключей
parser = argparse.ArgumentParser(description='Kochetkov')


# -------------------------- action = store --------------------------
# значение ключа записывается в переменную

# создать ключ -a, значение которого запишется в переменную ip
# если его не указать, то будет None
parser.add_argument('-a', action="store", dest="ip", help="dicription of what -a does")

parser.add_argument('--sex', action="store", choices=['male', 'female'], default='male')
# можем ограничить выбор параметра

# также можно указать тип переменной и значение по умолчанию
parser.add_argument('-c', action="store", dest="count", default=2, type=int)

# ключ -d является обязательным
# если его не указать, то будет ошибка
parser.add_argument('-d', action="store", dest="delta", required=True, type=str)


# ------------------------ action = const -----------------------------
# при вызове ключа в переменную запишется указанная в коде const
# иначе в переменную запишется None

parser.add_argument('--take_const', dest='suka', action='store_const', const=42)
# if script.py --const -> args.suka = 42
# if script.py -> args.suka = None


# ------------------------ action = store_true / store_false -----------
# аналогично как в store=const, но для булевых переменных const=True/False
# if script.py --const -> args.suka = True/False
# if script.py -> args.suka = False/True - наоборот


# ------------------------ action = append ------------------------------
# заполняет список ключами
parser.add_argument('-v', dest='list_', action='append')
# script.py -v A -v B -v V -v D
# list_ = [A, B, C, D]


# ------------------------ action = count ------------------------------
parser.add_argument('--step', '-s', dest='counter', action='count')
# если не указать ни одного ключа -> args.counter=None

# merge all arguments
args = parser.parse_args()

# извлечь значение ключа
print(args.count)