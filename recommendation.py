import restaurantData as r
print("In welcher Art von Restaurant wollen Sie essen?")
i = 1
for wish in r.types:
    print(str(i)+"."+wish)
    i+=1
numb = input("Wähle eine 1 - 15!")
food = r.types
for j in range(i):
    if food[int(numb)-1]==r.restaurant_data[j-1][0]:
        print(r.restaurant_data[j-1])

