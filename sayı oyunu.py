 
import random

def sayi_tahmin_oyunu():
    while True:
        rastgele_sayi = random.randint(1,100)
        hak = 7
    
        print("""     
        +-+-+-+-+-+-+ +-+-+-+-+-+
        |T|a|h|m|i|n| |O|y|u|n|u|
        +-+-+-+-+-+-+ +-+-+-+-+-+
        """)
        print("\n1 ile 100 arasında bir sayı tahmin edin. 7 hakkınız var!")

        while hak > 0:
            tahmin = input(f"Kalan hakkınız: {hak} - Tahmininiz:")

            if tahmin.isdigit():
                tahmin = int(tahmin)

                if tahmin == rastgele_sayi:
                    print("Tebrikler! Doğru tahmin ettiniz!")
                    break
                elif tahmin < rastgele_sayi:
                    print("Daha büyük bir sayı girin.")
                else:
                    print("Daha küçük bir sayı girin.")

                hak -= 1    #  =>  hak = hak - 1
            else:
                print("Lütfen geçerli bir sayı girin!")

        if tahmin != rastgele_sayi:
            print(f"Bilemediniz! Doğru sayı: {rastgele_sayi} idi")

        tekrar = input("Tekrar oynamak ister misiniz? (E/H): ").strip().lower()

        if tekrar != "e":
            print("Oyunu oynadığınız için teşekkürler!")
            break
        
    
sayi_tahmin_oyunu()










