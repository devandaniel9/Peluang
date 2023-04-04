# Title

# List import
import numpy as np
import math
import streamlit as st

from PIL import Image

# Menjalankan program
# streamlit run 'Peluang 2.py'

# @import fonts/Roboto-Regular.ttf;

aaa = """
	<style>
	@import fonts/Roboto-Regular.ttf;

	html, body, [class*="css"]  {
	font-family: 'Roboto', sans-serif;
	}
	</style>
"""

streamlit_style = """
	<style>
	@import fonts;

	[class*="css"]  {
	font-family: 'roboto';
	}
	</style>
"""

def color(text, c):
    return f"<font color={c}>{text}</font>"

st.markdown(streamlit_style, unsafe_allow_html=True)

def stw(text):
    return st.markdown(text, unsafe_allow_html=True)

# import base64

def get_base64(bin_file):
    import base64

    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# set_background("background.jpg")

st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

# Streamlit
# st.write("""# Program Peluang""")
# st.markdown("# <font color='#a0c0ff'>Program Peluang</font>", unsafe_allow_html=True)
stw(f"# {color('Program Peluang', '#a0c0ff')}")
st.write('**Peluang** dalam matematika adalah kejadian yang muncul.')
st.write('')

st.write('## **Pengaturan**')
with st.expander("Tampilkan"):
    st.write('### **Background**')
    satuan = st.radio('Pilih background', ['Tidak ada', 'Ada'], index=1)
    # st.write('Source: https://www.pinterest.com/pin/81050726416304712')
    
    st.write('### **Link**')
    st.write('Link program Geometri:  \nhttps://devandaniel9-geometry-3.streamlit.app/')
    st.write('### **Lanjutan**')
    st.write('[Coming Soon]')
    st.write('### **Tentang**')
    st.write('Copyright © ?????')
    st.write('Dibuat oleh Devan Daniel')
    st.write('### **Reset**')
    st.button('Reset Settings')
st.write('')

# oi = open image

def open_image(nama):
    width = 300
    try:
        # img = Image.open(f"{bentuk}.png")
        img = Image.open(f'images/{nama}')
        # st.image(img, width=200)
        st.image(img, width=width)
    except FileNotFoundError:
        img = ""

st.write('## **Peluang**')
open_image("Peluang.png")
st.write('Program Peluang terdiri dari Titik Sampel, Jenis Peluang, Kombinasi, dan Himpunan')
st.write('Lebih lengkap di tab Definisi')
geometri_list = ["Titik Sampel", "Jenis Peluang", "Kombinasi", "Himpunan", "Definisi"]
geometri = st.selectbox("Pilih jenis peluang:", geometri_list)

digit = 3
def fungsi(angka):
    a = round(angka, digit)
    if round(angka, digit) == round(angka, 0):
        angka = int(a)
    else:
        angka = a
   
    return angka

