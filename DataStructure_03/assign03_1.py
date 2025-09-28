# LIST -> Python 리스트 사용
class Polynomial:
    def __init__(self):
        self.coef = []

    def read(self):
        n = int(input("다항식 최고 차수 입력 :"))
        for i in range(n, -1, -1):
            coef_el=int(input("x^%d의 계수 :" % i))
            self.coef.append(coef_el)
        self.coef.reverse()

    def degree(self):
        return len(self.coef)-1

    def evaluate(self,scalar):
        coef_ev_sum=0
        for i in range(len(self.coef)):
            coef_ev_sum+=self.coef[i]*(scalar**i)
        return coef_ev_sum

    def add(self,rhs):
        if(len(self.coef)>len(rhs.coef)):
            for i in range(len(rhs.coef)):
                coef_add = self.coef[i] + rhs.coef[i]
                self.coef[i] = coef_add
            return self
        else:
            for i in range(len(self.coef)):
                coef_add = self.coef[i] + rhs.coef[i]
                rhs.coef[i] = coef_add
            return rhs

    def sub(self,rhs):
        neg_rhs=Polynomial()
        neg_rhs.coef=[-x for x in rhs.coef]
        return self.add(neg_rhs)

    def multiply(self,rhs):
        coef_multi=Polynomial()
        coef_multi.coef=[0]*(len(self.coef)+len(rhs.coef)-1)
        for i in range(len(self.coef)):
            for j in range(len(rhs.coef)):
                coef_multi.coef[i+j] += self.coef[i] * rhs.coef[j]

        return coef_multi

    def display(self,message):
        message+=f'{self.coef[-1]}x^{len(self.coef)-1}'
        for i in range(len(self.coef)-2,-1,-1):
            if(self.coef[i]>0):
                message+=f' +{self.coef[i]}x^{i}'
            elif(self.coef[i]<0):
                message+=f' {self.coef[i]}x^{i}'
            else:
                pass

        return f'{message}'

a=Polynomial()
b=Polynomial()
a.read()
b.read()
c=a.add(b)
d=a.sub(b)
e=a.multiply(b)
print(a.degree())
print("C(2) = ",a.evaluate(2))
print(a.display("A(x) = "))
print(b.display("B(x) = "))
print(c.display("C(x) = "))
print(d.display("D(x) = "))
print(e.display("E(x) = "))