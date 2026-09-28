import importlib
import os
import sys
from pathlib import Path

from PIL import Image


DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 480
DEFAULT_PORT = "/dev/ttyACM0"


class Display:
    def __init__(
        self,
        port: str = DEFAULT_PORT,
        driver_path: str | None = None,
    ) -> None:
        self.port = port
        self.driver_path = driver_path or os.getenv("TURING_DRIVER_PATH")

        if not self.driver_path:
            raise RuntimeError(
                "TURING_DRIVER_PATH is not configured."
            )

        driver_root = Path(self.driver_path).expanduser().resolve()

        if not driver_root.exists():
            raise RuntimeError(
                f"Turing driver path does not exist: {driver_root}"
            )

        sys.path.insert(0, str(driver_root))

        module = importlib.import_module(
            "library.lcd.lcd_comm_rev_a"
        )

        lcd_comm_class = module.LcdCommRevA
        self._orientation = module.Orientation

        self._lcd = lcd_comm_class(
            com_port=self.port,
            display_width=DISPLAY_WIDTH,
            display_height=DISPLAY_HEIGHT,
        )

    def initialize(self) -> None:
        self._lcd.Reset()
        self._lcd.InitializeComm()
        self._lcd.SetBrightness(level=10)
        self._lcd.SetOrientation(
            orientation=self._orientation.PORTRAIT
        )

    def show(self, image: Image.Image) -> None:
        if image.size != (DISPLAY_WIDTH, DISPLAY_HEIGHT):
            raise ValueError(
                f"Expected image size "
                f"{DISPLAY_WIDTH}x{DISPLAY_HEIGHT}, "
                f"got {image.width}x{image.height}"
            )

        self._lcd.DisplayPILImage(image)
