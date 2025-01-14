import psycopg2
import random
from xlwt import Workbook

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
result = con.execute("SELECT per_name,dpt_code,fac_designation FROM public.vw_usr_faculty WHERE usr_active=true ORDER BY dpt_code")

def check_sequenced(first, second, third):
    """
    Check if the three numbers form a sequence.
    """
    return first > 0 and second > 0 and third > 0

def reorganize(arr, limit):
    """
    Reorganize the array such that no more than `limit` elements are adjacent.
    """
    i = 0
    while i < len(arr) - limit:
        # Check if elements exceed the limit consecutively
        if all(arr[i + j] > 0 for j in range(limit + 1)):
            # Move the last element in the sequence to a new position
            temp = arr[i + limit]
            arr[i + limit] = 0

            # Find a new position for `temp` where it doesn't break the limit
            for j in range(i + limit + 1, len(arr)):
                if arr[j] == 0:
                    arr[j] = temp
                    break

        i += 1

    # Verify if the array satisfies the condition
    if not is_valid(arr, limit):
        print("The array could not be reorganized correctly.")

    return arr

def is_valid(arr, limit):
    """
    Check if the array satisfies the limit condition.
    """
    count = 0
    for num in arr:
        if num > 0:
            count += 1
            if count > limit:
                return False
        else:
            count = 0
    return True

def check(a, n):
    for i in a:
        if i == n:
            return True
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
            #recurive(arr, limit)
            arr = reorganize(arr, 2)
        else:
            continue
    arr.sort()
    return arr

def remove_duty(arr,max):
    j = 0

    times = arr.count(1) - max
    while j < times:
        for i in range(0, len(arr)):
            n = random.randrange(0,30)
            if arr[n] == 1:
                arr[n] = 0
                j +=1
            if j>= times:
                break

    return arr

def find_position(arr,n):
    flag = False
    if n >= len(arr) - 2:
        count = arr[n - 1] + arr[n - 2]
        print("Segment 1")
        # print(arr,n, count, "OK")
        if count < 2:
            arr[n] = 1
            flag = True
        # print(arr)

def add_duty(arr, max):
    # Calculate how many 1's need to be added
    times = max - arr.count(1)
    j = 0

    while j < times:
        placed = False  # Track if a `1` was placed during this iteration

        for n in range(len(arr)):
            if arr[n] == 0:  # Check if the current position is empty
                # Check left and right neighbors
                left_valid = (n == 0 or arr[n - 1] == 0)
                right_valid = (n == len(arr) - 1 or arr[n + 1] == 0)
                #print(n)
                if left_valid and right_valid:
                    arr[n] = 1
                    j += 1
                    placed = True
                    break  # Move to the next iteration of the while loop
                else:
                    if n>0 and n<len(arr)-2:
                        if arr[n+1] ==0 or arr[n-1] ==0:

                            arr[n] = 1
                            j += 1
                            placed = True
                            break  # Move to the next iteration of the while loop


        if not placed:
            # If no valid position is found in the loop, terminate to prevent infinite loop
            print("No more valid positions to place 1.")
            break

    return arr

def get(limit, max, shift):
    arr = []
    count = 0
    for i in range(0, shift):
        arr.append(0)
    while count <= limit:
        for i in range(0, shift):
            n = random.randrange(0, shift)
            if check(arr, n) == False:
                arr[n] = 1
                count += 1
            else:
                continue
        #print(arr)
        #arr.sort()
        arr = reorganize(arr, 2)

        #print(arr.count(1))
   # print("Before",arr, arr.count(1))
    #arr = add_duty(arr, max)

    if arr.count(1)>max:
        arr = remove_duty(arr, max)
    elif arr.count(1)<max:
        arr = add_duty(arr, max)
    #print("After",arr, arr.count(1))

    return arr
# Input array and limit

def write_data(wb,sheet1, shift, result, invigilatos, limit):
    for i in range(1, shift + 1):
        sheet1.write(0, i, i)

    row = 1
    for r in result:
        sheet1.write(row, 0, r[0])
        row += 1

    row = 1
    for i in range(0, invigilatos):
        arr = get(limit, 12, shift)
        col = 1
        for a in arr:
            # print(a)
            sheet1.write(row, col, a)
            col += 1
        row += 1

    wb.save('xlwt example.xls')
    print("Successfully Created Roster File!!!")

def make_shifts2(wb,sheet1, totaldays):
    days = range(1, totaldays)
    shifts = {"M", "E", "N"}

    shifts_list = []

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
    col = 2
    for x in data:
        dic =[]
        for y in x:
            if y != '':
                dic.append(y)
                if y.isdigit()==False:
                    sheet1.write(0, col, y)
                    col +=1
        shifts.append(dic)

    return shifts

def make_shifts(wb,sheet1, totaldays):
    col = 2
    for day in range(0, totaldays):
        if day%2==0:
                sheet1.write(0, col, 'M')
                col +=1
                sheet1.write(0, col, 'E')
                col += 1

        else:
                sheet1.write(0, col, 'M')
                col += 1
                sheet1.write(0, col, 'E')
                col += 1
                sheet1.write(0, col, 'N')
                col += 1

def f():
    try:
        arr = []

        invigilatos = len(result)

        shift = 20
        A = [invigilatos, shift]

        _size = (len(A) + invigilatos) - 2
        #print(_size)
        B = [[0]*shift for x in range(_size)]


        limit = 2


        wb = Workbook()

        sheet1 = wb.add_sheet("Roster")

        #write_data(wb,sheet1, shift, result, invigilatos, limit)

        make_shifts(wb,sheet1, 8)

        row = 1
        for r in result:
            sheet1.write(row, 0, r[0])
            sheet1.write(row, 1, r[2])
            row +=1

        row = 1
        for i in range(0, invigilatos):
            arr = get(limit, 12, shift)
            col = 2
            for a in arr:
                #print(a)
                sheet1.write(row,col,a)
                col +=1
            row +=1

        wb.save('DutyRoster.xls')
        print("Successfully Created Roster File!!!")
    except:
        print("Something went wrong! Please try again.")


if __name__ == '__main__':
    f()

