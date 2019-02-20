# class Chief:
#     def __init__(self, armor, weapon, armor_color):
#         self.armor = armor
#         self.weapon = weapon
#         self.armor_color = armor_color
    
#     # def kill():
#     #     print('Chief is killing convenant scum')

#     # def drive():
#     #     print('steal a ghost')

#     def chief(self):
#         print('oi')

#     def chief1(self, weapon):
#         self.weapon = 'carabine'
#         print(chief1.weapon)

# # obj_chief = Chief('carabine','q','green')
# # print(obj_chief.armor)
# x = Chief(2,2,'oi')
# x.chief()

class Car:

    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
    
    def buzz(self):
        print('buzinando')
    def dejavu(self):
        print('drift')

car1 = Car('red', 'Ferrari', 'FF')

car1.dejavu()

