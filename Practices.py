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
        result_value = sum(range(integer + 1))
        return result_value
    except:
        TypeError
        return 0


print(add_it_up(5))

# Most Repeated Character on Text

sentence = "This is a common interview question"
char_dict = {}
for i in sentence:
    if i in char_dict:
        char_dict[i] += 1
    else:
        char_dict[i] = 1

final = sorted(char_dict.items(), key=lambda kv: kv[1], reverse=True)
print("The maximum repeated value is: ", final[0])
