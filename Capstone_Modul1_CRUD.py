#Data Museum
data_museum = []  
data_museum = [

            {"Number":"1", 
             "Inventory Number":"INV001",
             "Name":"Ancient Vase",
             "Type":"Ceramic",
             "Material":"Clay",
             "Location Founded":"Greece",
             "Condition":"Execellent",
             "Obtain From":"Archaeological Excavation"
            },
            
            {"Number":"2", 
             "Inventory Number":"INV002",
             "Name":"Medieval Sword",
             "Type":"Weaponry",
             "Material":"Iron",
             "Location Founded":"England",
             "Condition":"Good",
             "Obtain From":"Royal Donation" 
            },
            
            {"Number":"3", 
             "Inventory Number":"INV003",
             "Name":"Egyptian Amulet",
             "Type":"Jewelry",
             "Material":"Gold",
             "Location Founded":"Egypt",
             "Condition":"Good",
             "Obtain From":"Archaeological Excavation"
            },
            
            {"Number":"4", 
             "Inventory Number":"INV004",
             "Name":"Roman Coin",
             "Type":"Currency",
             "Material":"Silver",
             "Location Founded":"Italy",
             "Condition":"Fair",
             "Obtain From":"Private Collector"
            },
            
            {"Number":"5", 
             "Inventory Number":"INV005",
             "Name":"Ancient Scroll",
             "Type":"Manuscript",
             "Material":"Papyrus",
             "Location Founded":"Turkey",
             "Condition":"Fragile",
             "Obtain From":"University Donation"
            },
            
            {"Number":"6", 
             "Inventory Number":"INV006",
             "Name":"Pottery Vessel",
             "Type":"Ceramic",
             "Material":"Clay",
             "Location Founded":"Peru",
             "Condition":"Fragile",
             "Obtain From":"Archaeological Excavation"
            },
            
            {"Number":"7", 
             "Inventory Number":"INV007",
             "Name":"Renaissance Painting",
             "Type":"Artwork",
             "Material":"Oil on Canvas",
             "Location Founded":"France",
             "Condition":"Good",
             "Obtain From":"Royal Donation"
            },
            
            {"Number":"8", 
             "Inventory Number":"INV008",
             "Name":"Aztec Mask",
             "Type":"Artifact",
             "Material":"Obsidian",
             "Location Founded":"Mexico",
             "Condition":"Good",
             "Obtain From":"Government Donation"
            },
            
            {"Number":"9", 
             "Inventory Number":"INV009",
             "Name":"Ancient Helmet",
             "Type":"Armor",
             "Material":"Steel",
             "Location Founded":"Norway",
             "Condition":"Good",
             "Obtain From":"Archaeological Excavation"
            },
            
            {"Number":"10", 
             "Inventory Number":"INV010",
             "Name":"Ming Dynasty Porcelain",
             "Type":"Artifact",
             "Material":"Porcelain",
             "Location Founded":"China",
             "Condition":"Excellent",
             "Obtain From":"Auction Purchase" 
            }

            ]

#Membuat tabel dalam CRUD
from tabulate import tabulate


#Menu_Utama
def main_menu():
      while True:
            opsi_menu = input('''

            \033[1m🏛️  MUSEUM COLLECTION DATABASE 🏛️\033[0m
            
            Menu Options:
            [1]. Display Collections                    [4]. Update Collection                                                
            [2]. Search Collection                      [5]. Delete Collection
            [3]. Add New Collection                     [6]. Exit Program 
                                  
            Select a number from the list above to start the program : 
            
            ''')

            if opsi_menu == "1": # Kondisi saat user memilih opsi menu 1 (Menampilkan semua koleksi)
                opsi_menu1()
            elif opsi_menu == "2": # Kondisi saat user memilih opsi menu 2 (Mencari koleksi berdasarkan alphabet/nama yang diinput)
                opsi_menu2()
            elif opsi_menu == "3": # Kondisi saat user memilih opsi menu 3 (Menambahkan koleksi)
                opsi_menu3()
            elif opsi_menu == "4": # Kondisi saat user memilih opsi menu 4 (Mengedit koleksi)
                opsi_menu4()
            elif opsi_menu == "5": # Kondisi saat user memilih opsi menu 5 (Menghapus koleksi)
                opsi_menu5()
            elif opsi_menu == "6": # Kondisi saat user memilih opsi menu 6 (Keluar dari program)
                opsi_menu6()
            else:
                print("\n⚠️ Invalid Data! Please select a number from the list above!")

