import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Uygulamamızı başlatalım
app = Flask(__name__)
app.secret_key = 'cok_gizli_anahtar'

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Arabaların listelendiği sayfa
@app.route('/arabalar')
def arabalar_sayfasi():
    return render_template('arac_liste.html')

# Müşterinin daha önceki kiralamalari ve rezervasyonlari
@app.route('/rezervasyonlarim')
def kullanici_rezervasyonlari():
    return render_template('rezervasyonlarim.html')

# İletişim sayfası
@app.route('/iletisim')
def iletisim_sayfasi():
    return render_template('iletisim.html')

# Giriş yapma sayfası
@app.route('/giris')
def kullanici_girisi():
    return render_template('giris.html')

# Admin girişi sayfası
@app.route('/admin')
def admin_girisi():
    return render_template('admin_giris.html')

# Admin paneli sayfası
@app.route('/admin/panel')
def admin_paneli():
    return render_template('admin_paneli.html')

# Araç listesi (admin paneli içindeki)
@app.route('/admin/araclar')
def admin_arac_listesi():
    return render_template('arac_liste.html')

# Yeni araç ekleme formu
@app.route('/admin/arac/ekle')
def arac_ekleme_formu():
    return render_template('arac_ekle.html')

# Kayıt olma sayfası
@app.route('/kayit')
def kayit_sayfasi():
    return render_template('kayit.html')

# Hoş geldin sayfası
@app.route('/hosgeldin')
def hosgeldin():
    return render_template('karsilama.html')

# Profil sayfası
@app.route('/profil')
def profil_sayfasi():
    return render_template('profil.html')

# Profil detayları sayfası
@app.route('/profil/detay')
def profil_detay_sayfasi():
    return render_template('profil-detay.html')

# Ayarlar sayfası
@app.route('/ayarlar')
def ayarlar_sayfasi():
    return render_template('ayarlar.html')

# Tüm arabaların listesi (kullanıcılar için)
@app.route('/arabalarimiz')
def tum_arabalar_sayfasi():
    return render_template('arabalarimiz.html')

# Belirli bir aracın detay sayfası (şimdilik ID alıyor)
@app.route('/araba/<int:arac_id>')
def araba_detay(arac_id):
    return f"Araba Detayları (ID: {arac_id}) (şimdilik backend yok)"

# Admin paneli sayfası (tekrar)
@app.route('/admin-paneli')
def admin_paneli_sayfasi_tekrar():
    return render_template('admin_paneli.html')

# Araç ekleme sayfası (tekrar)
@app.route('/admin/arac-ekle')
def admin_arac_ekle_sayfasi():
    return render_template('arac_ekle.html')

if __name__ == '__main__':
    app.run(debug=True)