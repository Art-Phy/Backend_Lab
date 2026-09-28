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
    try:
        result = subprocess.run(
           ["vcgencmd", "measure_temp"],
           capture_output=True,
           text=True,
           check=True, 
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None

    output = result.stdout.strip()

    if "=" not in output:
        return None

    try:
        return float(
            output.split("=", 1)[1]
            .replace("'C", "")
        )
    except ValueError:
        return None



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
