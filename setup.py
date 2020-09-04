"""
This library provides a set of tools that can be used in chemometrics analysis.

These tools are:

- some pre-processing methods that can be applyed in the spectra.
- an function that make average of spectra in the case of there are more than one spectra by sample (e.g. triplicate or duplicate aquisitions)
"""
DOCLINES = (__doc__ or '').split("\n")


import setuptools

setuptools.setup(
    name="preprocspectra",
    version="0.0.65",
    license='MIT',
    author="Diego José da Silva",
    author_email="diegojsilvabr@gmail.com",
    description=DOCLINES[0],
    long_description = "\n".join(DOCLINES[2:]),
    url="https://github.com/dijsilva/preprocspectra",
    packages=setuptools.find_packages(),
    download_url = 'https://github.com/dijsilva/preprocspectra/releases/tag/0.0.1',
    keywords = ['SPECTROSCOPY', 'PREPROCESSING', 'SPECTRA'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pandas>=1.0.3',
        'numpy>=1.18.3',
        'scipy>=1.4.1',
    ],
    python_requires='>=3.6'
)
