import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="watson_text_talker",
    version="0.8.10",
    author="Jeff Greenberg",
    author_email="jeff@ziligy.com",
    description="Simple Text-to-Speech Interface for Raspberry Pi using IBM's Watson TTS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ziligy/watson-text-talker",
    packages=setuptools.find_packages(),
    install_requires=['watson-developer-cloud', 'pygame', 'python-slugify'],
    license = "MIT",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)