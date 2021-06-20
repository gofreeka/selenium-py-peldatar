print("Kérem, adja meg a következő adatokat!")

# ----Adatok bekérése----

fogyasztas_orszagut = float(input("Országúti fogyasztás (liter/100km): ")) # Orszagúti átlag üzemanyag-fogyasztás bekérése

fogyasztas_varos = float(input("Varosi fogyasztás (liter/100km): "))    # Városi átlag üzemanyag-fogyasztás bekérése

tav_orszagut = int(input("Orszagúton megtett Km: "))                    # Országúton megtett út bekérése

tav_varos = int(input("Varosban megtett Km: "))                         # Városban megtett út bekérése

uzemanyag_ara = int(input("Üzemanyag ára (Ft/liter): "))                # Üzemanyag árának bekérése

# ----Számítások és kiírások----

uzemanyag_felhaszn_orszagut = ((fogyasztas_orszagut / 100) * tav_orszagut)  # Országúton felhasznált üzemanyag mennyiség számítása

uzemanyag_felhaszn_varos = ((fogyasztas_varos / 100) * tav_varos)   # Városban felhasznált üzemanyag mennyiség számítása

uzemanyag_oda = uzemanyag_felhaszn_orszagut + uzemanyag_felhaszn_varos  # Üzemanyag fogyasztás számítása csak odaútra
print("Az autó " + str(uzemanyag_oda) + " liter üzemanyagot fogyasztott odaúton")   # Üzemanyag fogyasztás kiíratása csak odaútra

uzemanyag_oda_vissza = uzemanyag_oda * 2    # Üzemanyag fogyasztás számítása oda-vissza
print("Az autó " + str(uzemanyag_oda_vissza) + " liter üzemanyagot fogyasztott oda-vissza") # Üzemanyag fogyasztás kiíratása oda-vissza

koltseg_oda_vissza = uzemanyag_oda_vissza * uzemanyag_ara   # Üzemanyag költség számítása - oda-vissza
print("Költég oda-vissza: " + str(koltseg_oda_vissza) + " Ft")  # Üzemanyag költség kiírása - oda-vissza
