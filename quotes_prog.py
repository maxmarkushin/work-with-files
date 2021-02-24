#напиши здесь свою программу
with open("quotes.txt","r",encoding= "utf-8") as file:
    data = file.read()
print(data)
with open("quotes.txt","a",encoding= "utf-8") as file:
    a = input("Введите автора")
    file.write("\n"+a)
with open("quotes.txt","r",encoding= "utf-8") as file:
    data = file.read()
print(data)

zitate = input("Хотите добавить еще одну цитату?  (да/нет)")
while zitate != "нет":
    b = input("Введите цитату:")
    with open("quotes.txt","a",encoding= "utf-8") as file:
        file.write("\n"+b)
    c = input("Введите автора:")
    with open("quotes.txt","a",encoding= "utf-8") as file:
        file.write("\n"+c)
    zitate = input("Хотите добавить еще одну цитату?  (да/нет)")
with open("quotes.txt","r",encoding= "utf-8") as file:
    data = file.read()
print(data)