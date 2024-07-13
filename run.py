from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/cd4ecdcfae1246ec848e4812cd756169'))

# Jumlah akun yang akan dibuat
jumlah_akun = 1000  # Ganti dengan jumlah yang Anda inginkan

# Membuat dan menyimpan akun
with open('pk.txt', 'w') as pk_file, open('address.txt', 'w') as address_file:
    for _ in range(jumlah_akun):
        account = web3.eth.account.create()
        pk_file.write(account.key.hex()[2:] + '\n')  # Menghilangkan '0x' di awal dan menambahkan baris baru
        address_file.write(account.address + '\n')

print(f'{jumlah_akun} akun telah dibuat dan disimpan di pk.txt dan address.txt')
