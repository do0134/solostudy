class Family:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def get_family_name(self):
        print(self.name)


f1 = Family("John")
f2 = Family("Sep")

f1.get_family_name()
f2.get_family_name()