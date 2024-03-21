import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

from PyPDF2 import PdfReader, PdfWriter


class PdfDivider(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Divider")
        self.setFixedSize(400, 300)  # Ekran boyutunu sabitle

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)
        self.setWindowIcon(QIcon('logo.ico'))

        # PDF dosyasını seçmek için düğme ve etiket
        self.select_pdf_button = QPushButton("PDF Seç")
        self.select_pdf_button.clicked.connect(self.select_pdf)
        layout.addWidget(self.select_pdf_button)

        self.selected_pdf_label = QLabel()
        layout.addWidget(self.selected_pdf_label)

        # Aralıkları girmek için etiket ve giriş kutusu
        self.interval_label = QLabel("Aralıkları girin<br>Birden çok aralık için virgül kullanın (örn. 120-130, 145-180):")
        layout.addWidget(self.interval_label)

        self.interval_edit = QLineEdit()
        layout.addWidget(self.interval_edit)

        # Çıktı dosyasını kaydetmek için düğme
        self.save_output_button = QPushButton("Çıktıyı Kaydet")
        self.save_output_button.clicked.connect(self.save_output)
        layout.addWidget(self.save_output_button)

        # Başarılı bir şekilde kaydedildi metni için etiket
        self.success_label = QLabel()
        layout.addWidget(self.success_label)

        # Kaydedildikten sonra dosya konumuna gitmek için düğme
        self.open_folder_button = QPushButton("Dosya Konumuna Git")
        self.open_folder_button.clicked.connect(self.open_folder)
        self.open_folder_button.setVisible(False)  # Başlangıçta gizli
        layout.addWidget(self.open_folder_button)

        self.setLayout(layout)

    def select_pdf(self):
        # PDF dosyasını seçme iletişim kutusunu aç
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.selected_pdf = selected_files[0]
                self.selected_pdf_label.setText(f"Seçilen PDF: {self.selected_pdf}")

    def save_output(self):
        # Aralıkları al
        intervals = self.interval_edit.text().split(',')

        # Tüm aralıkları birleştir
        all_pages_to_extract = []
        for interval in intervals:
            # Aralıkta sadece bir sayfa numarası varsa, başlangıç ve bitiş sayfası olarak aynı sayfa kabul edilir
            if '-' not in interval:
                page = int(interval)
                all_pages_to_extract.append((page, page))
            else:
                start, end = map(int, interval.split('-'))
                all_pages_to_extract.append((start, end))

        # Çıktı PDF dosyasını kaydetme iletişim kutusunu aç
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setDefaultSuffix(".pdf")
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        if file_dialog.exec_():
            save_path = file_dialog.selectedFiles()[0]

            # PDF'i böl
            self.split_pdf(self.selected_pdf, save_path, all_pages_to_extract)

    def split_pdf(self, input_pdf, output_pdf, pages_to_extract):
        # Giriş PDF dosyasını oku
        input_pdf = PdfReader(input_pdf)

        # Çıktı PDF dosyasını oluştur
        output = PdfWriter()

        # Belirtilen sayfa aralıklarındaki sayfaları çıktıya ekle
        for page_start, page_end in pages_to_extract:
            for page_num in range(page_start, page_end + 1):
                output.add_page(input_pdf.pages[page_num - 1])

        # Çıktı PDF dosyasını yaz
        with open(output_pdf, "wb") as outputStream:
            output.write(outputStream)
            self.selected_pdf_label.setText(f"Çıktı PDF: {output_pdf}")
            self.success_label.setText("Başarılı bir şekilde kaydedildi")  # Başarılı bir şekilde kaydedildi metnini göster


        self.open_folder_button.setVisible(True)  # Dosya konumuna git düğmesini görünür yap

    def open_folder(self):
        # Dosya konumuna git
        file_path = os.path.dirname(self.save_output_button.text())
        os.startfile(file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PdfDivider()
    window.show()
    sys.exit(app.exec_())
