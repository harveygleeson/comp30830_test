import socket
import platform
import multiprocessing
import psutil

print(socket.gethostname())
print(platform.system())
print(platform.version())
print(multiprocessing.cpu_count())
print(psutil.virtual_memory().total, "bytes")
