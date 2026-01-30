from setuptools import setup, find_packages

setup(
    name="imei-tracker-pro",
    version="1.0.0",
    author="Cyber Security Research",
    author_email="security@example.com",
    description="Advanced Real-Time IMEI Location Tracking Tool",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/imei-tracker-pro",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Communications :: Telephony",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.31.0",
        "Pillow>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "imei-tracker=imei_tracker:main",
        ],
    },
)
