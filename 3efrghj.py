class employee:
    def __init__(self,name,id_num,bolim,dolzhnost=None):
        self.id_num=id_num
        self.bolim=bolim
        self.name=name
        self.dolzhnost=dolzhnost
    def shygaru(self):
        print("Aty: ",self.name,", id nomeri:  ",self.id_num ,", bolim: ", self.bolim,", dolzhnost: ",self.dolzhnost)
employee1=employee("Siuzan Meiers",47899,"bukhgalteria")
#employee1.malimet("Siuzan Meiers",47899,"bukhgalteria","VP")
employee1.shygaru()

