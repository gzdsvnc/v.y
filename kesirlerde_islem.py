def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

class Kesir:
    def __init__(self,pay,payda):
        obeb = gcd(pay,payda)
        self.payim = pay / obeb
        self.paydam = payda / obeb
    def __str__(self):
        return str(self.payim) + "/" + str(self.paydam)
    def __add__(self,diger):
        yeni_pay = self.payim * diger.paydam + self.paydam * diger.payim
        yeni_payda = self.paydam * diger.paydam
        sonuc1 = Kesir(yeni_pay,yeni_payda)
        return sonuc1
    def __sub__(sel,diger):
        yeni_pay = self.payim * diger.paydam - self.paydam * diger.payim
        yeni_payda = self.paydam * diger.paydam
        sonuc2 = Kesir(yeni_pay,yeni_payda)
        return sonuc2
    def __mul__(self,diger):
        yeni_pay = self.payim * diger.payim
        yeni_paydam = self.paydam * diger.paydam
        sonuc3 = Kesir(yeni_pay,yeni_payda)
        return sonuc3
    def __div__(self,diger):
        yeni_pay = self.payim * diger.paydam
        yeni_paydam = self.paydam * diger.payim
        sonuc4 = Kesir(yeni_pay,yeni_payda)
        return sonuc4


