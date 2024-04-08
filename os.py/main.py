import platform  # Импорт модуля platform для получения информации об операционной системе
import psutil  # Импорт модуля psutil для работы с системными ресурсами
import socket  # Импорт модуля socket для работы с сетевыми операциями
import time  # Импорт модуля time для работы со временем
import os

def get_os_info():
    try:
        os_info = platform.platform()  # Получение информации об операционной системе
    except Exception as e:
        os_info = f"Error retrieving OS information: {e}"  # Обработка ошибки, если информацию не удалось получить
    return os_info

def get_processor_info():
    try:
        processor_info = platform.processor()  # Получение информации о процессоре
    except Exception as e:
        processor_info = f"Error retrieving processor information: {e}"  # Обработка ошибки, если информацию не удалось получить
    return processor_info

def get_memory_info():
    try:
        memory_info = psutil.virtual_memory().total / (1024 ** 3)  # Получение информации о памяти
    except Exception as e:
        memory_info = f"Error retrieving memory information: {e}"  # Обработка ошибки, если информацию не удалось получить
    return memory_info

def get_available_disk_space():
    try:
        disk_info = psutil.disk_usage('/').free / (1024 ** 3)  # Получение информации о доступном дисковом пространстве
    except Exception as e:
        disk_info = f"Error retrieving disk space information: {e}"  # Обработка ошибки, если информацию не удалось получить
    return disk_info

def get_current_user():
    try:
        current_user = platform.node()  # Получение имени текущего пользователя
    except Exception as e:
        current_user = f"Error retrieving current user information: {e}"  # Обработка ошибки, если информацию не удалось получить
    return current_user

def get_ip_address():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())  # Получение IP-адреса
    except Exception as e:
        ip_address = f"Error retrieving IP address: {e}"  # Обработка ошибки, если информацию не удалось получить
    return ip_address

def get_system_uptime():
    try:
        uptime = time.time() - psutil.boot_time()  # Получение времени работы системы
    except Exception as e:
        uptime = f"Error retrieving system uptime: {e}"  # Обработка ошибки, если информацию не удалось получить
    return uptime

def get_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)  # Получение информации об использовании CPU
    except Exception as e:
        cpu_usage = f"Error retrieving CPU usage: {e}"  # Обработка ошибки, если информацию не удалось получить
    return cpu_usage

def get_running_processes():
    try:
        running_processes = len(psutil.pids())  # Получение количества запущенных процессов
    except Exception as e:
        running_processes = f"Error retrieving running processes: {e}"  # Обработка ошибки, если информацию не удалось получить
    return running_processes


def get_disk_partitions():
    try:
        disk_partitions = psutil.disk_partitions()  # Получение информации о разделах диска
    except Exception as e:
        disk_partitions = f"Error retrieving disk partitions: {e}"  # Обработка ошибки, если информацию не удалось получить
    return disk_partitions

def get_system_architecture():
    try:
        system_architecture = platform.architecture()[0]  # Получение архитектуры системы (32-битная или 64-битная)
    except Exception as e:
        system_architecture = f"Error retrieving system architecture: {e}"  # Обработка ошибки, если информацию не удалось получить
    return system_architecture

def get_environment_variables():
    try:
        environment_variables = dict(os.environ)  # Получение переменных окружения
    except Exception as e:
        environment_variables = f"Error retrieving environment variables: {e}"  # Обработка ошибки, если информацию не удалось получить
    return environment_variables



if __name__ == "__main__":
    print("OS Name and Version:", get_os_info())  # Вывод информации об операционной системе
    print("Processor Information:", get_processor_info())  # Вывод информации о процессоре
    print("Memory (GB):", get_memory_info())  # Вывод информации о памяти
    print("Available Disk Space (GB):", get_available_disk_space())  # Вывод информации о доступном дисковом пространстве
    print("Current User:", get_current_user())  # Вывод имени текущего пользователя
    print("IP Address:", get_ip_address())  # Вывод IP-адреса
    print("System Uptime (seconds):", get_system_uptime())  # Вывод времени работы системы
    print("CPU Usage (%):", get_cpu_usage())  # Вывод информации об использовании CPU
    print("Running Processes:", get_running_processes())  # Вывод количества запущенных процессов
    print("Disk Partitions:", get_disk_partitions())  # Вывод информации о разделах диска
    print("System Architecture:", get_system_architecture())  # Вывод архитектуры системы
    print("Environment Variables:", get_environment_variables())  # Вывод переменных окружения