def tampilkan_koleksi(): 
    print("\n" + "=" * 60 + "\033[1m🏛️  MUSEUM COLLECTION DATABASE 🏛️ \033[0m" + "=" * 58 + "\n")
    headers = ["Number", "Inventory Number", "Name", "Type", "Material", "Location Founded", "Condition", "Obtain From"]
    table = [[museum["Number"], museum ["Inventory Number"], museum["Name"], museum["Type"], museum["Material"], museum["Location Founded"], museum["Condition"], museum["Obtain From"]] for museum in data_museum]
    print(tabulate(table, headers=headers, tablefmt="heavy_grid", numalign=("left"), stralign=("left")))

# Menu 1 - 2
def opsi_menu1():
    while True:
            opsi_menu_1 = input('''

            \033[1m🏛️  MUSEUM COLLECTION DATABASE 🏛️\033[0m
            
            Menu Options:
            [1]. Display All Collections                                                              
            [2]. Display Collection by Inventory Number                        
            [3]. Return to Main Menu                   
                                    
            Select a number from the list above to start the program : 
            
            ''')
            if opsi_menu_1 == '1':
                    while True :
                        menu1_konfirmasi = input("\t    Do you want to display all collections? (Y/N) : ").upper()
                        if menu1_konfirmasi == 'Y':
                            tampilkan_koleksi()
                            break
                        elif menu1_konfirmasi == 'N':
                            print("❌ Display cancelled. You can view the collections anytime by selecting the display option.")
                            break
                        else:
                            print("⚠️ Invalid input! Please enter 'Y' or 'N'.")

            elif opsi_menu_1 == '2':
                    while True:
                        if not data_museum:
                            print("⚠️  No data available.")
                            return
                        
                        valid_inventory_numbers = sorted([museum["Inventory Number"] for museum in data_museum])
                        print(f"\nℹ️  Valid Inventory Numbers: {', '.join(valid_inventory_numbers)}")
                        
                        pilihan = input("Enter Inventory Number (e.g., INV005): ").replace(" ", "").upper()
                        hasil = [museum for museum in data_museum if museum["Inventory Number"] == pilihan]
                        
                        if not hasil:
                            print(f"\n⚠️  Inventory Number {pilihan} is not found in the collection.")
                            continue
                        
                        museum = hasil[0]  #Untuk mendapatkan hasil yang sesuai 

                        while True:
                            tanya_kolom = input("Do you want to show this collection? (Y/N): ").strip().upper()
                            if tanya_kolom == "Y":
                                headers_1 = list(museum.keys())
                                data_dipilih = [[museum[kolom] for kolom in headers_1]]
                                print(f"\n📄 Full Details for {pilihan}:\n")
                                print(tabulate(data_dipilih, headers=headers_1, tablefmt="rounded_grid", numalign="left", stralign="left"))
                                opsi_menu1()

                            elif tanya_kolom == "N":
                                print("❌ Display cancelled. You can view the collections anytime by selecting the display option.")
                                opsi_menu1()
                            else:
                                print("⚠️ Invalid input! Please enter 'Y' or 'N'.")
                                continue

            elif opsi_menu_1 == '3':
                print("\n🔙 Returning to main menu...")      
                main_menu()

            else:
                print("\n⚠️ Invalid Data! Please select a number from the list above!") 

