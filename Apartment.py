
class Apartment():
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition 
    
    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}"\
            .format(self.rent, self.metersFromUCSB, self.condition)
    def __gt__(self, rhs): #greater function comparing the order of apartment 
        # if the order of apartment in the list is in the behind of the order of 
        #other apartment than it should return True
        if self.rent > rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB == rhs.metersFromUCSB:
                return len(self.condition) < len(rhs.condition)
                    
            else:
                return False

        else:
            return False

    # def __lt__(self,rhs): # less than is order of apartment 越靠前越True
    #     if self.rent > rhs.rent:
    #         return False
    #     elif self.rent == rhs.rent:
    #         if self.metersFromUCSB > rhs.metersFromUCSB:
    #             return False
    #         elif self.metersFromUCSB == rhs.metersFromUCSB:
    #             return len(self.condition) > len(rhs.condition)
    #         else:
    #             return True
    #     else:
    #         return True
    def __lt__(self, rhs): #greater function comparing the order of apartment 
        # if the order of apartment in the list is in the behind of the order of 
        #other apartment than it should return True
        if self.rent < rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.metersFromUCSB < rhs.metersFromUCSB:
                return True
            elif self.metersFromUCSB == rhs.metersFromUCSB:
                return len(self.condition) > len(rhs.condition)
                    
            else:
                return False

        else:
            return False

    def __eq__(self,rhs):
        if self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and len(self.condition) == len(rhs.condition):
             return True
        else:
            return False
# a0 = Apartment(1200, 200, "average")
# a1 = Apartment(1200, 200, "excellent")
# a2 = Apartment(1000, 100, "average")
# a3 = Apartment(1000, 215, "excellent")
# a4 = Apartment(700, 315, "bad")
# a5 = Apartment(800, 250, "excellent")
# a6 = Apartment(800, 250, "excellent")

# assert a6==a5
# assert a0>a1
# assert a2<a3
# assert a5<a1




# a0 = Apartment(1204, 200, "bad")
# print(a0.getApartmentDetails())

