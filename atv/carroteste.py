class Car:
    def __init__(self):
        self.pas = 0
        self.km = 0
        self.gas = 0
        self.lim_pas = 2
        self.lim_gas = 10

    def ent(self):
        if self.pas < self.lim_pas:
            self.pas += 1
        else:
            print("fail: limite de pessoas atingido")
    def tirar(self):
        if self.pas > 0:
            self.pas -= 1
        else:
            print("fail:nao ha ninguem")
    def abast(self, quant):
        self.gas = quant
        if self.gas > self.lim_gas:
            self.gas = self.lim_gas
    def dirig(self, distancia):
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
            return
        gas_prec = distancia / 10
        if self.gas >= gas_prec:
            self.km += distancia
            self.gas = gas_prec
        else:
            print("fail: gasolina insuficente")
                

    def __str__(self):
        
        return "pass:" + str(self.pas)+ "\n" "gas:" + str(self.gas) + "\n" "km:" + str(self.km)
carro = Car()
line = ""
print("digite show, in, abast _quant, dirig _dist, out ou end")
while(line != "end"):
    line = raw_input()
    ui = line.split(" ")
    if ui[0] == "end":
        break
    elif ui[0] == "show":
        print(carro)
    elif ui[0] == "in":
        carro.ent()
    elif ui[0] == "out":
        carro.tirar()
    elif ui[0] == "gas":
        carro.abast(int(ui[1]))
    elif ui[0] == "dirig":
        carro.dirig(int(ui[1]))
        
    else:
        print("fail: comando invalido")
        
print(carro)