def opsi_menu2():
        while True:
            opsi_menu_2 = input('''

            \033[1m🔎 SEARCH COLLECTIONS MENU 🔍\033[0m

            Menu Options:
            [1]. Search by Columns                                                                
            [2]. Search by Inventory Number Only                       
            [3]. Return to Main Menu
                                    
            Select a number from the list above to search: 

            ''')
        
            if opsi_menu_2 == '1':
                while True:
                    print("\n🔎 Search by Columns : \n")
                    kolom_pilihan = {
                        "1": "Number",
                        "2": "Inventory Number",
                        "3": "Name",
                        "4": "Type",
                        "5": "Material",
                        "6": "Location Founded",
                        "7": "Condition",
                        "8": "Obtain From"
                    }

                    for kode, nama_kolom in kolom_pilihan.items():
                        print(f"[{kode}]. {nama_kolom}")

                    input_kolom = input("\nEnter the number of the column you want to search by: ").strip()
                    if input_kolom not in kolom_pilihan:
                        print("\n⚠️ Invalid input! Please select a valid option.")
                        continue
                    
                    kolom_dicari = kolom_pilihan[input_kolom]
                    keyword = input(f"Enter keyword to search in '{kolom_dicari}': ").strip().lower().replace(" ", "")

                    hasil_filter = []
                    for item in data_museum:
                        if keyword in str(item[kolom_dicari]).lower().replace(" ", ""):
                            hasil_filter.append([
                                item["Number"], item["Inventory Number"], item["Name"], item["Type"],
                                item["Material"], item["Location Founded"], item["Condition"], item["Obtain From"]
                            ])

                    if hasil_filter:
                        judul_kolom = ["Number", "Inventory Number", "Name", "Type", "Material", "Location Founded", "Condition", "Obtain From"]
                        print("\n📖 Search Result:\n")
                        print(tabulate(hasil_filter, headers=judul_kolom, tablefmt="rounded_grid", numalign="left", stralign="left"))
                    else:
                        print("\n❌ No matching collection found.")

                    while True:
                        ulang_search = input("\nDo you want to search again in any column? (Y/N): ").upper()
                        if ulang_search == 'Y':
                            break
                        elif ulang_search == 'N':
                            print("\n🔙 Returning to search menu...")
                            opsi_menu2()
                        else:
                            print("⚠️ Invalid input! Please enter 'Y' or 'N'.")

            elif opsi_menu_2 == '2':
                while True:
                    if not data_museum:
                        print("⚠️ No data available.")
                        return
                    
                    daftar_inv = sorted([item["Inventory Number"] for item in data_museum])
                    print(f"\nℹ️ Valid Inventory Numbers: {', '.join(daftar_inv)}")

                    inv_dicari = input("Enter Inventory Number to search (e.g., INV005): ").replace(" ", "").upper()
                    hasil_cari = [item for item in data_museum if item["Inventory Number"] == inv_dicari]

                    if not hasil_cari:
                        print(f"\n⚠️ Inventory Number '{inv_dicari}' not found.")
                        continue
                    
                    item_terpilih = hasil_cari[0]

                    while True:
                        konfirmasi_detail = input(f"Do you want to display full details of {inv_dicari}? (Y/N): ").strip().upper()
                        if konfirmasi_detail == 'Y':
                            judul_kolom = list(item_terpilih.keys())
                            data_detail = [[item_terpilih[kol] for kol in judul_kolom]]
                            print(f"\n📄 Full Details for {inv_dicari}:\n")
                            print(tabulate(data_detail, headers=judul_kolom, tablefmt="rounded_grid", numalign="left", stralign="left"))
                            break
                        elif konfirmasi_detail == 'N':
                            print("❌ Display cancelled.")
                            break
                        else:
                            print("⚠️ Invalid input! Please enter 'Y' or 'N'.")

                    while True:
                        cari_lagi = input("\nDo you want to search another Inventory Number? (Y/N): ").strip().upper()
                        if cari_lagi == 'Y':
                            break
                        elif cari_lagi == 'N':
                            print("\n🔙 Returning to search menu...")
                            opsi_menu2()
                        else:
                            print("⚠️ Invalid input! Please enter 'Y' or 'N'.")

            elif opsi_menu_2 == '3':
                print("\n🔙 Returning to main menu...")
                main_menu()

            else:
                print("\n⚠️ Invalid Data! Please select a number from the list above!")

