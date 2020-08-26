import setuptools

setuptools.setup(
    name="preprocspectra",
    version="0.0.1",
    license='MIT',
    author="Diego José da Silva",
    author_email="diegojsilvabr@gmail.com",
    description="A simple library to apply preprocessing of spectra obtained from infrared spectroscopy.",
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
