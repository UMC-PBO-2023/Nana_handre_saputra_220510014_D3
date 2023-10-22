#Program menghitung luas dan volume tabung

# Pertemuan 1
# Programmer: Nana handre saputra
# Tanggal:  22 Oktober 2023


jariJariTabung = 5;
tinggi = 15;

luasSelimutTabung = 2*3.14*jariJariTabung**2 * tinggi;
luasPermukaanTabung = luasSelimutTabung + 2*3.14*jariJariTabung**2;
volumeTabung = (3.14*jariJariTabung)*tinggi;

print('luas selimut tabung:', luasSelimutTabung)
print('luas permukaan tabung:', luasPermukaanTabung)
print('volume permukaan tabung:', volumeTabung)
