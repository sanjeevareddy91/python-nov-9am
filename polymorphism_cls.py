# polymorphism : Multiple forms(Same methods name but different functonalities.)

    # Method Overriding : Considering the Child Method by overriding Parent method..
    # Method Overloading : 


# Method Overriding:

# class Parent:
#     no_acres = 14

#     def agriculture_info(self):
#         return "This person has {} agriculuture land.".format(self.no_acres)

#     def property_info(self,realestate_count,location):
#         return "{} cents of land is regstered to this person at {}".format(realestate_count,location)


# class Child(Parent):
#     no_acres = 8

#     def agriculture_info(self):
#         return "This person has {} acres agriculuture land.".format(self.no_acres)

#     # def property_info(self,realestate_count,location):
#     #     return "This person has {} cents of land at {}".format(realestate_count,location)


# obj = Child()

# print(obj.agriculture_info())

# Method Overloading: Python doesnot support this feature.


class Child:
    no_acres = 8

    def agriculture_info(self):
        return "This person has {} acres agriculuture land.".format(self.no_acres)

    # def property_info(self,realestate_count,location):
    #     return "This person has {} cents of land at {}".format(realestate_count,location)

    # def property_info(self,realestate_count,city,state):
    #     return "This person has {} cents of land at {} city which is in {} state".format(realestate_count,city,state)


    def property_info(self,**property):
        site_count = 0
        for ele in property:
            if ele not in ['city','state']:
                site_count += property[ele]
        return "He has a property of {} located in {} comes under {} state.".format(site_count,property['city'],property['state'])

obj = Child()

# print(obj.property_info(400,'Hyderabad'))

print(obj.property_info(site1 = 400,city='Hyderabad',state='Telangana'))


print(obj.property_info(site1 = 400,site2 = 300,site3 = 200,city='Bangalore',state='Karnataka'))