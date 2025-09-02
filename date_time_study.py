import  datetime as  dt

now = dt.datetime.now()

print(f"Today is {now.date()}")
print(f"The current time is {now.strftime("%H:%M:%S")}")

def print_current_time():
    print(f"Today is {now.strftime("%d/%m/%Y, %H:%M:%S")}")