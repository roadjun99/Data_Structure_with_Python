from Set_SortedList import SetSorted
from Set_items import itemsSet

setA = SetSorted()
setA.insert(-3)
setA.insert(2)
setA.insert(113)
setA.insert(137)
setA.display("정렬된 집합 A:")

setB = SetSorted()
setB.insert(-3)
setB.insert(2)
setB.insert(113)
setB.insert(137)
setB.display("정렬된 집합 B:")

setC = setA.union(setB)
setC.display("A와 B 합집합:")

setD = setA.intersect(setB)
setD.display("A와 B 교집합:")

setE = setA.difference(setB)
setE.display("A와 B 차집합")

print("A에 1이 포함?:", setA.contains(1))
print("A에 2가 포함?:", setA.contains(2))
print("A 와 B는 같다:", setA == setB)

setF = itemsSet()
setF.insert(7)
setF.insert(-3)
setF.insert(1)
setF.insert(200)
setF.display("정렬되지않은 집합 F")

setG = itemsSet()
setG.insert(7)
setG.insert(-3)
setG.insert(19)
setG.insert(2)
setG.display("정렬되지않은 집합 G")

setV = setF.union(setG)
setV.display("F와 G 합집합:")

setM = setF.intersect(setG)
setM.display("F와 G 교집합:")

setL = setA.difference(setB)
setL.display("A와 B 차집합")

print("F에 1이 포함?:", setF.contains(1))
print("G에 2가 포함?:", setG.contains(2))
print("F 와 G는 같다:", setF == setG)