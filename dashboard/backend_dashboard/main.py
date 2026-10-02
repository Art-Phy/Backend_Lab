import time

from backend_dashboard.display import Display
from backend_dashboard.metrics import collect_system_metrics
from backend_dashboard.renderer import create_dashboard_frame
from backend_dashboard.services import collect_service_status


UPDATE_INTERVAL = 5


def main() -> None:
    display = Display()
    display.initialize()

    try:
        while True:
            metrics = collect_system_metrics()
            services = collect_service_status()

            frame = create_dashboard_frame(metrics, services)
            display.show(frame)

            time.sleep(UPDATE_INTERVAL)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
