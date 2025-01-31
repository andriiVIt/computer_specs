# hardware_info.py
import os
import platform
import socket
import psutil
import cpuinfo
import GPUtil

class HardwareInfo:
    """Class to retrieve system and hardware information."""

    def __init__(self):
        self.hostname = socket.gethostname()
        self.system = platform.system()
        self.architecture = platform.machine()
        self.kernel = platform.release()
        self.compiler = platform.python_compiler()
        self.cpu = cpuinfo.get_cpu_info()["brand_raw"]
        self.cores_physical = psutil.cpu_count(logical=False)
        self.cores_logical = psutil.cpu_count(logical=True)
        self.ram_total = round(psutil.virtual_memory().total / (1024 ** 3), 1)
        self.disk_total = round(psutil.disk_usage('/').total / (1024 ** 3), 1)

    def get_gpu_info(self):
        """Retrieve GPU information."""
        gpus = GPUtil.getGPUs()
        if not gpus:
            return "No information! Probably the GPU is onboard!"
        else:
            return [(gpu.name, gpu.memoryTotal) for gpu in gpus]

    def get_ram_usage(self):
        """Retrieve RAM usage."""
        ram = psutil.virtual_memory()
        return round(ram.used / (1024 ** 3), 1), self.ram_total, ram.percent

    def get_disk_usage(self):
        """Retrieve Disk usage."""
        disk = psutil.disk_usage('/')
        return round(disk.used / (1024 ** 3), 1), self.disk_total, disk.percent
