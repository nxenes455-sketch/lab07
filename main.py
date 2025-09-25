
a = 5.0  
b = 3.0  

print("Shuma:", round(a + b, 2))
print("Diferenca:", round(a - b, 2))
print("Produkti:", round(a * b, 2))

if b == 0:
    print("Pjesetimi: Nuk lejohet ndarja me zero!")
else:
    print("Pjesetimi:", round(a / b, 2))
    print("Pjesetimi_i_plote:", int(a // b))
    print("Mbetja:", round(a % b, 2))

print("Fuqi a^2:", round(a ** 2, 2))
print("Fuqi b^3:", round(b ** 3, 2))



mosha = 20 
karte = "jo" 
buxheti = 100.0  
cmimi = 50.0 
zbritje_lejuar = mosha < 18 or mosha >= 65 or karte == "po"
blerja_mundur = buxheti >= cmimi
oferta_speciale = (500 <= cmimi <= 2000) and (16 <= mosha <= 25)

print("Zbritje e lejuar:", "PO" if zbritje_lejuar else "JO")
print("Blerja e mundur:", "PO" if blerja_mundur else "JO")
print("Oferta speciale:", "PO" if oferta_speciale else "JO")



emri = "noel"
mosha = 25  
cmimi_baze = 1000.0 
kupon = "po" 
if len(emri) < 2 or not (10 <= mosha <= 99) or cmimi_baze <= 0:
    print("Te dhenat jane te pavlefshme. Kontrollo emrin, moshen dhe cmimin.")
else:
    zbritje = 0
    if mosha < 18 or mosha >= 65:
        zbritje += 10
    if kupon in ["po", "yes", "y"]:
        zbritje += 5
    if mosha <= 23 and cmimi_baze >= 1000:
        zbritje += 3 

    vlere_zbritje = cmimi_baze * zbritje / 100
    pas_zbritjes = cmimi_baze - vlere_zbritje
    tvsh = pas_zbritjes * 0.15
    total = pas_zbritjes + tvsh

    print("------------------------------")
    print(f"Klient: {emri} (mosha {mosha})")
    print(f"Cmimi baze: {format(cmimi_baze, '.2f')} Lek")
    print(f"Zbritje totale: {zbritje}% (vlere: {format(vlere_zbritje, '.2f')} Lek)")
    print(f"Pas zbritjes: {format(pas_zbritjes, '.2f')} Lek")
    print(f"TVSH (15%): {format(tvsh, '.2f')} Lek")
    print(f"Totali: {format(total, '.2f')} Lek")
