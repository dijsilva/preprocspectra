# Preprocspectra
### A lib with preprocessing methods for spectral data

[![PyPI Latest Release](https://img.shields.io/pypi/v/preprocspectra.svg)](https://pypi.org/project/preprocspectra/)
[![License](https://img.shields.io/pypi/l/preprocspectra.svg)](https://github.com/dijsilva/preprocspectra/blob/master/LICENSE)

This library provides a set of tools that can be used in chemometrics analysis.
These tools are:
 - Some pre-processing methods that can be applyed in the spectra.
 - A function that make average of spectra in the case of there are more than one spectra by sample (e.g. triplicate or duplicate aquisitions)

## Install
```sh
# PyPI
pip install preprocspectra
```

## Usage
### Applying pre-processing methods
It is possible to use a few treatments at a time or all at once.
```python
from preprocspectra import make_transformations
```
The function has three parameters. The first must be a list with the panda dataframe with the spectra to be transformed (max of 2 datasets). The second parameter must be a list of strings with the names of the treatments and the third parameter is the index of the column where the spectrum starts (if there are columns with other type of data).

For example, to apply the SNV (Standard Normal Variate) treatment on a dataframe where the first two columns have other types of data (other than the spectrum), you can use the following command:
```python
spectras_transformed = make_transformations([data], ['snv'], 2)
```
To use all treatments, just use [`'all'`] as the second parameter.

The function `make_transfomations` will return a list of tuples with the treatments. The list size corresponds to the number of treatments applied (maximum 23). The size of each tuple corresponds to the number of inserted dataframes to be preprocessed + 1 (at last position has a name of preprocessing method) and the order of the datasets in each tuple is the same as that inserted.
There are 23 treatments available for use.

## Preprocessing methods available

- RAW (No treatment)
- SNV (Standard Normal Variate)
- MSC (Multiplicative Scatter Correction)
- AREA_NORM (Area Normalize)
- SG_11 (Savitzky-Golay filter with 11 smoothing points, 4 polynomial order and 1 order of the derivative)
- SG_25 (Savitzky-Golay filter with 25 smoothing points, 4 polynomial order and 1 order of the derivative)
- SG2_11 (Savitzky-Golay filter with 11 smoothing points, 4 polynomial order and 2 order of the derivative)
- SG2_25 (Savitzky-Golay filter with 25 smoothing points, 4 polynomial order and 2 order of the derivative)
- SNV_SG11 (SNV + SG_11)
- SNV_SG2_11 (SNV + SG2_11)
- SNV_SG25 (SNV + SG_25)
- SNV_SG2_25 (SNV + SG2_25)
- SG11_SNV (SG_11 + SNV)
- SG2_11_SNV (SG2_11 + SNV)
- SG2_25_SNV (SG2_25 + SNV)
- SG11_MSC (SG_11 + MSC)
- SG2_11_MSC (SG2_11 + MSC)
- SG25_MSC (SG_25 + MSC)
- SG2_25_MSC (SG2_25 + MSC)
- AREA_NORM_SG2_11 (AREA_NORM + SG2_11)
- AREA_NORM_SG2_25 (AREA_NORM + SG2_25)
- MSC_SG2_11 (MSC + SG2_11)
- MSC_SG2_25 (MSC + SG2_25)
- ALL (all preprocessing methods available)


### Applying pre-processing methods

## License
MIT © Diego Silva
