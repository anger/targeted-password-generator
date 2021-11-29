print("""
Password Wordlist Generator

Answer all questions to the best of your ability, those you do not know, press enter. Date of birth is a necessary input.
""")

list = []
names = []
temp_names = []
phoneNumber = ''
dateOfBirth = input("Date of birth(DDMMYYYY):")
if (len(dateOfBirth) == 8):
    day = dateOfBirth[:2]
    month = dateOfBirth[2:4]
    year = dateOfBirth[4:]
else:
    print("ERROR: Wrong format detected for dateOfBirth, please enter 8 numbers in the format of DDMMYYYY")
    exit()

phoneNumber = input("Enter phone no:")


def importantWords():
    names.append(input("First name:"))
    print("\n")
    names.append(input("Last name:"))
    print("\n")
    names.append(input("Nickname:"))
    print("\n")
    names.append(input("Significant other/Best Friend name:"))
    print("\n")
    names.append(input("Significant other/Best Friend Nickname:"))
    print("\n")
    names.append(input("Pets name:"))
    print("\n")
    names.append(input("Company name:"))
    print("\n")
    names.append(input("Child's name:"))
    print("\n")
    names.append(input("Child's nickname:"))
    print("\n")
    names.append(input("City:"))
    print("\n")
    names.append(input("Country:"))
    print("\n")
    names.append(input("Favourite color:"))
    print("\n")
    print("Enter all other keywords (Parents, friends, hobbies, passions): ")
    while True:
        inp = input()
        if inp == '':
            break
        names.append(inp)
    while ('' in names):
        names.remove('')


def permute(inp):
    n = len(inp)

    mx = 1 << n

    inp = inp.lower()

    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()

        temp = ""
        for i in combination:
            temp += i
        temp_names.append(temp)


def generateList(list):
    for word in names:
        for i in range(0, len(word) + 1):
            list.append(word[:i] + day + word[i:])
            list.append(word[:i] + month + word[i:])
            list.append(word[:i] + year + word[i:])
            if len(year) == 4:
                list.append(word[:i] + year[2:] + word[i:])
            list.append(word[:i] + phoneNumber + word[i:])
    if not phoneNumber == '':
        list.append(phoneNumber)


def fileCreate(list):
    with open('output.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)


importantWords()
for i in names:
    permute(i)
names = names + temp_names
generateList(list)
fileCreate(list)
