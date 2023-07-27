from PIL import Image
from file_packer import FilePackReader

try:
    import cv2
    CV2_IMPORTED = True
except ImportError as err:
    CV2_IMPORTED = False
import os

_fopen = open


def open(path, mode, file_reader=None, *args, **kwargs):
    if isinstance(file_reader, FilePackReader):
        return file_reader.open(path, mode, *args, **kwargs)
    else:
        return _fopen(path, mode, *args, **kwargs)


def listdir(path, file_reader=None, *args, **kwargs):
    if isinstance(file_reader, FilePackReader):
        return file_reader.listdir(path, *args, **kwargs)
    else:
        return sorted(os.listdir(path))


def walk(path, file_reader=None, *args, **kwargs):
    if isinstance(file_reader, FilePackReader):
        return file_reader.walk(path, *args, **kwargs)
    else:
        return os.walk(path, *args, **kwargs)


def exists(path, file_reader=None, *args, **kwargs):
    if isinstance(file_reader, FilePackReader):
        return file_reader.exists(path, *args, **kwargs)
    else:
        return os.path.exists(path)


def isdir(path, file_reader=None, *args, **kwargs):
    if isinstance(file_reader, FilePackReader):
        return file_reader.isdir(path, *args, **kwargs)
    else:
        return os.path.isdir(path)


def isfile(path, file_reader=None, *args, **kwargs):
    if isinstance(file_reader, FilePackReader):
        return file_reader.isfile(path, *args, **kwargs)
    else:
        return os.path.isfile(path)


def cv2_imread(path, file_reader, *args, **kwargs):
    if not CV2_IMPORTED:
        raise EnvironmentError("This method in not usable since cv2 could not be imported.")
    if isinstance(file_reader, FilePackReader):
        return file_reader.cv2_imread(path, *args, **kwargs)
    else:
        if "exclude_base_path" in kwargs:
            del kwargs["exclude_base_path"]
        return cv2.imread(path, *args, **kwargs)


def PIL_imread(path, file_reader, exclude_base_path=False, mode="r"):
    if isinstance(file_reader, FilePackReader):
        return Image.open(file_reader.open(path, exclude_base_path), mode)
    else:
        return Image.open(path, mode)
