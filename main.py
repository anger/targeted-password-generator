print("""inp
Targeted Password Generator
github.com/anger

Please answer all questions provided the best you can. If you do not know the answer, or are unsure, please press enter. DOB is a required input.
""")

list = []
names = []
temp_names = []
phone_number = ''
dob = input("Enter Birthday (DDMMYYYY):")
if (len(dob) == 8):
    day = dob[:2]
    month = dob[2:4]
    year = dob[4:]
else:
    print("ERROR OCCURED: Wrong format detected for birthday, please enter 8 numbers in DDMMYYYY format")
    exit()

phone_number = input("Enter phone number:")


def imp_info():
    names.append(input("First name:\n"))
    names.append(input("Last name:\n"))
    names.append(input("Nickname:\n"))
    names.append(input("Significant other/Best Friend name:\n"))
    names.append(input("Significant other/Best Friend Nickname:\n"))
    names.append(input("Pet's name:\n"))
    names.append(input("Company name:\n"))
    names.append(input("Child's name:\n"))
    names.append(input("Child's nickname:\n"))
    names.append(input("City:\n"))
    names.append(input("Country:\n"))
    names.append(input("Favourite color:\n"))
    print("Enter all other keywords (Parents, friends, hobbies, passions): ")
    while True:
        val_input = input()
        if val_input == '':
            break
        names.append(val_input)
    while ('' in names):
        names.remove('')


def permute(val_input):
    n = len(val_input)

    mx = 1 << n

    val_input = val_input.lower()

    for i in range(mx):
        combo = [k for k in val_input]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combo[j] = val_input[j].upper()

        temp = ""
        for i in combo:
            temp += i
        temp_names.append(temp)


def make_list(list):
    for word in names:
        for i in range(0, len(word) + 1):
            list.append(word[:i] + day + word[i:])
            list.append(word[:i] + month + word[i:])
            list.append(word[:i] + year + word[i:])
            if len(year) == 4:
                list.append(word[:i] + year[2:] + word[i:])
            list.append(word[:i] + phone_number + word[i:])
    if not phone_number == '':
        list.append(phone_number)


def make_file(list):
    with open('output.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)


imp_info()
for i in names:
    permute(i)
names = names + temp_names
make_list(list)
make_file(list)
print("output.txt has been created")
