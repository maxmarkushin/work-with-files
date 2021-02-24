#напиши здесь свою программу
with open("quotes.txt","r",encoding= "utf-8") as file:
    data = file.read()
print(data)
with open("quotes.txt","a",encoding= "utf-8") as file:
    a = input("Введите автора")
    file.write(a)
with open("quotes.txt","r",encoding= "utf-8") as file:
    data = file.read()
print(data)