#Input kolom baru
def jenis_baru():
    while True:
        jenis_baru1 = input("Enter Type: ").strip()
        if jenis_baru1.isalpha():
            return jenis_baru1
        else:
            print("⚠️ The 'Type' column must not contain numbers!")
            continue

def bahan_baru():
    while True:    
        bahan_baru1 = input("Enter Material: ").strip()
        if bahan_baru1.isalpha():
            return bahan_baru1
        else:
            print("⚠️ The 'Material' column must not contain numbers!")
            continue

def lokasi_baru():
    while True: 
        lokasi_baru1 = input("Enter Location Founded: ").strip()
        if lokasi_baru1.isalpha():
            return lokasi_baru1
        else:
            print("⚠️ The 'Location Founded' column must not contain numbers!")
        continue
    
def kondisi_baru():
    while True: 
        kondisi_baru1 = input("Enter Condition: ").strip()
        if kondisi_baru1.isalpha():
            return kondisi_baru1
        else:
            print("⚠️ The 'Condition' column must not contain numbers!")
        continue

# Menu 3 - 6 
def opsi_menu3():
        while True:
            opsi_menu_3 = input('''

            \033[1m➕ ADD COLLECTION MENU ➕\033[0m

            Menu Options:
            [1]. Add New Collection                                                                
            [2]. Return to Main Menu
                                    
            Select a number from the list above to continue: 

            ''')

            if opsi_menu_3 == '1':
                tampilkan_koleksi()

                while True:
                    konfirmasi_tambah = input("Do you want to add a new collection? (Y/N): ").strip().upper()
                    if konfirmasi_tambah == 'Y':
                        break
                    elif konfirmasi_tambah == 'N':
                        print("❌ Addition cancelled. Returning to Add Collection Menu.")
                        opsi_menu3()  
                    else:
                        print("⚠️ Invalid input! Please enter 'Y' or 'N'.")

                print("\n📝 Please fill in the following data accurately:")

                nomor_baru = len(data_museum) + 1
                inventori_baru = f"INV{int(nomor_baru):03d}"  

                nama_baru = input("Enter Name of the Item: ").strip()
                
                jenis = jenis_baru()
                bahan = bahan_baru()
                lokasi = lokasi_baru()
                kondisi = kondisi_baru()
                
                asal_baru = input("Enter Source (Obtain From): ").strip()

                data_baru = {
                    "Number": nomor_baru,
                    "Inventory Number": inventori_baru,
                    "Name": nama_baru,
                    "Type": jenis,
                    "Material": bahan,
                    "Location Founded": lokasi,
                    "Condition": kondisi,
                    "Obtain From": asal_baru
                }

                print("\n📄 Here's the collection you are about to add:\n")
                kolom = ["No", "Inventory Number", "Name", "Type", "Material", "Location Founded", "Condition", "Obtain From"]
                nilai = [[
                    data_baru["Number"],
                    data_baru["Inventory Number"],
                    data_baru["Name"],
                    data_baru["Type"],
                    data_baru["Material"],
                    data_baru["Location Founded"],
                    data_baru["Condition"],
                    data_baru["Obtain From"]
                ]]
                print(tabulate(nilai, headers=kolom, tablefmt="rounded_grid", numalign="left", stralign="left"))

                while True:
                    konfirmasi_simpan = input("\nDo you want to save this collection? (Y/N): ").strip().upper()
                    if konfirmasi_simpan == 'Y':
                        data_museum.append(data_baru)
                        print("✅ New collection successfully added!")
                        tampilkan_koleksi()
                        break
                    elif konfirmasi_simpan == 'N':
                        print("❌ Data was not saved.")
                        break
                    else:
                        print("⚠️ Invalid input! Please enter 'Y' or 'N'.")

            elif opsi_menu_3 == '2':
                print("\n🔙 Returning to main menu...")
                main_menu()
            
            else:
                print("⚠️ Invalid Data! Please select a number from the list above.")

