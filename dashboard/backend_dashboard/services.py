from dataclasses import dataclass
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
    try:
        result = subprocess.run(
            [
                "systemctl",
                "show",
                "backup-postgresql.service",
                "-p",
                "Result",
                "-p",
                "ExecMainStatus",
                "--value",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

    values = result.stdout.strip().splitlines()

    if len(values) != 2:
        return False

    service_result, exit_status = values

    return service_result == "success" and exit_status == "0"



def collect_service_status() -> ServiceStatus:
    return ServiceStatus(
        nginx=is_systemd_service_active("nginx"),
        docker=is_systemd_service_active("docker"),
        postgres=is_systemd_service_active("postgresql@17-main"),
        backup=was_last_backup_successful(),
    )
