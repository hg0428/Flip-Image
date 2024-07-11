from setuptools import setup

APP = ["image-flipper.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "icons/icon.icns",
    "packages": ["PIL"],
    "plist": {
        "CFBundleIconFile": "icons/icon.icns",  # Window icon for macOS
        "CFBundleName": "Image Flipper",  # Application name
        "CFBundleShortVersionString": "0.0.1",  # Application version
        "CFBundleGetInfoString": "Image Flipper App",  # Information string
        "CFBundleExecutable": "image-flipper",  # Executable file name
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
