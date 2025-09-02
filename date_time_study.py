import  datetime as  dt

now = dt.datetime.now()

def print_current_time():
    print(f"Today is {now.strftime("%d/%m/%Y, %H:%M:%S")}")