import password_utils
from temperature_converter import *
from password_utils import *
temp_in_c = 33

temp_in_f = celsius_to_fahrenheit(temp_in_c)
print(temp_in_f)


# Testing password gen
new_password = password_utils.generate_password(4,3,2)
print(new_password)