from PIL import Image, ImageDraw, ImageFont

WIDTH = 320
HEIGHT =480

BACKGROUND = (15, 23, 42)
TEXT_PRIMARY = (241, 245, 249)
TEXT_SECONDARY = (148, 163, 184)
STATUS_OK = (34, 197, 94)


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except OSError:
        return ImageFont.load_default()



def create_dashboard_frame() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)

    title_font = load_font(28)
    status_font = load_font(22)
    body_font = load_font(16)

    title = "BACKEND LAB"
    status = "ONLINE"
    subtitle = "Raspberry Pi Server"

    title_box = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_box[2] - title_box[0]

    draw.text(
        ((WIDTH - title_width) // 2, 100),
        title,
        font=title_font,
        fill=TEXT_PRIMARY,
    )

    status_box = draw.textbbox((0, 0), status, font=status_font)
    status_width = status_box[2] - status_box[0]

    status_y = 190
    dot_radius = 6
    gap = 12

    group_width = (dot_radius * 2) + gap + status_width
    group_x = (WIDTH - group_width) // 2

    dot_center_x = group_x + dot_radius
    dot_center_y = status_y + 12

    draw.ellipse(
        (
            dot_center_x - dot_radius,
            dot_center_y - dot_radius,
            dot_center_x + dot_radius,
            dot_center_y + dot_radius,
        ),
        fill=STATUS_OK,
    )

    draw.text(
        (group_x + dot_radius * 2 + gap, status_y),
        status,
        font=status_font,
        fill=STATUS_OK,
    )

    subtitle_box = draw.textbbox((0, 0), subtitle, font=body_font)
    subtitle_width = subtitle_box[2] - subtitle_box[0]

    draw.text(
        ((WIDTH - subtitle_width) // 2, 260),
        subtitle,
        font=body_font,
        fill=TEXT_SECONDARY,
    )

    return image


if __name__== "__main__":
    frame = create_dashboard_frame()
    frame.save("dashboard-preview.png")

    print("Dashboard preview generated: dashboard-preview.png")
