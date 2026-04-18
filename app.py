import streamlit as st
import google.generativeai as genai
from PIL import Image

# Sayfa Ayarları
st.set_page_config(page_title="InDesign Soru Çevirici (Gemini)", layout="centered")

st.title("✍️ Gemini El Yazısı - InDesign Dizgi")
st.markdown("Hocanın kağıdını yükle, InDesign'a yapıştırmaya hazır metni al.")

# API Key Girişi
api_key = st.text_input("Gemini API Anahtarınızı Girin:", type="password")

# Sabit Talimatlar (Sistem Promptu)
SISTEM_TALIMATI = """
Sen bir profesyonel dizgi uzmanısın. Görseldeki el yazısı metinleri ve matematiksel ifadeleri oku.
Kurallar:
1. Her soruyu ve şıkları orijinal sırayla yaz. Sorular arasında bir satır boşluk bırak.
2. Şıkları (A, B, C, D, E) her biri ayrı satırda olacak şekilde alt alta yaz.
3. Matematiği sadeleştir: Kesirleri (3x+5)/2, üslü sayıları x^2, karekökleri kök(x) olarak yaz.
4. Grafik veya şekil varsa [ŞEKİL EKLENECEK] notu düş.
5. Sadece metni ver, ek açıklama yapma.
"""

uploaded_file = st.file_uploader("Görseli Yükle", type=['png', 'jpg', 'jpeg'])

if uploaded_file and api_key:
    if st.button("Metne Çevir"):
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')            
            # Görseli hazırla
            img = Image.open(uploaded_file)
            
            with st.spinner("Gemini sayfayı inceliyor..."):
                response = model.generate_content([SISTEM_TALIMATI, img])
                
                st.success("Çeviri Tamamlandı!")
                st.text_area("InDesign Metni:", value=response.text, height=400)
                
                st.download_button(
                    label="Dosyayı İndir (.txt)",
                    data=response.text,
                    file_name="indesign_sorular.txt",
                    mime="text/plain"
                )
        except Exception as e:
            st.error(f"Hata: {e}")
