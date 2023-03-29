# UTS KECERDASAN BUATAN A
# KELOMPOK 16

import os;
import time;

# Skema Representasi Pengetahuan (Frame)

# Membuat dictionary (key: value)
introvert = {
    "introvert" : True,
    "extrovert" : False,
    "ambivert"  : False
}

extrovert = {
    "introvert" : False,
    "extrovert" : True,
    "ambivert"  : False
}

ambivert = {
    "introvert" : False,
    "extrovert" : False,
    "ambivert"  : True
}

daftar_pertanyaan = [
    {
        # Pertanyaan ke 1
        "pertanyaan" : 
            "Bagaimana kamu mengisi energi dan semangat setelah merasa lelah dan letih? ",
        "jawaban" : [
            {
                "pilihan" : "Istirahat di rumah atau bersantai di tempat tenang sendirian",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Pergi ke mall, berjumpa dengan teman-teman dan jalan-jalan",
                "nilai"   : extrovert       
            },
            {
                "pilihan" : "Nongkrong sendiri di kafe atau bersantai dengan sahabat dekat",
                "nilai"   : ambivert 
            }
        ]
    },
    {
        # Pertanyaan ke 2
        "pertanyaan" :
            "Bagaimana reaksi kamu saat mendengar kabar yang mengejutkan? ",
        "jawaban" : [
            {
                "pilihan" : "Tenang dan berfikir terlebih dahulu",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Terkejut dan menunjukkan reaksi",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Terkejut namun tetap tenang menanyai detil kabar tersebut",
                "nilai"   : ambivert
            }
        ]
    },
    {
        # Pertanyaan ke 3
        "pertanyaan" :
            "Bagaimana cara kamu memanfaatkan waktu luang di tengah kesibukan? ",
        "jawaban" : [
            {
                "pilihan" : "Membaca, menonton, atau bersantai di rumah",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Makan di luar, pergi ke taman bermain, atau berjumpa dengan teman",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Seimbang agar tidak bosan di rumah atau keseringan di luar",
                "nilai"   : ambivert
            }
        ]
    },
    {
        # Pertanyaan ke 4
        "pertanyaan" :
            "Cara kerja apa yang membuat kamu lebih produktif dalam mengerjakan pekerjaan?",
        "jawaban" : [
            {
                "pilihan" : "Kerja sendiri dan independen",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Kerja kelompok agar cepat selesai",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Kerja bareng 1-3 teman dekat kamu atau sendiri juga tidak apa-apa",
                "nilai"   : ambivert
            }
        ]
    },
    {
        # Pertanyaan ke 5
        "pertanyaan" :
            "Apa peran kamu dalam berteman dan bersosialisasi di lingkunganmu? ",
        "jawaban" : [
            {
                "pilihan" : "Lebih sering menjadi pendengar sehingga paham yang diceritakan teman",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Lebih aktif bercerita dan membagikan pengalaman yang baru dialami",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Memahami cerita teman serta memberikan pendapat yang tepat",
                "nilai"   : ambivert
            }
        ]
    },
    {
        # Pertanyaan ke 6
        "pertanyaan" :
            "Kira-kira bagaimana penilaian orang terhadap kamu? ",
        "jawaban" : [
            {
                "pilihan" : "Aku adalah orang yang serius, selalu hati-hati dan mandiri",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Aku adalah orang yang pandai bergaul, interaktif dan aktif",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Aku adalah orang yang mudah diajak berbicara, dan bisa menjaga rahasia",
                "nilai"   : ambivert
            }
        ]
    },
    {
        # Pertanyaan ke 7
        "pertanyaan" :
            "Bagaimana cara kamu membaca berita dan memberikan komentar di sosmed / forum? ",
        "jawaban" : [
            {
                "pilihan" : "Membaca detail dari awal sampai akhir sebelum memberikan pendapat",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Membaca bagian tengah dan akhir isi berita, baru memberikan pendapat",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Mencari bagian penting pada isi berita, baru memberikan pendapat ",
                "nilai"   : ambivert
            }
        ]
    },
    {
        # Pertanyaan ke 8
        "pertanyaan" :
            "Bagaimana kamu mendefinisikan aktivitas kamu di sosmed yang kamu miliki? ",
        "jawaban" : [
            {
                "pilihan" : "Lebih banyak membaca dan menyimak daripada memposting di sosmed",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Lebih sering memposting kegiatan di sosmed karena self image",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Memposting di sosmed saat momen penting atau diperlukan",
                "nilai"   : ambivert
            }
        ]
    },
    {
        # Pertanyaan ke 9
        "pertanyaan" :
            "Aktivitas apa yang membuatmu lupa diri atau lupa waktu? ",
        "jawaban" : [
            {
                "pilihan" : "Ketika sedang bersantai, membaca atau menonton film",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Ketika mengobrol bersama dengan teman atau melakukan aktivitas diluar",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Ketika sedang jalan-jalan di luar sendiri atau sama teman atau keluarga",
                "nilai"   : ambivert
            }
        ]
    },
    {
        # Pertanyaan ke 10
        "pertanyaan" : 
            "Jika boleh memilih hadiah, mana yang akan kamu pilih dibawah ini? ",
        "jawaban" : [
            {
                "pilihan" : "Lilin aromaterapi dan buku favorit",
                "nilai"   : introvert
            },
            {
                "pilihan" : "Voucher gym dan sandal travel",
                "nilai"   : extrovert
            },
            {
                "pilihan" : "Buku kesukaan dan parfum",
                "nilai"   : ambivert
            }
        ]
    }    
]


