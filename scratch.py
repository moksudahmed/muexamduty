import psycopg2
import random
from numpy import *

class Connection:
    def __init__(self):
        self.con = psycopg2.connect(database="db_muERPv8p0",
                               host="localhost",
                               user="postgres",
                               password="success8085.com",
                               port=8085)

        self.cur = self.con.cursor()
        self.cur.execute("SELECT * from public.tbl_j_person")
        self.result = self.cur.fetchall()

    def execute(self, query):
        self.cur.execute(query)
        self.result = self.cur.fetchall()
        return self.result

con = Connection()
result = con.execute("SELECT * FROM public.vw_usr_faculty WHERE dpt_code='ENG'")

def make_shifts():
    days = range(1, 13)
    shifts = {"M", "E", "N"}

    shifts_list = []

    print((type(shifts_list)))
    for day in days:
        txt = f"{day}-"

        for shift in shifts:
            if (day % 2 != 0):
                    txt = txt + f"{shift}-"
            else:
                if shift == 'M' or shift == 'E':
                    txt = txt + f"{shift}-"
        shifts_list.append(txt)
    data = [item.replace(' ', '').split('-') for item in shifts_list]
    shifts =[]
    for x in data:
        dic =[]
        for y in x:
            if y != '':
                dic.append(y)
        shifts.append(dic)
    return shifts

shifts = make_shifts()

def get_total_shifts():
    count = 0
    for x in shifts:
        for y in x:
            count +=1
    return count

def get_faculty():
    num = random.randrange(1, 80)
    return result[num][2]

def get_header():
    header=[]
    header.append('Faculty Name')
    for x in shifts:
       for y in x:
           if y =='M' or y=='E' or y=='N':
             header.append(y)
    return header

def draw():
    for f in result:
        txt = f"{f[1]} {f[2]}|"
        sh =''
        for i in range(1, get_total_shifts()):
            if i%2==0:
                sh = f"{sh}|*"
            else:
                sh = f"{sh}| "
        shift = f"{txt}|{sh}|"
        print(shift)

def draw_shcedule():
    rows = len(result)
    cols = 30
    #duty_roster = [[0]*cols]*rows
    duty_roster = [[ 0 for i in range(rows)] for j in range(cols)]
    print(duty_roster)
    for i in range(rows):
        for j in range(6):
            if i%2 == 0:
                duty_roster[i][j] = 2
    i = 0
    temp = []

    return duty_roster
#print(get_faculty())

header = get_header()

#print(header)
#draw()
#roster = draw_shcedule()
#for r in roster:
#    print(r, end='\n')
invigilatos = len(result)

shift = 30
A = [invigilatos, shift]

#print(invigilatos)

_size = (len(A) + invigilatos) - 2
#print(_size)
B = [[0]*shift for x in range(_size)]
import random

limit = 16

def check(a, n):
    for i in a:
        if i == n:
            return True
    return False


def check_sequenced(first, second, third):
    temp = (third - (second - first))
    if first>0 and second>0 and third>0:
        return True
    else:
        return False

def recurive(arr, l):
    for i in range(0, len(arr)):
        if check_sequenced(arr[i-2], arr[i-1],arr[i]):
            n = random.randrange(0, 30)
            #print("Sequenced",i)
            arr[i] = n
            return recurive(arr, l)
        else:
            continue
            #print("Not Sequenced")
    count = 0
    for i in arr:
        if i>0:
           count +=1
        #else:continue

    if count>= l:
        print(count)
        return False


def get_duty():
    arr = []
    count = 0

    for i in range(0, 30):
       n = random.randrange(0, 30)
       if check(arr, n) == False:
          arr.append(n)
          count +=1
       else: continue
       if count == limit:
           break
    arr.sort()
    for i in range(0, len(arr)):
        if check_sequenced(arr[i-2], arr[i-1],arr[i]):
            recurive(arr, limit)
        else:
            continue
    arr.sort()
    return arr

for i in range(invigilatos):
    temp = random.randrange(0, 1)
    count = 0
    total = 0
    for j in range(temp, shift):
        count += 1
        if count <= 2:
            B[i][j] = 0
            total = total + count
        else:
            count = 0
            continue

        if total == limit:
            break

for i in range(invigilatos):
    #arr = get_duty(arr)
    for j in get_duty():
        B[i][j] = j

for i in B:
    print(i)

