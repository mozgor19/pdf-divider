from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_pdf, start_page, end_page):
    # Giriş PDF dosyasını oku
    input_pdf = PdfReader(input_pdf)
    
    # Çıktı PDF dosyasını oluştur
    output = PdfWriter()
    
    # Belirtilen sayfa aralığındaki sayfaları çıktıya ekle
    for page_num in range(start_page - 1, end_page):
        output.add_page(input_pdf.pages[page_num])
    
    # Çıktı PDF dosyasını yaz
    with open(output_pdf, "wb") as outputStream:
        output.write(outputStream)

# Örnek kullanım
input_pdf_file = "ornek.pdf"
output_pdf_file = "cikti.pdf"
start_page = 238
end_page = 257

split_pdf(input_pdf_file, output_pdf_file, start_page, end_page)
