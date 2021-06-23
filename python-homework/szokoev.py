def l_year(y, a):
    if (y > 1582) and ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
        print(str(y) + " Szökőév.")
        return True
    else:
        print(str(y) + " Nem szökőév.")
        return False


user_year = int(input("Adjon meg egy évszámot, hogy ellenőrizhessük, szökőév-e: "))
answer = bool()
f = l_year(user_year, answer)
print(f)