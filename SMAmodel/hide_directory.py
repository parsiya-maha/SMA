import os


def hide(path):
    os.system(f"attrib +s +h {path}")

def unhide(path):
    os.system(f"attrib -s -h {path}")
    