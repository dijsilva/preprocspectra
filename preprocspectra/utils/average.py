import pandas as pd
import numpy as np

def make_average(dataset, number_of_repetions, start_spectra):

    if not isinstance(dataset, pd.DataFrame):
        raise ValueError('The dataset should be a dataframe.')

    if type(number_of_repetions) not in [int]:
        raise ValueError('The number_of_repetions should be integer.')

    if type(start_spectra) not in [int]:
        raise ValueError('The start_spectra should be integer that references a column which spectra starts.')

    if number_of_repetions <= 0:
        raise ValueError('The number_of_repetions cannot be negative.')

    df = dataset.copy()
    
    n_samples = df.shape[0]

    #X_average = pd.DataFrame()
    X_average = pd.DataFrame(np.zeros((int(n_samples / number_of_repetions), df.shape[1])))

    new_positions  = list(range(0, n_samples, number_of_repetions))
    for pos, index in enumerate(new_positions):
        X_average.iloc[pos, start_spectra :] = df.iloc[index : index + number_of_repetions, start_spectra :].mean(axis=0).values
        X_average.iloc[pos, : start_spectra] = df.iloc[index, : start_spectra].values

    X_average.index = new_positions
    X_average.columns = df.columns
    X_average.iloc[:,0] = X_average.iloc[:,0].astype(df.iloc[:,0].dtype)
    
    return X_average
        