from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

EXTRAS_REQUIRE = {
    'tests': [
        "pytest",
        "coverage[toml]>=5.0.2",
    ],
}
EXTRAS_REQUIRE['dev'] = EXTRAS_REQUIRE['tests'] + [
    "prospector[pyroma]",
    "black",
    "twine",
    "wheel",
]

setup(
    name="moncode",
    description="Take code from the clipboard and format it for MongoDB slides.",
    long_description=long_description,
    long_description_content_type='text/markdown; variant=GFM',
    version='0.0.1',
    author="Mark Smith",
    author_email="judy@judy.co.uk",
    url="https://github.com/judy2k/moncode",
    
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click      ~= 7.1",
        "pyperclip  ~= 1.8",
        "pygments   ~= 2.6",
    ],
    extras_require=EXTRAS_REQUIRE,
    entry_points="""
        [console_scripts]
        moncode=moncode:main
    """,

    keywords=["tui", "console", "syntax", "formatting", "rtf", "presentation", "code"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Environment :: Console",
        "Operating System :: OS Independent",
    ],
)