import datetime
import random

SYMBOLS = " QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmik,ol.p!@#$%^&*()_+~`?/.>,<':{}[] "
FOR_NAMES = "QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmik,ol.p"
NAMES = ["Alex", "Boris", "Cavin", "Bob", "Candra", "Debora", "Darya", "Elena", "Helen", "Kate", "Emma", "Emanuel", "Mikle", "Michel", "Rob", "Alexander", "Max", "Lorenc", "Kirill", "Anastasia", "Jane"]
EMAIL_BASE = "qazxswedcrfvtgbyhnujmikolp_-."
DIGITS = "1234567890"


# define variable types INT BOOL DOUBLE FLOAT STRING DATE TUPLE etc...
def build_data_list(columns):
    today_date = datetime.datetime.today()
    temp_list = ["id;name;2name;email;score;double_score;flag;date;string_field"]  # define table header
    for n in range(1, columns):
        id_ = str(n)
        name = NAMES[random.randint(0, len(NAMES)-1)]
        email = NAMES[random.randint(0, len(NAMES)-1)] + generate_string(EMAIL_BASE, 10) + "@gmail.com"
        second_name = generate_string(FOR_NAMES, 10)
        long_field = generate_string(DIGITS, 10)
        float_field = str(round(float(random.randint(0, 99)/7), 4))
        # imitate random value: true, false or empty string
        if n % 7 == 0:
            bool_flag = ""
        else:
            bool_flag = str(bool(random.getrandbits(1)))
        random_string = generate_string(SYMBOLS, 30)
        temp = "%s;%s;%s;%s;%s;%s;%s;%s;%s" % \
               (id_, name, second_name, email, long_field, float_field, bool_flag, str(today_date), random_string)

        temp_list.append(temp)
    return temp_list


def generate_string(base, *args):
    if args:
        n = args[0]
    else:
        n = random.randint(0, 99)
    temp = ""
    for i in range(n):
        temp += base[random.randint(0, len(base) - 1)]
    return temp


def create_file_and_write(data_list, file_type):
    timestamp = str(datetime.datetime.now())[:10] + "_" + str(datetime.datetime.now())[11:-7]
    print(timestamp)
    f = open("test_data_" + timestamp + file_type, "a")
    for i in data_list:
        f.write(str(i) + "\n")
    f.close()


if __name__ == "__main__":
    # generate 100 lines file, adjust amount of line as needed
    create_file_and_write(build_data_list(100), ".csv")
