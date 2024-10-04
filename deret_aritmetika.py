def deret_aritmetika(N):
    # Nilai awal dan selisih
    awal = 2
    selisih = 3
    
    # Menghasilkan deret aritmetika
    deret = [awal + i * selisih for i in range(N)]
    
    return deret

if __name__ == "__main__":
    try:
        # Minta input dari pengguna
        N = int(input("Input: "))
        
        # Dapatkan deret dan format output
        hasil = deret_aritmetika(N)
        output = ','.join(map(str, hasil))
        
        # Tampilkan hasil
        print("Output:", output)
        
    except ValueError:
        print("Masukkan angka yang valid.")