import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

def snv(dataset, spectra_start):
    
    """
    Apply the standard normal variate transformation.
        - the dataset should be a dataframe
        - spectra_start is the column that spectra start
    """

    if not isinstance(dataset, pd.DataFrame):
        raise ValueError('dataset should be a pandas dataframe')
    if type(spectra_start) not in [int]:
        raise ValueError('spectra_start should be a integer that reference a column')

    df = dataset.copy()

    avg = df.iloc[: ,spectra_start:].mean(axis=1)
    stds = df.iloc[: ,spectra_start:].std(axis=1)

    df.iloc[:, spectra_start:] = df.iloc[:, spectra_start:].subtract(avg, axis=0)
    df.iloc[:, spectra_start:] = df.iloc[:, spectra_start:].divide(stds, axis=0)
    
    return df


def msc(dataset, spectra_start):

    """
    Apply the Multiplicative Scatter Correction transformation.
        - the dataset should be a dataframe
        - spectra_start is the column that spectra start
    """

    if not isinstance(dataset, pd.DataFrame):
        raise ValueError('dataset should be a pandas dataframe')
    if type(spectra_start) not in [int]:
        raise ValueError('spectra_start should be a integer that reference a column')

    df = dataset.copy()

    spectra = df.iloc[:, spectra_start:]

    ref = np.mean(df.iloc[:, spectra_start:], axis=0)
    mean = df.iloc[:, spectra_start:].mean(axis=1)

    df.iloc[:, spectra_start:] = df.iloc[:, spectra_start:].subtract(mean, axis=0)

    for i in range(spectra.shape[0]):
        
        fit = np.polyfit(ref, df.iloc[i, spectra_start :].astype('float64'), deg=1, full=True)
        
        df.iloc[i, spectra_start:] = ((df.iloc[i, spectra_start :] - fit[0][1]) / fit[0][0]).values

    return df


def area_norm(dataset, spectra_start):
    
    """
    Apply the Area Normalize.
        - the dataset should be a dataframe
        - spectra_start is the column that spectra start
    """

    if not isinstance(dataset, pd.DataFrame):
        raise ValueError('dataset should be a pandas dataframe')
    if type(spectra_start) not in [int]:
        raise ValueError('spectra_start should be a integer that reference a column')

    df = dataset.copy()

    sum_of_rows = df.iloc[:, spectra_start:].sum(axis=1)

    df.iloc[:, spectra_start:] = df.iloc[:, spectra_start:].divide(sum_of_rows, axis=0)
    
    return df



def sg(dataset, differentiation, window_size, spectra_start, polynominal_order=4):
    
    """
    Apply the Savitzky-Golay filter.
        - the dataset should be a dataframe
        - differentiation is the derivative order
        - window_size is a window size (must be odd).
        - polynominal_order for equation
    """
    if not isinstance(dataset, pd.DataFrame):
        raise ValueError('dataset should be a pandas dataframe')
    if type(differentiation) not in [int]:
        raise ValueError('differentiation should be a integer')
    if type(window_size) not in [int]:
        raise ValueError('window_size should be a integer')
    if type(polynominal_order) not in [int]:
        raise ValueError('polynominal_order should be a integer')
    if type(spectra_start) not in [int]:
        raise ValueError('spectra_start should be a integer that reference a column')

    df = dataset.copy()

    sg_df = savgol_filter(df.iloc[:, spectra_start:], window_length=window_size, polyorder=polynominal_order, deriv=differentiation, axis=-1)

    sg_df = pd.DataFrame(sg_df)

    sg_df.columns = df.iloc[:, spectra_start:].columns
    sg_df.index = df.iloc[:, spectra_start:].index

    df.iloc[:, spectra_start:] = sg_df.iloc[:, spectra_start:]

    gap = window_size // 2
    
    columns_sg = list(sg_df.iloc[:,gap:-gap].columns)
    columns_dataset = list(df.iloc[:,spectra_start:].columns)

    columns_for_drop = list(set(columns_dataset) - set(columns_sg))

    df = df.drop(columns_for_drop, axis=1)

    return df

def plus_sg(dataset, sg_first, transformation, differentiation, window_size, spectra_start, polynominal_order=4):
    
    """
    Apply the Savitzky-Golay filter after apply SNV transformation.
        - the dataset should be a dataframe
        - sg_first should be a boolean value. True if sg should  be performed before the additional transformation
        - differentiation is the derivative order
        - window_size is a window size (must be odd).
        - polynominal_order for equation
    """

    if sg_first not in [True, False]:
        raise ValueError('sg_first should be a boolean value')
    if not isinstance(dataset, pd.DataFrame):
        raise ValueError('dataset should be a pandas dataframe')
    if type(differentiation) not in [int]:
        raise ValueError('differentiation should be a integer')
    if type(window_size) not in [int]:
        raise ValueError('window_size should be a integer')
    if type(polynominal_order) not in [int]:
        raise ValueError('polynominal_order should be a integer')
    if type(spectra_start) not in [int]:
        raise ValueError('spectra_start should be a integer that reference a column')
    
    df = dataset.copy()
    if sg_first == True:
        df_first = sg(df, differentiation, window_size, spectra_start, polynominal_order)
        df_transformed = transformation(df_first, spectra_start=spectra_start)
    else:
        df_first = transformation(df, spectra_start=spectra_start)
        df_transformed = sg(df_first, differentiation, window_size, spectra_start, polynominal_order)

    return df_transformed
