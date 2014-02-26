class Banane():
    def __init__(self):
        self.peanut = 1
        


a = [Banane(),Banane()]

for b in a:
    print(b.peanut)
    a.append(Banane())
