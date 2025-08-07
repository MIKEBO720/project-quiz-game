#tanya user beberapa pertanyaan dan jika jawab benar beri point step 1

print("welcome to the quiz game! Let's see how much you know!")

playing = input("do you want to play? ") #input itu promt buat tanya user apakah mau main jadi input ya kaya buat isi ya atau tidak

#step 2 mau cek apakah user mau main atau tidak
if playing.lower() != "yes":#syntax if itu untuk mengecek kondisi, kalau kondisi itu benar maka akan dieksekusi
    #lower() itu untuk mengubah input user menjadi huruf kecil semua kalau upper itu untuk mengubah input user menjadi huruf besar semua
    #tapi bisa input habis itu belakang nya .lower() ATAU .upper() harus pakai kurung yaitu () karena itu adalah fungsi
    quit() #kalau user tidak mau main maka program akan berhenti

print("okay! let's play!XD ") #kalau user mau main maka program akan lanjut 

#step 4 dan 5 set up code buat track score user
#ini adalah variabel untuk menyimpan score user buat tracking score user
#menambahkan += itu sama dengan score = score + 1
#jadi kalau user benar maka score nya bertambah 1
score = 0 #ini adalah variabel untuk menyimpan score user buat tracking score user

#STEP 3 TANYA USER PERTANYAAN PERTAMA ya buat quiz nya
answer = input("what does CPU STANDS FOR? ") #tanya user pertanyaan pertama
if answer.lower() == "central processing unit": #cek apakah jawaban user benar
        print("correct!") #kalau benar maka user dapat point
        score += 1 #kalau benar maka score user bertambah 1
else: #kalau salah maka user tidak dapat point
        print ("incorrect!") #tampilkan pesan salah

answer = input("what does the government likes? ") #tanya user pertanyaan pertama
if answer.lower() == "corruption": #cek apakah jawaban user benar
        print("correct!") #kalau benar maka user dapat point
        score += 1 #kalau benar maka score user bertambah 1
else: #kalau salah maka user tidak dapat point
        print ("incorrect!") #tampilkan pesan salah

answer = input("WHO LOVES TO JOGET JOGET? ") #tanya user pertanyaan pertama
if answer.upper() == "ME": #cek apakah jawaban user benar
        print("correct!") #kalau benar maka user dapat point
        score += 1 #kalau benar maka score user bertambah 1
else: #kalau salah maka user tidak dapat point
        print ("incorrect!") #tampilkan pesan salah

#step 6 tampilkan score user
print("you got " + str(score) + " points!") #tampilkan score user, str() itu untuk mengubah integer menjadi string
#jadi kalau score nya 3 maka akan tampil "you got 3 points!"
print("you got "+str(score/3 * 100) + "%") #tampilkan persentase score user, jadi kalau score nya 3 maka akan tampil "you got 100%"
#jadi kalau score nya 2 maka akan tampil "you got 66.666666666
#score/3 karena ada 3 pertanyaan jadi score dibagi 3 dan dikali 100 untuk mendapatkan persentase
#jadi kalau score nya 1 maka akan tampil "you got 33.3333333333%"
#jadi kalau score nya 0 maka akan tampil "you got 0%"
#step 7 tampilkan pesan terima kasih sudah bermain
print("thanks for playing!") #tampilkan pesan terima kasih sudah bermain
#jadi kalau user sudah selesai bermain maka program akan berhenti