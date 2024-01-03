class Family:
    name = "HI"

    def __init__(self,name):
        self.name = name

    #@staticmethod
    def get_family_name(self):
        print(self.name)
        return 22
    @classmethod
    def get_name(clss):
        print(clss.get_family_name(clss.name))
        return 11


f1 = Family("John")
f2 = Family("Sep")

# f1.get_family_name()
# f2.get_family_name()

f1.get_name()