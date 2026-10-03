from dataclasses import dataclass
import shutil
import subprocess
import time

import psutil



@dataclass
class SystemMetrics:
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    temperature_c: float | None
    uptime_seconds: float



def get_cpu_temperature() -> float | None:
    thermal_path = "/sys/class/thermal/thermal_zone0/temp"

    try:
        with open(thermal_path, "r", encoding="utf-8") as file:
            value = int(file.read().strip())
    except (FileNotFoundError, ValueError, OSError):
        return None

    return value / 1000



def collect_system_metrics() -> SystemMetrics:
    disk_usage = shutil.disk_usage("/")

    disk_percent = (
        disk_usage.used / disk_usage.total * 100
        if disk_usage.total
        else 0.0
    )

    uptime_seconds = time.time() - psutil.boot_time()

    return SystemMetrics(
        cpu_percent=psutil.cpu_percent(interval=0.2),
        memory_percent=psutil.virtual_memory().percent,
        disk_percent=disk_percent,
        temperature_c=get_cpu_temperature(),
        uptime_seconds=uptime_seconds,
    )
