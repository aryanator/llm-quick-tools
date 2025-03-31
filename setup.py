from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llm-quick-tools",
    version="0.1.1",
    author="Aryan",
    description="Prompt evaluation and mock LLM for testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aryanator/llm-tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "transformers>=4.26.0",
        "torch>=1.13.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "black>=22.0"],
    },
)