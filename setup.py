import setuptools

setuptools.setup(
	name="preprocspectra",
	version="0.0.1",
    author="Diego José da Silva",
    author_email="diegojsilvabr@gmail.com",
    description="A simple library to apply preprocessing of spectra obtained from infrared spectroscopy.",
    url="https://github.com/dijsilva/spectra-transform",
    packages=setuptools.find_packages(),
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
