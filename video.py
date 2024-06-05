import requests

def get_facebook_data(access_token):
    try:
        # Buat permintaan GET ke Graph API untuk mendapatkan informasi pengguna
        url = f'https://graph.facebook.com/v13.0/me?fields=id,name,email&access_token={access_token}'
        response = requests.get(url)
        
        # Periksa status respons
        if response.status_code == 200:
            user_data = response.json()
            print("Informasi Pengguna:")
            print("ID:", user_data.get('id'))
            print("Nama:", user_data.get('name'))
            print("Email:", user_data.get('email'))
            print("friend:", user_data.get('friends'))
            print("Email:", user_data.get('pages'))
        else:
            print("Gagal mengambil data. Kode status:", response.status_code)
    except Exception as e:
        print("Terjadi kesalahan:", e)

# Masukkan akses token Anda di sini
access_token = ' ' # masukan token fb
get_facebook_data(access_token)


