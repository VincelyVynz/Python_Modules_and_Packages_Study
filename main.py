import password_generator
from temperature_converter import *
import date_time_study as dts
temp_in_c = 33

temp_in_f = celsius_to_fahrenheit(temp_in_c)
print(temp_in_f)

# Testing password gen
new_password = password_generator.generate_password()
print(new_password)

dts.print_current_time()