name_switcher = str(input("Enter your nickname:"))
name = name_switcher
del name_switcher

print(name, "wants to say!")
print("...")

name_switcher = str(input("Do you really want to change your nickname? (yes/no)"))

no = "no"
yes = "yes"

if(name_switcher == yes):
    print("OK!")
    name_switcher = str(input("Enter your new nickname:"))
    name = name_switcher
    print(name,", you successfully changed your nickname :)")
if(name_switcher == no):
        print("Сancel")