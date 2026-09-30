from backend_dashboard.display import Display
from backend_dashboard.metrics import collect_system_metrics
from backend_dashboard.renderer import create_dashboard_frame
from backend_dashboard.services import collect_service_status



def main() -> None:
    metrics = collect_system_metrics()
    services = collect_service_status()

    frame = create_dashboard_frame(metrics, services)

    display = Display()
    display.initialize()
    display.show(frame)


if __name__ == "__main__":
    main()
