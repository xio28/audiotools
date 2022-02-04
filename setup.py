from setuptools import find_packages
from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="audiotools",
    version="0.1.5",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Topic :: Artistic Software",
        "Topic :: Multimedia",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Editors",
        "Topic :: Software Development :: Libraries",
    ],
    description="Utilities for handling audio.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Prem Seetharaman",
    author_email="prem@descript.com",
    license="MIT",
    packages=find_packages(),
    package_data={"": ["core/templates/headers.html", "core/templates/widget.html"]},
    install_requires=[
        "numpy",
        "soundfile",
        "pyloudnorm",
        "importlib-resources",
        "scipy",
        "torch",
        "julius",
        "torchaudio",
        "ffmpy",
        "ipython",
        "rich",
        "matplotlib",
        "librosa",
        "pystoi",
        "torch_stoi",
    ],
    extras_require={
        "tests": ["pytest", "pytest-cov", "line_profiler", "tqdm", "pesq"],
    },
)
