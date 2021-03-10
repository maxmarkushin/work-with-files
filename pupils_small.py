#напиши здесь свою программу

class Pupil: 
    def __init__(self,firstname,name,mark):
        self.firstname=firstname
        self.name=name
        self.mark=mark
pupils=[]
def print_class(pupils):
    for pupil in pupils:
        print(pupil.firstname,pupil.name,"-",pupil.mark)
    print("\n")
    
def print_wellmarkers(pupils):
    print("wellmarkers:")
    for pupil in pupils:
        if pupil.mark==5:
            print(pupil.firstname)
    print("\n")

def count_average(pupils):
    a=0
    for pupil in pupils:
        a= a + pupil.mark
    amount_of_pupils= len(pupils)
    average=a/amount_of_pupils
    print("average of class:",average)
with open("pupils_large_txt.txt","r",encoding= "utf-8") as file:
    for line in file:
        data=line.split(" ")
        pupil=Pupil(data[0],data[1],int(data[2]))
        pupils.append(pupil)
print_wellmarkers(pupils)
count_average(pupils)




