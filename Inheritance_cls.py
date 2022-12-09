# # Inheritance : A class getting the properties from some other class..

# # 1) Single Inheritance : 
# # 2) Multiple Inheritance
# # 3) Multilevel Inheritance
# # 4) Hybrid Inheritance
# # 5) Hierical Inheritance


# # Single Inheritance : Child class getting the properties from Parent class..

# # class Parent:
# #     no_acres = 14

# #     def agriculture_info(self):
# #         return "This person has {} agriculuture land.".format(self.no_acres)

# #     def property_info(self,realestate_count,location):
# #         return "{} cents of land is regstered to this person at {}".format(realestate_count,location)


# # class Child(Parent):
# #     # no_acres = 8

# #     def agriculture_info(self):
# #         return "This person has {} acres agriculuture land.".format(self.no_acres)

# #     # def property_info(self,realestate_count,location):
# #     #     return "This person has {} cents of land at {}".format(realestate_count,location)


# # obj = Child()

# # print(obj.no_acres)

# # print(obj.agriculture_info())

# # print(obj.property_info(200,"Gachibowli"))

# # obj1 = Parent()


# # 2) Multiple Inheritance() -- A child class getting the properties from multiple parent classes..


# # class Father:
# #     no_acres = 14

# #     def agriculture_info(self):
# #         return "This person has {} agriculuture land.".format(self.no_acres)

# # class Mother:
# #     no_acres = 10

# #     def agriculture_info(self):
# #         return "His mother has {} acres of agriculture land.".format(self.no_acres)

# #     def property_info(self,realestate_count,location):
# #         return "{} cents of land is regstered to this person at {}".format(realestate_count,location)

# # class Child(Mother,Father):  # inheritance will be done based on the order we follow during inheriting
# #     # no_acres = 8
# #     pass

# #     def agriculture_info(self):
# #         return "This person has {} acres agriculuture land.".format(self.no_acres)

# #     # def property_info(self,realestate_count,location):
# #     #     return "This person has {} cents of land at {}".format(realestate_count,location)

# #     # def agriculture_info(self):
# #     #     return "This person has {} acres agriculuture land.".format(Father.no_acres)

# # obj = Child()

# # print(obj.no_acres)

# # print(obj.agriculture_info())


# # 3) Multilevel Inheritance() : A class getting the properties from Parent class and that parent again getting the properties from Its parent(Grand Parent).


# class GrandFather:
#     # no_acres = 14

#     def agriculture_info(self):
#         return "His Grandfather has {} agriculuture land.".format(self.no_acres)

# # class Father(GrandFather):
# #     # no_acres = 10

# #     def agriculture_info(self):
# #         return "His father has {} acres of agriculture land.".format(self.no_acres)

# #     def property_info(self,realestate_count,location):
# #         return "{} cents of land is regstered to this person at {}".format(realestate_count,location)

# # class Mother():
# #     no_acres = 6

# #     def agriculture_info(self):
# #         return "His father has {} acres of agriculture land.".format(self.no_acres)

# #     def property_info(self,realestate_count,location):
# #         return "{} cents of land is regstered to this person at {}".format(realestate_count,location)

# # class Child(Father,Mother):  # inheritance will be done based on the order we follow during inheriting
# #     # no_acres = 8
# #     pass

# #     def agriculture_info(self):
# #         return "This person has {} acres agriculuture land.".format(self.no_acres)

# #     def property_info(self,realestate_count,location):
# #         return "This person has {} cents of land at {}".format(realestate_count,location)

# #     # def agriculture_info(self):
# #     #     return "This person has {} acres agriculuture land.".format(Father.no_acres)

# # obj = Child()

# # print(obj.no_acres)

# # print(obj.agriculture_info())

# # 4) Hierircal Inheritance: Multiple child classes are getting the properties from 1 parent..

# class Father():
#     no_acres = 10

#     def agriculture_info(self):
#         return "His father has {} acres of agriculture land.".format(self.no_acres)

#     def property_info(self,realestate_count,location):
#         return "{} cents of land is regstered to this person at {}".format(realestate_count,location)

# class Child1(Father):
#     # no_acres = 6

#     def agriculture_info(self):
#         return "His father has {} acres of agriculture land.".format(self.no_acres)

#     def property_info(self,realestate_count,location):
#         return "{} cents of land is regstered to this person at {}".format(realestate_count,location)

# class Child2(Father): 
#     # no_acres = 8
#     pass

#     def agriculture_info(self):
#         return "This person has {} acres agriculuture land.".format(self.no_acres)

#     def property_info(self,realestate_count,location):
#         return "This person has {} cents of land at {}".format(realestate_count,location)

#     # def agriculture_info(self):
#     #     return "This person has {} acres agriculuture land.".format(Father.no_acres)

# obj1 = Child2()

# obj2 = Child1()

# print(obj1.no_acres)
# print(obj2.no_acres)

# # 5) Hybrid Inheritance() -- Combination of any of the inheritances..


# # !,$,@,_