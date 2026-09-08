from setuptools import setup, find_packages

setup(
    name="openvoice",
    version="2.0.0",
    packages=find_packages(include=["openvoice", "openvoice.*"]),
    include_package_data=True,
    install_requires=[
        "torch>=2.0.0",
        "torchaudio>=2.0.0",
        "librosa>=0.10.0",
        "faster-whisper>=0.10.0",
        "wavmark>=0.0.3",
        "open-clip-torch>=2.20.0",
    ],
)
