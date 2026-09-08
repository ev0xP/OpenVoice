import os
from setuptools import setup, find_packages

# Membaca README.md tanpa memicu FileNotFoundError saat diproses pip
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read().strip()

setup(
    name='openvoice',
    version='2.0.0',
    description='Instant voice cloning by MyShell',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['text-to-speech', 'tts', 'voice-clone', 'zero-shot-tts'],
    url='https://github.com/ev0xP/OpenVoice',
    author='ev0xP',
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=[
        'librosa>=0.10.0',
        'faster-whisper>=0.10.0',
        'pydub>=0.25.1',
        'wavmark>=0.0.3',
        'numpy>=1.26.0',
        'eng_to_ipa>=0.0.2',
        'inflect>=7.0.0',
        'unidecode>=1.3.7',
        'whisper-timestamped>=1.14.2',
        'pypinyin>=0.50.0',
        'cn2an>=0.5.22',
        'jieba>=0.42.1',
        'langid>=1.1.6',
        'open-clip-torch>=2.20.0',
    ],
    zip_safe=False
)
