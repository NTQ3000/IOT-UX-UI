import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class WebDataApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Data App')
        
        # Tạo layout
        layout = QVBoxLayout()

        # Tạo nhãn để hiển thị dữ liệu
        self.data_label = QLabel('Dữ liệu: Chưa có', self)
        layout.addWidget(self.data_label)

        # Tạo nút để lấy dữ liệu
        self.fetch_button = QPushButton('Lấy Dữ Liệu', self)
        self.fetch_button.clicked.connect(self.fetch_data)
        layout.addWidget(self.fetch_button)

        # Thiết lập layout cho widget
        self.setLayout(layout)

        self.show()

    def fetch_data(self):
        try:
            # Gửi yêu cầu HTTP đến trang web
            response = requests.get('http://127.0.0.1:5500/web-app/index.html')
            response.raise_for_status()  # Kiểm tra lỗi

            # Phân tích cú pháp HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Giả sử bạn muốn lấy nội dung của một thẻ <div> với class "data"
            data_div = soup.find('div', class_='data')  # Thay đổi theo cấu trúc HTML của bạn
            if data_div:
                data_text = data_div.get_text()
                self.data_label.setText(f'Dữ liệu: {data_text}')
            else:
                self.data_label.setText('Không tìm thấy dữ liệu')
        except requests.exceptions.RequestException as e:
            self.data_label.setText(f'Lỗi: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebDataApp()
    sys.exit(app.exec_())
