from backend_dashboard.display import Display
from backend_dashboard.metrics import collect_system_metrics
from backend_dashboard.renderer import create_dashboard_frame



def main() -> None:
    metrics = collect_system_metrics()
    frame = create_dashboard_frame()

    display = Display()
    display.initialize()
    display.show(frame)


if __name__ == "__main__":
    main()