# Deklarasi variabel
i = 1;
skor_introvert  = 0;
skor_extrovert = 0;
skor_ambivert  = 0;

fast_track     = "";
jawaban_user = {};
queue = [];

tipe_kepribadian = ["Introvert", "Extrovert", "Ambivert"];

deskripsi_introvert = "Kamu sangat pemilih, kamu tidak suka menjadi pusat perhatian \nataupun berada dikeramain. Kamu tidak suka berhadapan dengan \norang yang bertele-tele. Kamu sangat hati-hati, kamu lebih \nsuka bekerja sendiri. Kamu memilih sendiri ketika merasa penat. \nKamu seorang perencana yang handal dan fokus. Kamu tidak \nsembarang membuka diri. Kamu adalah pemikir, tenang, dan handal.";
deskripsi_extrovert = "Kamu sangat baik dalam berinteraksi, karena kemampuan komunikasi \nyang baik, kamu dipercayai untuk menghandle orang lain. Kamu percaya \ndiri dan suka tampil. Kamu suka ditempat ramai, berbagi cerita \nadalah cara untuk melepas penatmu, walau membenci kesendirian, \nbukan berarti kamu tidak mandiri. Kamu merasa dunia dipenuhi \ncerita menarik dan kamu ingin menjadi bagian dari hal itu.";
deskripsi_ambivert = "Kamu baik dalam berkomunikasi dan juga merasa nyaman saat sendiri. \nKamu dapat beradaptasi dengan baik dimanapun. Pekerjaanmu juga bisa \nselesai dikerjakan baik sendiri maupun berkelompok. Kamu memang mudah \nberubah, karena itu kamu dapat memilih kapan untuk menyendiri dan \nkapan pergi ke luar. Kamu bisa menjadi pendengar yang baik.";


# Fungsi
def dekorasi() :
    print("------------------------------------------------------------------");

def tampilkan_hasil(nomor_tipe) :
    print("Tipe Kepribadian : ", tipe_kepribadian[nomor_tipe]);

def tampilkan_pertanyaan(daftar_pertanyaan) :
    global i;

    dekorasi();
    print("Pertanyaan ", i); 
    dekorasi();
    print("\n");

    print(daftar_pertanyaan["pertanyaan"], "\n");
    i+=1;

    j=1;
    for pilihan in daftar_pertanyaan["jawaban"] : 
        print("", j, ") ", pilihan["pilihan"]);
        j+=1;

    print("\n");

