class Calc:
    def __init__(self):
        self.bat = 0
        self.bat_max = 0
    def gastbat(self):
        if self.bat == 0:
            print("fail: bateria insuficiente")
            return 
        self.bat -= 1
        return
    def soma(self, a, b):
        if self.gastbat():
            print(a + b)
    def carreg(self, valor):
        self.bat += valor
        if self.bat > self.bat_max:
            self.bat = self.bat_max
    def __str__(self):
        return "bateria:" + str(self.bat)+ "\n" "BateriaMax:" + str(self.bat_max)


calc = Calc()
print("show, init _bat_max, carreg _valor, soma _a _b, ")
while True:
    ui = raw_input().split(" ")
    if ui[0] == "end":
        break
    elif ui[0] == "show":
        print(calc)
    elif ui[0] == "init":
        calc = calc(int(ui[1]))
    elif ui[0] == "carreg":
        calc.carreg(int(ui[1]))
    else:
        print("fail: comando invalido") 