if geometri == geometri_list[0]:
    bentuk_list = ["Koin", "Dadu", "Kustom"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        open_image("Koin.png")
        st.write(f"A = Angka\n\nG = Gambar")
        jumlah = float(st.text_input("Jumlah (1-6)", value=3))
        st.write('## **Hasil Penyelesaian**')
        if jumlah >= 1 and jumlah <= 6:
            for a in range(int(2**jumlah)):
                hasil = ""
                for b in range(int(jumlah),0,-1):
                    angka = int(a/2**(b-1)+1e-12)%2
                    if angka == 0:
                        hasil = f"{hasil}A"
                    else:
                        hasil = f"{hasil}G"
                st.write(f"{a+1} = {hasil}")

    if bentuk == bentuk_list[1]:
        open_image("Dadu.png")
        st.write(f"A = Angka\n\nG = Gambar")
        jumlah = float(st.text_input("Jumlah (1-2)", value=1))
        st.write('## **Hasil Penyelesaian**')
        if jumlah == 1:
            img = Image.open("1 dadu.png")
            st.image(img, width=300)
        if jumlah == 2:
            img = Image.open("2 dadu.png")
            st.image(img, width=300)

    if bentuk == bentuk_list[2]:
        st.write(f"A = Angka\n\nB = Gambar")
        jumlah = float(st.text_input("Jumlah (1-6)", value=3))
        st.write('## **Hasil Penyelesaian**')
        if jumlah >= 1 and jumlah <= 6:
            for a in range(int(2**jumlah)):
                hasil = ""
                for b in range(int(jumlah),0,-1):
                    angka = int(a/2**(b-1)+1e-12)%2
                    if angka == 0:
                        hasil = f"{hasil}A"
                    else:
                        hasil = f"{hasil}B"
                st.write(f"{a+1} = {hasil}")

if geometri == geometri_list[1]:
    bentuk_list = ["Kalkulator", "Kejadian Majemuk", "Kejadian Komplemen", "Kejadian Saling Lepas", "Kejadian Tidak Saling Lepas", "Kejadian Bersyarat", "Jumlah Angka", "Frekuensi Harapan"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        st.latex(r"P(K)=\frac{n(K)}{n(S)}")
        st.write(f"K = Kejadian\n\nS = Sampel")
        a = float(st.text_input("n(K)", value=2))
        b = float(st.text_input("n(S)", value=4))
        st.write('### **Hasil Persamaan**')
        st.latex(fr"n(K)={fungsi(a)}")
        st.latex(fr"n(S)={fungsi(b)}")
        st.latex(fr"P(K)=\frac{{{fungsi(a)}}}{{{fungsi(b)}}}")
        st.write('### **Hasil Penyelesaian**')
        st.markdown(f"P(K) = {fungsi(a/b)}")

    if bentuk == bentuk_list[1]:
        st.latex(r"P(A\cap B)=P(A)\times P(B)")
        st.write(f"Jumlah kejadian A dan B secara bersamaan")
        a = float(st.text_input("P(A)", value=0.4))
        b = float(st.text_input("P(B)", value=0.6))
        st.write('### **Hasil Persamaan**')
        st.latex(fr"P(A)={fungsi(a)}")
        st.latex(fr"P(B)={fungsi(b)}")
        st.latex(fr"P(A\cap B)=P(A)\times P(B)")
        st.write('### **Hasil Penyelesaian**')
        st.latex(fr"P(A\cap B) = {fungsi(a*b)}")

    if bentuk == bentuk_list[2]:
        st.latex(r"P(K')=1-P(K)")
        st.write(f"K = Kejadian")
        a = float(st.text_input("P(K)", value=0.2))
        st.write('### **Hasil Persamaan**')
        st.latex(fr"P(K)={fungsi(a)}")
        st.write('### **Hasil Penyelesaian**')
        st.latex(fr"P(K') = {fungsi(1-a)}")

    if bentuk == bentuk_list[3]:
        st.latex(fr"P(A\cup B)=P(A)+P(B)")
        st.write(f"Jumlah kejadian A atau B secara bersamaan")
        a = float(st.text_input("P(A)", value=0.5))
        b = float(st.text_input("P(B)", value=0.3))
        st.write('### **Hasil Persamaan**')
        st.latex(fr"P(A)={fungsi(a)}")
        st.latex(fr"P(B)={fungsi(b)}")
        st.latex(fr"P(A\cup B)=P(A)+P(B)")
        st.write('### **Hasil Penyelesaian**')
        st.latex(fr"P(A\cup B) = {fungsi(a+b)}")

    if bentuk == bentuk_list[4]:
        st.latex(fr"P(A\cup B)=P(A)+P(B)-P(A\cap B)")
        st.write(f"Jumlah kejadian A atau B secara bersamaan (2)")

    if bentuk == bentuk_list[5]:
        st.latex(fr"P(B|A)=\frac{{P(A\cap B)}}{{P(A)}}")

    if bentuk == bentuk_list[6]:
        # st.latex(r"C^n_r = \frac{n!}{r!(n-r)!}")
        # st.write(f"n = Elemen\n\nr = Unsur")
        st.latex(r"P(K)=\frac{n(K)}{n(S)}")
        st.latex(r"n(K)=C^a_b=\frac{a!}{b!(a-b)!}")
        st.latex(r"n(S)=2^a")
        a = int(st.text_input("Jumlah Koin (1-10)", value=3))
        b = int(st.text_input("Jumlah Angka (1-10)", value=2))
        st.write('## **Hasil Penyelesaian**')
        st.write(f"Jumlah Gambar = {a-b}")
        st.write(f"Daftar Koin = {b}A {a-b}G")
        abab = r"\frac{{{a}}!}{b!({{a}}-{{b}})!}"
        #abab = r"\frac{{{%a}}!}{%b!({{a}}-{{b}})!}"%(a)
        st.latex(fr"n(K)={abab}={fungsi(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))}")
        st.latex(fr"n(S)={2**a}")
        st.write(f"P(Koin) = {fungsi(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)*2**a))}")

    if bentuk == bentuk_list[7]:
        st.latex(fr"Fh(A)=P(A)\times N")
        a = float(st.text_input("P(A)", value=0.4))
        b = float(st.text_input("N", value=3))
        st.write('### **Hasil Persamaan**')
        st.latex(fr"P(A)={fungsi(a)}")
        st.latex(fr"N={fungsi(b)}")
        st.write('### **Hasil Penyelesaian**')
        st.latex(fr"Fh(A) = {fungsi(a*b)}")

if geometri == geometri_list[2]:
    bentuk_list = ["Permutasi", "Permutasi berulang", "Kombinasi", "Permutasi siklis", "Kombinasi 2", "Jumlah angka"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        st.latex(r"P^n_r = \frac{n!}{(n-r)!}")
        st.write(f"n = Elemen\n\nr = Unsur")
        a = int(st.text_input("Elemen (1-10)", value=3))
        b = int(st.text_input("Unsur (1-10)", value=2))
        st.write('## **Hasil Penyelesaian**')
        hasil = fungsi(math.factorial(a)/math.factorial(a-b))
        st.latex(fr"P^{a}_{b} = {hasil}")
        st.write(f"Jumlah Kombinasi = {hasil}")

    if bentuk == bentuk_list[1]:
        st.latex(r"n(K)={{basis}}^{{jumlah}}")
        basis = float(st.text_input("Basis (2-6)", value=2))
        jumlah = float(st.text_input("Jumlah (2-6)", value=3))
        st.write('## **Hasil Penyelesaian**')
        st.write(f"Jumlah Kombinasi = {int(basis**jumlah)}")

    if bentuk == bentuk_list[2]:
        st.latex(r"C^n_r = \frac{n!}{r!(n-r)!}")
        st.write(f"n = Elemen\n\nr = Unsur")
        a = int(st.text_input("Elemen (1-10)", value=3))
        b = int(st.text_input("Unsur (1-10)", value=2))
        st.write('## **Hasil Penyelesaian**')
        st.write(f"Jumlah Kombinasi = {fungsi(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))}")

    if bentuk == bentuk_list[3]:
        st.latex(r"P^n_{siklis} = (n-1)!")
        st.write(f"n = Elemen")
        a = int(st.text_input("Elemen (1-10)", value=3))
        st.write('## **Hasil Penyelesaian**')
        hasil = fungsi(math.factorial(a-1))
        st.latex(fr"P^{a}_{{siklis}} = {hasil}")
        st.write(f"Jumlah Kombinasi = {hasil}")

def union(a2, b2):
    hasil = []
    for a in range(len(a2)):
        hasil.append(int(a2[a]))
    for a in range(len(b2)):
        if not (b2[a] in a2):
            hasil.append(int(b2[a]))
    return hasil

def intersection(a2, b2):
    hasil = []
    for a in range(len(a2)):
        if a2[a] in b2:
            hasil.append(int(a2[a]))
    return hasil

if geometri == geometri_list[3]:
    bentuk_list = ["Gabungan", "Irisan"]
    bentuk = st.selectbox(f"Pilih jenis {geometri}:", bentuk_list)

    if bentuk == bentuk_list[0]:
        # st.latex(r"n(K)={{basis}}^{{jumlah}}")
        a = st.text_input("Himpunan A", value="1,2,3,4")
        b = st.text_input("Himpunan B", value="2,3,5")
        st.write('## **Hasil Penyelesaian**')
        a2 = list(a.split(','))
        b2 = list(b.split(','))
        hasil = union(a2,b2)
        st.latex(fr"A = [{a}]")
        st.latex(fr"B = [{b}]")
        st.latex(fr"A\cup B = {hasil}")
        # st.write(f"Jumlah Kombinasi = {basis**jumlah}")

    if bentuk == bentuk_list[1]:
        # st.latex(r"n(K)={{basis}}^{{jumlah}}")
        a = st.text_input("Himpunan A", value="1,2,3,4")
        b = st.text_input("Himpunan B", value="2,3,5")
        st.write('## **Hasil Penyelesaian**')
        a2 = list(a.split(','))
        b2 = list(b.split(','))
        hasil = intersection(a2,b2)
        st.latex(fr"A = [{a}]")
        st.latex(fr"B = [{b}]")
        st.latex(fr"A\cap B = {hasil}")

# f"baca {angka}" = "baca " + str(angka)
# print = st.write = st.markdown

# f"baca {angka}" = "baca " + str(angka)
# print = st.write = st.markdown
