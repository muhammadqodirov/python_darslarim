one = 'Naharis'
two = 'Mormont'
three = 'Sand'

# BEGIN (write your solution here)

# END
# Третий символ из первой строки
# Второй символ из второй строки
# Четвертый символ из третьей строки
# Пятый символ из второй строки
# Третий символ из второй строки
print(f"{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}")
stark = 'Arya'

# BEGIN (write your solution here)

# END
# Do you want to eat, Arya?
# Yes, I'm hungry, mom.
# print(f"Do you want to eat, {stark}?\nYes, I'm hungry , mom.")
print(f"""Do you want to eat, {stark}? Yes, I'm hungry, mom.""")
king = 'King Balon the 6th'

# BEGIN (write your solution here)

# END
ancestors = str(6*17)
# anc=str(ancestors)
print(king + ' has ' + ancestors + ' rooms.')

name='Dragon'
print(name)
# print('-Did Joffrey agree?\n-He did. He also said "I love using \\n".')
# print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')
# class Talaba:
#     def __init__(self,ism, familiya, pasport, tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.pasport=pasport
#         self.tyil=tyil
#         self.fanlar=[]
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil} da tug'ilgan"
#
#
# talaba=Talaba('Muhammad','Qodirov','AB733159',2001)
# print(talaba.get_info())
# class Fan:
#     def __init__(self,nomi,sinf,yil):
#         self.nomi=nomi
#         self.sinf=sinf
#         self.yil=yil
#     def fanga_yozil(self):








# class Shaxs:
#     def __init__(self, ism, familiya, pasport, tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.pasport=pasport
#         self.tyil=tyil
#
#     def get_info(self):
#         info=f"{self.ism} {self.familiya}\n"
#         info+=f"Pasport: {self.pasport}\n{self.tyil} yilda tug'ilgan."
#         return info
#     def get_age(self, yil):
#         return yil - self.tyil
# inson = Shaxs("Muhammad","Qodirov","AB7333159",2001)
# print(f"{inson.get_info()} {inson.get_age(2022)} yoshda")
#
# # class Talaba(Shaxs):
# #     def __init__(self, ism, familiya, pasport, tyil):
# #         super().__init__(ism,familiya,pasport,tyil)
# # talaba = Talaba("Valijon","Aliyev","FA112299",2000)
# # print(talaba.get_info())
# # print(talaba.get_age(2022))
# # class Talaba(Shaxs):
# #     def __init__(self, ism, familiya, pasport, tyil,id_raqam):
# #         super().__init__(ism,familiya,pasport,tyil)
# #         self.id_raqam=id_raqam
# #         self.bosqich=1
# # talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
#
#
# class Talaba(Shaxs):
#     """Talaba klassi"""
#
#     def __init__(self, ism, familiya, passport, tyil, id_raqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.id_raqam = id_raqam
#         self.bosqich = 1
#
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.id_raqam
#
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")
# print(f"{talaba.get_bosqich()}-bosqich talabasi")
#
#
