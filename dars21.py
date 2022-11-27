def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        ism = ism.title()
        baho=input(f"Talaba {ism}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
talabalar=['ali', 'vali', 'muhammad', 'zakariyo']
baholar=bahola(talabalar)
print(baholar)
# def katta_harf(matnlar):
#     matnlar=matnlar[:]
#     for x in range(len(matnlar)):
#         matnlar[x]=matnlar[x].title()
#     return matnlar
# ismlar=['zakariyo', 'ahror', 'abror', 'muhammad']
# yangi_ismlar=katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)