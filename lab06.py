from Apartment import *

def mergesort(alist):
	if len(alist) > 1:
		mid = len(alist) // 2

		lefthalf = alist[:mid]
		righthalf = alist[mid:]


		mergesort(lefthalf)
		mergesort(righthalf)


		i = 0 
		j = 0 
		k = 0 

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i = i + 1
			else:
				alist[k] = righthalf[j]
				j = j + 1
			k = k + 1

		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		while j < len(righthalf):
			alist[k] = righthalf[j]
			j = j + 1
			k = k + 1

def ensureSortedAscending(apartmentlist): 
    count = 0
    
    for i in range(len(apartmentlist)-1):
        if apartmentlist[i] < apartmentlist[i+1] or apartmentlist[i] == apartmentlist[i+1]:
            count += 1
            #print(count)
    if count == len(apartmentlist)-1:
        return True
    else:
        return False

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    res = ""
    mergesort(apartmentList)
    for i in apartmentList:
        if i.getRent() <= budget:
            res = res + i.getApartmentDetails()+ "\n"
    res= res.rstrip()
    return res

# a0 = Apartment(1115, 215, "bad")
# a1 = Apartment(950, 215, "average")
# a2 = Apartment(950, 215, "excellent")
# a3 = Apartment(950, 190, "excellent")
# a4 = Apartment(900, 190, "excellent")
# a5 = Apartment(500, 250, "bad")


# apartmentList = [a0, a1, a2, a3, a4, a5]


# print('apartmentList is NOT SORTED:')
# for apartment in apartmentList: 
#     print(apartment.getApartmentDetails())

# assert ensureSortedAscending(apartmentList) == False
# mergesort(apartmentList)
# assert ensureSortedAscending(apartmentList) == True

# print('apartmentList is SORTED:')
# for apartment in apartmentList: 
#     print(apartment.getApartmentDetails())

# a0 = Apartment(1200, 200, "average")
# a1 = Apartment(1200, 200, "excellent")
# list1=[a0,a1]

# a2 = Apartment(1000, 100, "average")
# a3 = Apartment(1000, 215, "excellent")
# a4 = Apartment(700, 315, "bad")
# a5 = Apartment(800, 250, "excellent")
# apartmentList = [a0, a1, a2, a3, a4, a5]

# assert ensureSortedAscending(apartmentList) == False

# print('Best Apartment in apartmentList:')
# print(getBestApartment(apartmentList))

# print('Worst Apartment in apartmentList:')
# print(getWorstApartment(apartmentList))
# print(getBestApartment(list1))

# a0 = Apartment(1115, 215, "bad")
# a1 = Apartment(970, 215, "average")
# a2 = Apartment(950, 215, "average")
# a3 = Apartment(950, 190, "excellent")
# a4 = Apartment(900, 190, "excellent")
# a5 = Apartment(500, 250, "bad")
# apartmentList = [a0, a1, a2, a3, a4, a5]

# print('All apartments whose rent is <= in SORTED order:')
# print(getAffordableApartments(apartmentList, 950))
        
