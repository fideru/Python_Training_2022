# 100 Years Old Practice
import datetime

def century_calculator(age):
    year = datetime.date.today().year
    century = (year - age) + 100
    return century

print((century_calculator(33)))

# Integer ramge sum
def add_it_up(integer):

    try:
        result_value = sum(range(integer +1))
        return result_value
    except:
        TypeError
        return 0

print(add_it_up(5))
