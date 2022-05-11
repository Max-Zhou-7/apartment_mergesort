from Apartment import *
from lab06 import *
def test_conditionalOperator():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    a6 = Apartment(800, 250, "excellent")

    assert a6==a5
    assert a0>a1
    assert a2<a3
    assert a5<a1

def test_ensureSortedAscending():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]



    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True


def test_getBestAndWorst(apartmentList):
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert ensureSortedAscending(apartmentList) == False
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_affordable(apartmentList):
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    
    assert getAffordableApartments(apartmentList, 950) =="(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad\n\
(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average\n"
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
