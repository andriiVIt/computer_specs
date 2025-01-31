# system_info.py
from hardware_info import HardwareInfo

class SystemInfo:
    """Class to display system information."""

    def __init__(self):
        self.hardware = HardwareInfo()

    def display_info(self):
        """Print system and hardware information."""
        print("———- System Info ———-")
        print(f"Hostname     : {self.hardware.hostname}")
        print(f"System       : {self.hardware.system} {self.hardware.architecture}")
        print(f"Kernel       : {self.hardware.kernel}")
        print(f"Compiler     : {self.hardware.compiler}")
        print(f"CPU          : {self.hardware.cpu}")
        print(f"Cores        : {self.hardware.cores_physical} Physical, {self.hardware.cores_logical} Logical")
        print(f"Memory       : {self.hardware.ram_total} GiB")
        print(f"Disk         : {self.hardware.disk_total} GiB")

        print("\n———- GPU ———-")
        gpus = self.hardware.get_gpu_info()
        if isinstance(gpus, str):
            print(gpus)
        else:
            for gpu_name, gpu_memory in gpus:
                print(f"GPU          : {gpu_name}")
                print(f"Memory Total : {gpu_memory} MB")

        print("\n———- RAM & Disk usage ———-")
        ram_used, ram_total, ram_percent = self.hardware.get_ram_usage()
        print(f"RAM Used     : {ram_used} GiB / {ram_total} GiB ({ram_percent} %)")
        
        disk_used, disk_total, disk_percent = self.hardware.get_disk_usage()
        print(f"Disk Used    : {disk_used} GiB / {disk_total} GiB ({disk_percent} %)")
