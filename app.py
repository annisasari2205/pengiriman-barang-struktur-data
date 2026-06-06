import streamlit as st
from collections import deque

# =====================================
# KELAS QUEUE PENGIRIMAN BARANG
# =====================================
class PengirimanQueue:
    def __init__(self):
        self.antrian = deque()

    def tambah_barang(self, kode, nama, tujuan):
        self.antrian.append({
            "Kode": kode,
            "Nama": nama,
            "Tujuan": tujuan
        })

    def kirim_barang(self):
        if self.antrian:
            return self.antrian.popleft()
        return None

    def lihat_antrian(self):
        return list(self.antrian)

# =====================================
# SESSION STATE
# =====================================
if "queue" not in st.session_state:
    st.session_state.queue = PengirimanQueue()

# =====================================
# TAMPILAN STREAMLIT
# =====================================
st.title("📦 Sistem Pengiriman Barang (Queue FIFO)")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Tambah Barang", "Kirim Barang", "Lihat Antrian"]
)

# =====================================
# MENU TAMBAH BARANG
# =====================================
if menu == "Tambah Barang":
    st.subheader("Tambah Barang ke Antrian")

    kode = st.text_input("Kode Barang")
    nama = st.text_input("Nama Barang")
    tujuan = st.text_input("Tujuan Pengiriman")

    if st.button("Tambah"):
        if kode and nama and tujuan:
            st.session_state.queue.tambah_barang(
                kode,
                nama,
                tujuan
            )
            st.success("Barang berhasil masuk antrian!")
        else:
            st.error("Semua data harus diisi!")

# =====================================
# MENU KIRIM BARANG
# =====================================
elif menu == "Kirim Barang":
    st.subheader("Proses Pengiriman Barang")

    if st.button("Kirim Barang Berikutnya"):
        barang = st.session_state.queue.kirim_barang()

        if barang:
            st.success("Barang berhasil dikirim!")
            st.write("### Detail Barang")
            st.write(f"Kode : {barang['Kode']}")
            st.write(f"Nama : {barang['Nama']}")
            st.write(f"Tujuan : {barang['Tujuan']}")
        else:
            st.warning("Antrian kosong!")

# =====================================
# MENU LIHAT ANTRIAN
# =====================================
elif menu == "Lihat Antrian":
    st.subheader("Daftar Antrian Pengiriman")

    data = st.session_state.queue.lihat_antrian()

    if data:
        st.table(data)
    else:
        st.info("Belum ada barang dalam antrian.")
