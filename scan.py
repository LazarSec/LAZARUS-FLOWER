import scapy.all as scapy
import threading
import time
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from colorama import Fore, Style

# Inisialisasi variabel untuk menyimpan jumlah paket per detik
packet_count = 0
# Durasi jendela waktu dalam detik
WINDOW_DURATION = 10
# Maksimum jumlah paket yang diizinkan dalam jendela waktu
MAX_PACKETS = 100

def generate_sunflower_logo():
    sunflower_logo = r"""
   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ 
 ( L | A | Z | A | R | U | S )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
         F L O W E R         
"""
    return sunflower_logo

def generate_menu():
    menu = f"""
{generate_sunflower_logo()}
{Fore.RED}=== Menu ==={Style.RESET_ALL}
{Fore.RED}1.{Style.RESET_ALL} Jalankan Pemantauan DDoS
{Fore.RED}2.{Style.RESET_ALL} Jalankan Pemantauan DDoS dengan Pemindaian IP
{Fore.RED}3.{Style.RESET_ALL} Jalankan Pemantauan DDoS dengan Pemindaian Port Web
{Fore.RED}4.{Style.RESET_ALL} Jalankan Pemantauan DDoS dengan Pemindaian Server
{Fore.RED}5.{Style.RESET_ALL} Keluar
"""
    return menu

def scan_ip(target, timeout=1):
    try:
        # Implementasi pemindaian IP Anda di sini
        print(f"Pemindaian IP untuk {target} telah selesai.")
    except Exception as e:
        print(f"Terjadi kesalahan saat melakukan pemindaian IP: {e}")

def scan_web(target):
    try:
        # Implementasi pemindaian port web Anda di sini
        print(f"Pemindaian port web untuk {target} telah selesai.")
    except Exception as e:
        print(f"Terjadi kesalahan saat melakukan pemindaian port web: {e}")

def scan_server(target):
    try:
        # Implementasi pemindaian server Anda di sini
        print(f"Pemindaian server untuk {target} telah selesai.")
    except Exception as e:
        print(f"Terjadi kesalahan saat melakukan pemindaian server: {e}")

def display_table(data):
    if not data:
        print("Tidak ada data untuk ditampilkan.")
        return
    try:
        table = PrettyTable()
        table.field_names = data[0].keys()
        for entry in data:
            table.add_row(entry.values())
        print(table)
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan tabel: {e}")

# Fungsi untuk memeriksa dan menolak paket yang mencurigakan
def check_ddos():
    global packet_count
    while True:
        time.sleep(WINDOW_DURATION)
        if packet_count > MAX_PACKETS:
            print("Serangan DDoS terdeteksi. Menerapkan tindakan preventif...")
            # Implementasikan tindakan preventif di sini (mis. menolak lalu lintas)
            print("Semua lalu lintas telah diblokir untuk melindungi dari serangan DDoS.")
            # Set ulang jumlah paket
            packet_count = 0

# Mulai thread untuk memeriksa serangan DDoS
ddos_thread = threading.Thread(target=check_ddos)
ddos_thread.start()

# Fungsi untuk menghitung jumlah paket per detik
def packet_callback(packet):
    global packet_count
    packet_count += 1

def monitor_ddos(interface="eth0", duration=60, ip_target=None, web_target=None):
    # Inisialisasi variabel untuk menyimpan jumlah paket per detik
    packet_count = []

    # Mendefinisikan fungsi untuk menghitung jumlah paket per detik
    def packet_callback(packet):
        packet_count.append(len(packet))

    # Mulai thread untuk memeriksa serangan DDoS
    ddos_thread = threading.Thread(target=check_ddos)
    ddos_thread.start()

    try:
        # Memulai sniffer pada antarmuka yang ditentukan
        scapy.sniff(iface=interface, prn=packet_callback, timeout=duration)

        # Menampilkan grafik jumlah paket per detik
        time = np.arange(0, len(packet_count))
        plt.plot(time, packet_count)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Number of packets')
        plt.title('DDoS Attack Monitoring')
        plt.show()

        # Membuat dan menampilkan tabel pemindaian IP jika target IP ditentukan
        if ip_target:
            ip_scan_result = scan_ip(ip_target)
            print("\n=== IP Scan Result ===")
            display_table(ip_scan_result)

        # Membuat dan menampilkan tabel pemindaian port web jika target port web ditentukan
        if web_target