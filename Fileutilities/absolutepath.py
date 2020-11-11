from pathlib import Path

def absolute_Path(filepath):
    relative = Path(filepath)
    return relative.absolute()