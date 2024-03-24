class NeoPixel:
    """
    Fake NeoPixel class for testing on non-Raspberry Pi platforms.
    """

    def __init__(
        self,
        pin,
        n: int,
        *,
        bpp: int = 3,
        brightness: float = 1.0,
        auto_write: bool = True,
        pixel_order: str = None
    ):
        pass
