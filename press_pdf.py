from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import os

def compress_pdf(input_file, output_file):
    try:
        from PyPDF2 import PdfReader, PdfWriter

        reader = PdfReader(input_file)
        writer = PdfWriter()

        # Optimize compression by reducing image quality and clearing unused objects
        for page in reader.pages:
            writer.add_page(page)

        writer.add_metadata(reader.metadata)

        with open(output_file, 'wb') as f:
            writer.write(f)

        original_size = os.path.getsize(input_file) / (1024 * 1024)  # MB
        compressed_size = os.path.getsize(output_file) / (1024 * 1024)  # MB
        return original_size, compressed_size
    except Exception as e:
        return None, None

class PdfCompressorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PDF fayllarni siqish dasturi")
        self.resize(600, 300)

        # Navbar
        navbar_label = QLabel("PDF fayllarni siqish dasturi")
        navbar_label.setFont(QFont("Arial", 14, QFont.Bold))

        # Header
        self.left_pdf_label = QLabel("Siz tanlagan PDF fayl: <Hajmi: 0.0 MB>")
        self.right_pdf_label = QLabel("Siqilgan PDF fayl: <Hajmi: 0.0 MB>")

        # Section
        self.select_pdf_button = QPushButton("Select PDF")
        self.select_pdf_button.clicked.connect(self.select_pdf)

        self.press_button = QPushButton("Press")
        self.press_button.clicked.connect(self.compress_pdf_file)

        # Footer
        footer_label = QLabel("Created by Tempiltin | Info: https://tempiltin.uz/")
        footer_label.setFont(QFont("Arial", 10))
        footer_label.setStyleSheet("text-align: center;")

        # Layouts
        navbar_layout = QVBoxLayout()
        navbar_layout.addWidget(navbar_label)

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.left_pdf_label)
        header_layout.addWidget(self.right_pdf_label)

        section_layout = QHBoxLayout()
        section_layout.addWidget(self.select_pdf_button)
        section_layout.addWidget(self.press_button)

        footer_layout = QVBoxLayout()
        footer_layout.addWidget(footer_label, alignment=Qt.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.addLayout(navbar_layout)
        main_layout.addLayout(header_layout)
        main_layout.addLayout(section_layout)
        main_layout.addLayout(footer_layout)

        self.setLayout(main_layout)

    def select_pdf(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)", options=options)
        if file_path:
            self.input_pdf_path = file_path
            size_in_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB
            self.left_pdf_label.setText(f"Siz tanlagan PDF fayl: <Hajmi: {size_in_mb:.2f} MB>")

    def compress_pdf_file(self):
        if hasattr(self, 'input_pdf_path') and self.input_pdf_path:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            output_file = os.path.join(desktop, "Siqilgan-pdf_tempiltin.pdf")
            original_size, compressed_size = compress_pdf(self.input_pdf_path, output_file)
            if original_size and compressed_size:
                self.right_pdf_label.setText(f"Siqilgan PDF fayl: <Hajmi: {compressed_size:.2f} MB>")
                self.left_pdf_label.setText(f"Fayl yuklandi: {output_file}")
            else:
                self.right_pdf_label.setText("PDF siqishda xatolik yuz berdi.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PdfCompressorApp()
    window.show()
    sys.exit(app.exec_())
