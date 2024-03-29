import os
import uuid

__all__ = (
    'get_random_filename',
)


def get_random_filename(filename):
    """Get random filename.

    Generation random filename that contains unique identifier and
    filename extension like: ``photo.jpg``.

    Args:
        filename (str): Name of file.

    Returns:
        new_filename (str): ``9841422d-c041-45a5-b7b3-467179f4f127.ext``.

    """
    path = str(uuid.uuid4())
    ext = os.path.splitext(filename)[1]
    new_filename = path + ext.lower()

    return new_filename
