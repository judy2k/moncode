from setuptools import setup, find_packages

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
    version='0.0.0',
    author="Mark Smith",
    author_email="judy@judy.co.uk",
    
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
)