"""
Setup configuration for Analizador Lexile Chile
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="analizador-lexile-chile",
    version="1.0.0",
    author="Claudio Rojas",
    author_email="",
    description="Analizador de nivel Lexile para textos en español, adaptado al sistema educativo chileno",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ClaudioRojasMon/analizador-lexile-chile",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Natural Language :: Spanish",
    ],
    python_requires=">=3.7",
    install_requires=[
        "spacy>=2.3.0,<4.0.0",
        "numpy>=1.20.0",
        "PyPDF2>=3.0.0",
        "pdfplumber>=0.9.0",
    ],
    entry_points={
        'console_scripts': [
            'lexile=main:main',
        ],
    },
    keywords="lexile, readability, spanish, education, chile, nlp, text-analysis",
    project_urls={
        "Bug Reports": "https://github.com/ClaudioRojasMon/analizador-lexile-chile/issues",
        "Source": "https://github.com/ClaudioRojasMon/analizador-lexile-chile",
    },
)
