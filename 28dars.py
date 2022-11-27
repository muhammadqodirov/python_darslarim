class User:
    """User nomli klass yaratamiz"""

    def __init__(self,ism, foydalanuvchining_ismi, email, tyil, raqami):
        """Foydalanuvchining xususiyatlari"""
        self.name=ism
        self.user=foydalanuvchining_ismi
        self.email=email
        self.tyil=tyil
        self.number=raqami
    def get_name(self):
        return self.name
    def get_username(self):
        return self.user
    def get_age(self, x):

        return x-self.tyil
    # def get_info(self):
    #     print(f"Foydalanuvchi: {self.user}  {self.tyil} yilda tig'ilgan. Ismi {self.name}, {self.email} pochta orqali yoki,\n{self.number} raqami bo'yicha murojaat qilsangiz bo'ladi")

user1=User("Muhammadxo'ja","Muhammad","kodirovmuhammad791@gmail.com",2001,333773300)
user2=User("Emil","Emil","shokirovemil@gmail.com",2000,555552222)
user3=User("Ahror","Ahrorchik","mamadjonovahror@gmail.com",2001,330103000)
user4=User("Zakariyo","Dolimov","dolimovzakariyo@gmail.com",2000,337773377)
print(user1.get_name())
print(user1.get_age(2022))
# user1.get_info()
# user2.get_info()
# user3.get_info()
# user4.get_info()
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")




# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Olim","Olimov",1995)
# talaba3 = Talaba("Husan","Akbarov",2004)
# talaba4 = Talaba("Hasan","Akbarov",2004)
# print(talaba4.tyil)
# print(talaba2.ism)
# print(t
# alaba4.familiya)
# talaba4 = Talaba("Hasan","Akbarov",2004)
# talaba4.tanishtir()
