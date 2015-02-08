class Slist:
       count = 0
       def __init__(self, name,element ):
              self.name = name
              Slist.count += 1
       def add_in_list(self, a):
              element.append(a)

       def show(self):
              print("Name of the list is :", self.name)
              for value in element:
                     print("The number is :", value)
                     
element = []
slist = Slist("Integer",element)
print ("the number of this class:", slist.count)

slist.add_in_list(12)
slist.add_in_list(5)
slist.add_in_list("lijianlin")

slist.show()
print("Slist.doc:", Slist.__doc__)
print("Slist.name:", Slist.__name__)
print("Slist.module:",Slist.__module__)
#print("Slist.dict:",Slist.__dict__)
print("Slist.bases:",Slist.__bases__)

slist2 = Slist("Integer2",element)
print ("the number of this class:", slist2.count)
