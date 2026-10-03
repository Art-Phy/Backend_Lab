from PIL import Image, ImageDraw, ImageFont

from backend_dashboard.metrics import SystemMetrics
from backend_dashboard.services import ServiceStatus


WIDTH = 320
HEIGHT = 480

BACKGROUND = (15, 23, 42)
TEXT_PRIMARY = (241, 245, 249)
TEXT_SECONDARY = (148, 163, 184)
STATUS_OK = (34, 197, 94)
STATUS_ERROR = (239, 68, 68)
BAR_BACKGROUND = (51, 65, 85)
BAR_FILL = (56, 189, 248)



def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except OSError:
        return ImageFont.load_default()



def format_uptime(seconds: float) -> str:
    total_minutes = int(seconds // 60)

    days, remaining_minutes = divmod(total_minutes, 1440)
    hours, minutes = divmod(remaining_minutes, 60)

    if days > 0:
        return f"{days}d {hours:02}h {minutes:02}m"

    return f"{hours:02}h {minutes:02}m"



def format_temperature(temperature: float | None) -> str:
    if temperature is None:
        return "N/A"

    return f"{temperature:.1f} °C"



def draw_metric_bar(
    draw: ImageDraw.ImageDraw,
    label: str,
    value: float,
    y: int,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> None:
    left = 30
    right = WIDTH - 30
    bar_top = y + 22
    bar_height = 8

    display_value = max(0.0, min(value, 100.0))

    draw.text(
        (left, y),
        label,
        font=font,
        fill=TEXT_SECONDARY,
    )

    value_text = f"{value:.1f}%"
    value_box = draw.textbbox((0, 0), value_text, font=font)
    value_width = value_box[2] - value_box[0]

    draw.text(
        (right - value_width, y),
        value_text,
        font=font,
        fill=TEXT_PRIMARY,
    )

    draw.rounded_rectangle(
        (left, bar_top, right, bar_top + bar_height),
        radius=4,
        fill=BAR_BACKGROUND,
    )

    fill_width = int((right - left) * display_value / 100)

    if fill_width > 0:
        draw.rounded_rectangle(
            (
                left,
                bar_top,
                left + fill_width,
                bar_top + bar_height,
            ),
            radius=4,
            fill=BAR_FILL,
        )



def draw_service_status(
    draw: ImageDraw.ImageDraw,
    label: str,
    is_ok: bool,
    y: int,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> None:
    status_color = STATUS_OK if is_ok else STATUS_ERROR

    draw.text(
        (30, y),
        label,
        font=font,
        fill=TEXT_SECONDARY,
    )

    draw.ellipse(
        (270, y + 3, 280, y + 13),
        fill=status_color,
    )



def create_dashboard_frame(
    metrics: SystemMetrics,
    services: ServiceStatus,
) -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)

    title_font = load_font(26)
    metric_font = load_font(15)
    info_font = load_font(14)
    service_font = load_font(13)

    title = "BACKEND LAB"

    title_box = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_box[2] - title_box[0]

    draw.text(
        ((WIDTH - title_width) // 2, 25),
        title,
        font=title_font,
        fill=TEXT_PRIMARY,
    )

    draw.ellipse(
        (29, 72, 41, 84),
        fill=STATUS_OK,
    )

    draw.text(
        (52, 68),
        "SYSTEM ONLINE",
        font=metric_font,
        fill=STATUS_OK,
    )

    draw_metric_bar(
        draw,
        "CPU",
        metrics.cpu_percent,
        110,
        metric_font,
    )

    draw_metric_bar(
        draw,
        "RAM",
        metrics.memory_percent,
        165,
        metric_font,
    )

    draw_metric_bar(
        draw,
        "DISK",
        metrics.disk_percent,
        220,
        metric_font,
    )

    draw.text(
        (30, 290),
        "TEMP",
        font=info_font,
        fill=TEXT_SECONDARY,
    )

    draw.text(
        (165, 290),
        format_temperature(metrics.temperature_c),
        font=info_font,
        fill=TEXT_PRIMARY,
    )

    draw.text(
        (30, 320),
        "UPTIME",
        font=info_font,
        fill=TEXT_SECONDARY,
    )

    draw.text(
        (165, 320),
        format_uptime(metrics.uptime_seconds),
        font=info_font,
        fill=TEXT_PRIMARY,
    )

    draw.text(
        (30, 360),
        "INFRA",
        font=info_font,
        fill=TEXT_PRIMARY,
    )

    draw_service_status(
        draw,
        "NGINX",
        services.nginx,
        390,
        service_font,
    )

    draw_service_status(
        draw,
        "DOCKER",
        services.docker,
        410,
        service_font,
    )

    draw_service_status(
        draw,
        "POSTGRES",
        services.postgres,
        430,
        service_font,
    )

    draw_service_status(
        draw,
        "BACKUP",
        services.backup,
        450,
        service_font,
    )

    return image



if __name__ == "__main__":
    from backend_dashboard.metrics import collect_system_metrics
    from backend_dashboard.services import collect_service_status

    metrics = collect_system_metrics()
    services = collect_service_status()

    frame = create_dashboard_frame(metrics, services)
    frame.save("dashboard-preview.png")

    print("Dashboard preview generated: dashboard-preview.png")
