import threading
import requests
import json
import time
import tkinter as tk
from flask import Flask, jsonify, render_template
from cefpython3 import cefpython as cef
import sys
import urllib3
import ctypes

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Окно загрузки
def show_loading_screen():
    loading_root = tk.Tk()
    loading_root.title("Загрузка")
    loading_root.geometry("300x100")
    loading_label = tk.Label(loading_root, text="Загрузка...", font=("Arial", 14))
    loading_label.pack(pady=20)
    loading_root.update()
    return loading_root

loading_screen = show_loading_screen()

# Flask сервер
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nojs')
def no_js():
    return render_template('nojs.html')


@app.route('/data')
def get_data():
    try:
        response = requests.get("https://iamvany.ru/api/ping", timeout=5, verify=False, headers={"Cache-Control": "no-cache"})
        response.raise_for_status()
        data = response.json()
        return jsonify({
            "cpu_usage": data['metrics'].get('cpu_usage', 'N/A'),
            "disk_usage": data['metrics'].get('disk_usage', 'N/A'),
            "memory_usage": data['metrics'].get('memory_usage', 'N/A'),
            "total_processes": data['metrics'].get('total_processes', 'N/A'),
            "status": data.get('status', 'N/A')
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

def run_flask():
    app.run(port=5000, debug=False, use_reloader=False)

# Запуск Flask в отдельном потоке
threading.Thread(target=run_flask, daemon=True).start()

# Инициализация CEF
cef.Initialize()
loading_screen.destroy()  # Закрываем окно загрузки

# Создание главного окна
window_info = cef.WindowInfo()
window_info.SetAsChild(0)  # Передаём 0, чтобы CEF сам создавал окно
browser = cef.CreateBrowserSync(window_info, url="http://127.0.0.1:5000")

# Получаем дескриптор окна
hwnd = browser.GetWindowHandle()

# Функция обновления размеров браузера
def resize_handler():
    if browser:
        cef.WindowUtils.OnSize(hwnd, 0, 0, 0)

# Обработчик изменения размеров окна
cef.PostTask(cef.TID_UI, resize_handler)

cef.MessageLoop()
cef.Shutdown()
