import restaurantData as r
def show_info(list):
    info = ["Name: ","Price: ","Rating: ","Street: "]
    print("______________")
    for label, data in zip(info,list[1:len(list)]):
        print(label+data)
    print("______________")

print("In welcher Art von Restaurant wollen Sie essen?")
i = 1
for i, wish in enumerate(r.types, 1):
    print(str(i)+"."+wish)
while True:
    try:
        numb = input("Wähle eine Zahl zwischen 1 - 15!\n")
        if 1<=int(numb) <= 15:
            break
        else:
            print("Die Zahl muss zwischen 1 und 15 liegen!")
    except ValueError:
        print("Keine gültige Eingabe!")

food = r.types
for j in range(len(r.restaurant_data)):
    if food[int(numb)-1]==r.restaurant_data[j][0]:
        show_info(r.restaurant_data[j])