import random
import datetime

inventory = []  # List untuk menyimpan barang

# Fungsi menambahkan barang ke inventaris
def add_item(name, quantity):
    item_id = random.randint(1000, 9999)  # ID acak untuk barang
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item = {"id": item_id, "name": name, "quantity": quantity, "added_at": timestamp}
    inventory.append(item)
    print(f"Barang '{name}' dengan ID {item_id} ditambahkan ke inventaris.")

# Fungsi melihat daftar barang
def view_inventory():
    if not inventory:
        print("Inventaris kosong.")
        return
    print("\nDaftar Barang:")
    for item in inventory:
        print(f"ID: {item['id']} | Nama: {item['name']} | Jumlah: {item['quantity']} | Ditambahkan: {item['added_at']}")

# Fungsi menghapus barang berdasarkan ID
def remove_item(item_id):
    global inventory
    inventory = [item for item in inventory if item['id'] != item_id]
    print(f"Barang dengan ID {item_id} telah dihapus.")

# Menu utama
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Lihat Inventaris")
        print("3. Hapus Barang")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            name = input("Masukkan nama barang: ")
            quantity = int(input("Masukkan jumlah barang: "))
            add_item(name, quantity)
        elif pilihan == "2":
            view_inventory()
        elif pilihan == "3":
            view_inventory()
            item_id = int(input("Masukkan ID barang yang ingin dihapus: "))
            remove_item(item_id)
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()