def opsi_menu4():
        while True:
            opsi_menu_4 = input('''

                \033[1m✏️  EDIT COLLECTION MENU ✏️\033[0m

                [1]. Edit Collection by Column
                [2]. Return to Main Menu
                
                Select a number from the list above to continue:
                
                ''')

            if opsi_menu_4 == "1":
                if not data_museum:
                    print("⚠️  No data available to edit.")
                    return

                # Menampilkan daftar Inventory Number
                daftar_inv_valid = sorted([koleksi["Inventory Number"] for koleksi in data_museum])
                print(f"\n📌 Valid Inventory Numbers: {', '.join(daftar_inv_valid)}")

                inv_input = input("Enter Inventory Number to edit: ").replace(" ", "").upper()
                koleksi_terpilih = [k for k in data_museum if k["Inventory Number"] == inv_input]

                if not koleksi_terpilih:
                    print(f"⚠️  Inventory Number '{inv_input}' not found.")
                    opsi_menu4()

                data_edit = koleksi_terpilih[0]

                # Preview data sebelum diedit
                kolom_header = list(data_edit.keys())
                isi_koleksi = [[data_edit[k] for k in kolom_header]]
                print(f"\n📄 Preview of Collection '{inv_input}':\n")
                print(tabulate(isi_koleksi, headers=kolom_header, tablefmt="rounded_grid", numalign="left", stralign="left"))

            
                while True:
                    lanjut = input("\nDo you want to edit this collection? (Y/N): ").strip().upper()
                    if lanjut == 'N':
                        print("❌ Edit cancelled.")
                        break
                    elif lanjut == 'Y':
                        # Menampilkan daftar kolom yang bisa diedit
                        pilihan_kolom = {
                            "1": "Name",
                            "2": "Type",
                            "3": "Material",
                            "4": "Location Founded",
                            "5": "Condition",
                            "6": "Obtain From"
                        }

                        print("\n🔧 Editable Columns:")
                        for key, val in pilihan_kolom.items():
                            print(f"[{key}]. {val}")

                        kolom_input = input("\nEnter column number to edit: ").strip()
                        if kolom_input not in pilihan_kolom:
                            print("⚠️ Invalid column selection.")
                            break

                        kolom_dipilih = pilihan_kolom[kolom_input]
                        nilai_lama = data_edit[kolom_dipilih]
                        
                        while True:
                            nilai_baru = input(f"Enter new value for '{kolom_dipilih}' (current: '{nilai_lama}'): ").strip()
                            
                            if kolom_dipilih in ["Type", "Material", "Location Founded", "Condition"]:
                                if not nilai_baru.replace(" ", "").isalpha():
                                    print(f"⚠️ The '{kolom_dipilih}' field must contain only alphabetic characters!")
                                    continue

                            if nilai_baru == nilai_lama or not nilai_baru:
                                print("⚠️ No changes were made.")
                                continue
                            
                            break  

                        while True:
                            konfirmasi_edit = input(f"Change '{kolom_dipilih}' from '{nilai_lama}' to '{nilai_baru}'? (Y/N): ").strip().upper()
                            if konfirmasi_edit == 'Y':
                                data_edit[kolom_dipilih] = nilai_baru
                                print("\n✅ Collection successfully updated!")

                                # Preview setelah edit
                                koleksi_terupdate = [[data_edit[k] for k in kolom_header]]
                                print("\n📄 Updated Collection:\n")
                                print(tabulate(koleksi_terupdate, headers=kolom_header, tablefmt="rounded_grid", numalign="left", stralign="left"))
                                tampilkan_koleksi()
                                return opsi_menu4()

                            elif konfirmasi_edit == 'N':
                                print("❌ Edit cancelled.")
                                return opsi_menu4()
                            
                            else:
                                print("⚠️ Invalid input. Please enter 'Y' or 'N'.")
                                
                    else:
                        print("⚠️ Invalid input. Please enter 'Y' or 'N'.")
                        continue
                    
            elif opsi_menu_4 == "2":
                print("🔙 Returning to Main Menu...")
                main_menu()

            else:
                print("⚠️ Invalid input. Please select a number from the list above.")

