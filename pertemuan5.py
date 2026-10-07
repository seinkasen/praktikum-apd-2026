#=======================================================
#LIST

#Contoh List
#formula1 = ["mclaren", "ferrari", "red bull", 2, 3, 1]
#print(formula1)

#sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
#print(sirkuit)

#Update List menggunakan .append()
#['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
#sirkuit.append("Spa-Francorchamps")
#print(sirkuit)

#Extend List menggunakan .extend()
#sirkuit.extend(["Spa-Francorchamps", "Interlagos"])
#print(sirkuit)

#Menyisipkan List menggunakan .insert()
#sirkuit.insert(2, "Interlagos")
#print(sirkuit)

#Menimpa List menggunakan index
#sirkuit[1] = "Monza Italia"
#print(sirkuit)

#Mengubah Elemen dengan metode slicing
#sirkuit[0:2] = ["Sepang", "Mugello"]
#print(sirkuit)

#Menghapus Elemen menggunakan del dan index
#del sirkuit[2]
#print(sirkuit)

#Menghapus Elemen menggunakan nilai
#sirkuit.remove("Suzuka")

#Menghapus dan mengembalikan elemen menggunakan .pop()
#ambil_sirkuit = sirkuit.pop(2)
#print(ambil_sirkuit)
#-------------------------------------------------------
#SLICING LIST

#driver = ["Hamilton", "Verstappen", "Leclerc", "Sainz", "Russell",
#"Antoneli", "Norris"]
#print(driver[0:6:2])
#-------------------------------------------------------
#OPERATOR PADA LIST

#Operator penjumlahan
#team1 = ["Mercedes", "Ferrari", "MacLaren"]
#team2 = ["Red Bull", "Alpine", "Aston Martin"]
#gabung_team = team1 + team2
#print(gabung_team)

#Operator pengulangan
#juara_WDC = ["MacLaren", "Red Bull"]
#juara = juara_WDC * 3
#print(juara)
#-------------------------------------------------------
#NESTED LIST

#line_up = [
#["Ferrari", "Leclerc", 16],
#["Mercedes", "Hamilton", 44],
#["Red Bull", "Verstappen", 1],
#["McLaren", "Norris", 4]
#]
#print(line_up[2][1])

#Untuk menampilkan semua data pada nested list, kita bisa menggunakan perulangan for
#line_up = [
#    ["Ferrari", "Leclerc", 16],
#    ["Mercedes", "Hamilton", 44],
#    ["Red Bull", "Verstappen", 1],
#    ["McLaren", "Norris", 4]
#]
#for i in line_up:
#    for j in i:
#        print(j)
#=======================================================

#=======================================================
#TUPLE

#Membuat Tuple
#chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
#print(chara)
#print(chara[2])
#print(chara[-1])
#print(chara[4][0])

#Memperbarui Tuple
#chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
#listchara = list(chara)

#listchara.append("Yui ")
#chara = tuple(listchara)
#print(chara)

#listchara.extend(["Kohaku", "Hikaru"])
#chara = tuple(listchara)
#print(chara)

#listchara.insert(2, "Senku")
#chara = tuple(listchara)
#print(chara)

# Unpack Tuple
# chara = ("Yukari", "Yukino", "Odette", "Senku")
# (Persona, Oregairu, Genshin, DrStone) = chara
# print(Persona)
# print(Oregairu)
#-------------------------------------------------------
#OPERATOR PADA TUPLE

#Operator join (penjumlahan)
# chara = ("Yukari", "Yukino", "Odette", "Senku")
# umur = (20, 22, 25, 17)
# join = chara + umur
# print(join)
#=======================================================