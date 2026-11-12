import logging
from PIL import Image, UnidentifiedImageError

logger = logging.getLogger(__name__)

def is_valid_image(file):
    if not file:
        return False
    try:
        file.seek(0)
        with Image.open(file) as im:
            im.load()
        file.seek(0)
        return True
    except (UnidentifiedImageError, OSError) as e:
        logger.warning(
            "Invalid image %r: %r",
            getattr(file, "name", "?"),
            e,
        )
        try:
            file.seek(0)
        except Exception:
            pass
        return False