def opsi_menu5():
        while True:
            opsi_menu_5 = input('''

                \033[1m🗑️  DELETE COLLECTION MENU 🗑️\033[0m

                [1]. Delete Collection by Number
                [2]. Return to Main Menu
                
                Select a number from the list above to continue:
                
                ''')

            if opsi_menu_5 == "1":
                if not data_museum:
                    print("⚠️  No data available to delete.")
                    return

                while True:  
                    print("\n📄 Museum Collection List:\n")
                    headers_2 = list(data_museum[0].keys())
                    rows = [[item[k] for k in headers_2] for item in data_museum]
                    print(tabulate(rows, headers=headers_2, tablefmt="heavy_grid", numalign="left", stralign="left"))

                    while True:
                        try:
                            index_hapus = int(input("\nEnter the collection number you want to delete: ")) - 1
                            if index_hapus < 0 or index_hapus >= len(data_museum):
                                print("❌ Invalid collection number! Please try again.")
                                continue
                        except ValueError:
                            print("❌ Input must be a number! Please try again.")
                            continue

                        koleksi_dipilih = data_museum[index_hapus]

                        print(f"\n📄 Selected Collection to Delete:\n")
                        print(tabulate([[koleksi_dipilih[k] for k in headers_2]], headers=headers_2, tablefmt="rounded_grid", numalign="left", stralign="left"))

                        while True:
                            konfirmasi_hapus = input("\nAre you sure you want to delete this collection? (Y/N): ").strip().upper()
                            if konfirmasi_hapus == 'Y':
                                koleksi_dihapus = data_museum.pop(index_hapus)
                                print(f"\n✅ Collection '{koleksi_dihapus['Name']}' has been successfully deleted!")

                                # Update nomor setelah penghapusan
                                for i in range(len(data_museum)):
                                    data_museum[i]["Number"] = i + 1

                                # Tampilkan kembali koleksi setelah penghapusan
                                if data_museum:
                                    print("\n📄 Updated Museum Collection:\n")
                                    updated_rows = [[item[k] for k in headers_2] for item in data_museum]
                                    print(tabulate(updated_rows, headers=headers_2, tablefmt="heavy_grid", numalign="left", stralign="left"))
                                else:
                                    print("📭 No remaining collections in the database.")
                                    return  # Keluar karena tidak ada lagi data
                                break

                            elif konfirmasi_hapus == 'N':
                                print("❌ Collection deletion has been canceled.")
                                opsi_menu5()

                            else:
                                print("⚠️ Invalid input! Please enter 'Y' or 'N'.")
                                continue

                        if data_museum:
                            while True:
                                ulang_hapus = input("\nDo you want to delete another collection? (Y/N): ").strip().upper()
                                if ulang_hapus == 'Y':
                                    break  # lanjut hapus lagi (kembali ke awal while True luar)
                                elif ulang_hapus == 'N':
                                    print("🔙 Returning to Delete Collection Menu...")
                                    opsi_menu5()
                                else:
                                    print("⚠️ Invalid input! Please enter 'Y' or 'N'.")
                        else:
                            break

            elif opsi_menu_5 == "2":
                print("🔙 Returning to Main Menu...")
                main_menu()

            else:
                print("⚠️ Invalid input. Please select a number from the list above.")

def opsi_menu6():
    print("Thank you! See you again.")
    exit()

main_menu()
