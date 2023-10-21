import restaurantData as r
def show_info(list):
    info = ["Name: ","Price: ","Rating: ","Street: "]
    for j in range(len(list)-1):
        print(info[j]+list[1:len(list)][j])
    print("_")

print("In welcher Art von Restaurant wollen Sie essen?")
i = 1
for wish in r.types:
    print(str(i)+"."+wish)
    i+=1
numb = input("Wähle eine 1 - 15\n")
food = r.types
for j in range(i):
    if food[int(numb)-1]==r.restaurant_data[j-1][0]:
        show_info(r.restaurant_data[j-1])