def masukkan_jawaban(daftar_pertanyaan) :
    jawaban_valid = False;
    while not jawaban_valid :
        pilihan_user = int(input(" Masukkan pilihan kamu (1/2/3) : "));
        dekorasi();
        if pilihan_user in [1, 2, 3] :
            jawaban_valid = True;
            jawaban_user[daftar_pertanyaan["pertanyaan"]] = daftar_pertanyaan["jawaban"][pilihan_user-1]["nilai"];
        else:
            print(" Mohon maaf, input tidak valid. Mohon masukkan angka 1/2/3");
            dekorasi();
            print("\n");

# Metode penalaran (Forward)
def hitung_nilai() :
    global skor_introvert, skor_extrovert, skor_ambivert;
    for jumlah_nilai in jawaban_user.values() :
        if jumlah_nilai["introvert"]: 
            skor_introvert += 1;
        elif jumlah_nilai["extrovert"] :
            skor_extrovert += 1;
        else :
            skor_ambivert +=1 ;

# Metode pencarian (Blind : Breadth-First Search (BFS))
def bfs():
    global queue;

    queue.append(("", 0))
    while queue:
        node, depth = queue.pop(0)
        if depth == len(jawaban_user):
            break;
        if len(node) < len(daftar_pertanyaan):
            for pertanyaan in daftar_pertanyaan[len(node)]:
                queue.append((node + str(pertanyaan), depth+1));
    return node;


# Main Program 
os.system("cls");

dekorasi();
print("\t    SELAMAT DATANG DI PROGRAM TES KEPRIBADIAN");
dekorasi();

print("Sebelum memulai tes kepribadian, mohon mengisi data");
print("berikut dengan informasi yang benar dan akurat \n");
dekorasi();

# 1. Biodata diri pengguna
nama_user    = input("Nama            : ");
umur_user    = int(input("Umur            : "));
gender_user  = input("Jenis Kelamin   : ");
kota_user    = input("Domisili        : ");
print("\n");

dekorasi();
print("\t    SELAMAT MENJALANKAN TES KEPRIBADIAN ^_^");
dekorasi();

time.sleep(5);
os.system("cls");

# 2. Kuisioner tes kepribadian
while True:
    node = bfs();
    tampilkan_pertanyaan(daftar_pertanyaan[len(jawaban_user)]);
    masukkan_jawaban(daftar_pertanyaan[len(jawaban_user)]);
    hitung_nilai();
    if len(jawaban_user) > 4 :
        if(len(jawaban_user) < 9) :
            while True:
                print("\nApakah kamu masih ingin melanjutkan mengisi tes ini atau langsung menampilkan hasil tes? ");
                fast_track = input("Silahkan ketik 'y' untuk melanjutkan atau 'n' untuk menampilkan hasil : ");
                if fast_track not in ["y", "n"] :
                    os.system("cls");
                    print("Mohon maaf, input tidak valid. Mohon masukkan huruf y atau n");
                    dekorasi();
                else :
                    break;

    os.system("cls");

    # 3. Hasil tes kepribadian 
    if(len(jawaban_user) > 9 or fast_track == "n") :
        dekorasi();
        print("\t             HASIL TES KEPRIBADIAN");
        dekorasi();

        print("Nama             : ", nama_user);
        print("Umur             : ", umur_user);
        print("Jenis Kelamin    : ", gender_user);
        print("Domisili         : ", kota_user);
        
        print("\n");
        dekorasi();

        if(skor_introvert > skor_extrovert and skor_introvert > skor_ambivert) : 
            tampilkan_hasil(0);
        elif(skor_extrovert > skor_introvert and skor_extrovert > skor_ambivert) :
            tampilkan_hasil(1);
        else:
            tampilkan_hasil(2);
        
        dekorasi();
        print("\n");

        if(skor_introvert > skor_extrovert and skor_introvert > skor_ambivert) : 
            print(deskripsi_introvert);
        elif(skor_extrovert > skor_introvert and skor_extrovert > skor_ambivert) :
            print(deskripsi_extrovert);
        else:
            print(deskripsi_ambivert);

        dekorasi();
        print('\n');

        break;