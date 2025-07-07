import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="muDIC",
    version="0.2.1",
    author="PolymerGuy",
    author_email="sindre.n.olufsen@ntnu.no",
    description="A digital image correlation toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PolymerGuy/muDIC",
    packages=setuptools.find_packages(),
    install_requires=[
        'numba',
        'scipy',
        'matplotlib',
        'numpy',
        'Pillow',
        'dill',
        # 'nose',  # latest version 1.3.7 on 02 Jun 2025, no longer supported
        'pytest',  # use pytest instead of nose
        'scikit-image',
        'muDIC',
        'natsort',
        'noise'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
