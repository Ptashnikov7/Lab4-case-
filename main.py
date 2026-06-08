import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# Модель: Метод Ньютона (5 семестр)
# Автор: Пташников Василь, група АІ-235

def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

def newton_method(x0, eps=0.0001):
    x = x0
    while abs(f(x)) > eps:
        if f_prime(x) == 0:
            return None
        x = x - f(x)/f_prime(x)
    return x

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Зчитуємо змінні середовища, які вимагає лабораторна
        student = os.getenv("STUDENT_NAME", "Невідомо")
        group = os.getenv("GROUP", "Невідомо")
        mode = os.getenv("MODE", "eco")
        
        # Обчислюємо корінь (за замовчуванням x0=1.0)
        root = newton_method(1.0)
        
        response_text = (
            f"--- Лабораторна робота №4 ---\n"
            f"Студент: {student}\n"
            f"Група: {group}\n"
            f"Режим роботи (MODE): {mode}\n"
            f"Модель: Метод Ньютона (5 семестр)\n"
            f"Результат обчислення (x0=1.0): {root}\n"
        )
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(response_text.encode('utf-8'))

def run():
    port = int(os.getenv("SERVICE_PORT", "8000"))
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Сервер запущено на порту {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
