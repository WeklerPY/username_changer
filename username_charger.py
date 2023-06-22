name_switcher = str(input("Введите свой никнейм:"))
name = name_switcher
del name_switcher

print(name, "хочет сказать!")
print("...")

name_switcher = str(input("Ты действительно хочешь сменить ник?(yes/no)"))

no = "no"
yes = "yes"

if(name_switcher == yes):
    print("Хорошо!")
    name_switcher = str(input("Введи свой новый ник:"))
    name = name_switcher
    print(name,", ты успешно изменил ник :)")
if(name_switcher == no):
        print("Отмена!")