from dataclasses import dataclass
from pathlib import Path
import subprocess



@dataclass
class ServiceStatus:
    nginx: bool
    docker: bool
    postgres: bool
    backup: bool


def is_systemd_service_active(service: str) -> bool:
    try:
        result = subprocess.run(
            ["systemctl", "is-active", "--quiet", service],
            capture_output=True,
        )
    except FileNotFoundError:
        return False

    return result.returncode == 0



def was_last_backup_successful() -> bool:
    status_file = (
        Path.home()
        / ".local"
        / "state"
        / "backend-lab"
        / "backup-postgresql.status"
    )

    try:
        status = status_file.read_text(encoding="utf-8").strip()
    except OSError:
        return False

    return status == "success"



def collect_service_status() -> ServiceStatus:
    return ServiceStatus(
        nginx=is_systemd_service_active("nginx"),
        docker=is_systemd_service_active("docker"),
        postgres=is_systemd_service_active("postgresql@17-main"),
        backup=was_last_backup_successful(),
    )
