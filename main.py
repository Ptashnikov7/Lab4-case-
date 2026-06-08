import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# Модель: Метод Ньютона (Контейнеризація сервісу)
# Автор: Пташников Василь AI-235.

def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

def newton_method(x0, eps=0.0001):
    x = x0
    while abs(f(x)) > eps:
        # Проверка на ноль, чтобы избежать ZeroDivisionError
        if f_prime(x) == 0:
            return None
        x = x - f(x)/f_prime(x)
    return x

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Читаем начальное значение x0 из переменной среды (дефолт: 1.0)
        env_x0 = os.getenv("NEWTON_X0", "1.0")
        
        try:
            x0 = float(env_x0)
            root = newton_method(x0)
            response_text = f"Newton Method Result (x0={x0}): Root is {root}\n"
            self.send_response(200)
        except ValueError:
            response_text = f"Error: Invalid NEWTON_X0 variable value '{env_x0}'\n"
            self.send_response(400)
            
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(response_text.encode('utf-8'))

def run():
    # Порт также выносим в переменную среды, по умолчанию 8000
    port = int(os.getenv("SERVICE_PORT", "8000"))
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Сервер запущено на порту {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
