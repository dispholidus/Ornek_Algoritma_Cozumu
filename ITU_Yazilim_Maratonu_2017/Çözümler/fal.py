"""
Problem dosyası: "/ITU_Yazilim_Maratonu_2017/Sorular/prob-Fal.pdf"

Girdi: 2 string
Çıktı: 1 string


Girdi-Çıktı birimi: Standart iput-output
"""

alfabe = ["A", "B", "C", "D", "E", "F", "G", "H",
			"I", "J", "K", "L", "M", "N", "O", "P",
			"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
			
isim_1 = input().upper()
isim_2 = input().upper()

i=0
j=0
temp = 0



while (i<len(isim_1)):
	harf_1 = alfabe.index(isim_1[i]) 
	
	harf_2 = alfabe.index(isim_2[i])
	temp += abs(harf_1 - harf_2)
	i += 1
	
	
	
print(temp)
