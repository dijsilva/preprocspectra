from preprocspectra.transformations import snv, sg, msc, plus_sg, area_norm

import pandas as pd


def make_transformations(datasets, transformations, index_spectra_start):
    if not isinstance(datasets, list):
        raise ValueError('datasets should be a list of dataframes.')

    if not isinstance(transformations, list):
        raise ValueError('transformations should be a list of strings.')

    for dataset in datasets:
        if not isinstance(dataset, pd.DataFrame):
            raise ValueError('dataset should be a pandas dataframe.')

    ALL = ['RAW', 'SNV', 'MSC', 'AREA_NORM', 'SG_11', 'SG_25', 'SG2_11', 'SG2_25', 
           'SNV_SG11', 'SNV_SG2_11', 'SNV_SG25', 'SNV_SG2_25', 'SG11_SNV',
           'SG2_11_SNV', 'SG2_25_SNV', 'SG11_MSC', 'SG2_11_MSC', 'SG25_MSC',
           'SG2_25_MSC', 'AREA_NORM_SG2_11', 'AREA_NORM_SG2_25', 'MSC_SG2_11', 
           'MSC_SG2_25']
    
    transformations = [x.upper() for x in transformations]
    dataset_transformed = []

    if 'ALL' in transformations:
        transformations = ALL
    
    if 'RAW' in transformations:
        if len(datasets) == 2:
            dataset_transformed.append((datasets[0], datasets[1], 'RAW'))
        if len(datasets) == 1:
            dataset_transformed.append((datasets[0], 'RAW'))

    if 'SNV' in transformations:
        if len(datasets) == 2:
            df_snv = snv(datasets[0], spectra_start=index_spectra_start)
            df_val_snv = snv(datasets[1], spectra_start=index_spectra_start)
            dataset_transformed.append((df_snv, df_val_snv, 'SNV'))

        elif len(datasets) == 1:
            df_snv = snv(datasets[0], spectra_start=index_spectra_start)
            dataset_transformed.append((df_snv, 'SNV'))
    
    
    
    if 'MSC' in transformations:
        if len(datasets) == 2:
            df_msc = msc(datasets[0], spectra_start=index_spectra_start)
            df_val_msc = msc(datasets[1], spectra_start=index_spectra_start)
            dataset_transformed.append((df_msc, df_val_msc, 'MSC'))
        
        elif len(datasets) == 1:
            df_msc = msc(datasets[0], spectra_start=index_spectra_start)
            dataset_transformed.append((df_msc, 'MSC'))
    


    if 'AREA_NORM' in transformations:
        if len(datasets) == 2:
            df_areanorm = area_norm(datasets[0], spectra_start=index_spectra_start)
            df_val_areanorm = area_norm(datasets[1], spectra_start=index_spectra_start)
            dataset_transformed.append((df_areanorm, df_val_areanorm, 'AREA_NORM'))
        elif len(datasets) == 1:
            df_areanorm = area_norm(datasets[0], spectra_start=index_spectra_start)
            dataset_transformed.append((df_areanorm, 'AREA_NORM'))
    


    if 'SG_11' in transformations:
        if len(datasets) == 2:
            df_sg11 = sg(datasets[0], differentiation=1, window_size=11, spectra_start=index_spectra_start)
            df_val_sg11 = sg(datasets[1], differentiation=1, window_size=11, spectra_start=index_spectra_start)
            dataset_transformed.append((df_sg11, df_val_sg11, 'SG_11'))
        elif len(datasets) == 1:
            df_sg11 = sg(datasets[0], differentiation=1, window_size=11, spectra_start=index_spectra_start)
            dataset_transformed.append((df_sg11, 'SG_11'))
    

    
    if 'SG_25' in transformations:
        if len(datasets) == 2:
            df_sg25 = sg(datasets[0], differentiation=1, window_size=25, spectra_start=index_spectra_start)
            df_val_sg25 = sg(datasets[1], differentiation=1, window_size=25, spectra_start=index_spectra_start)
            dataset_transformed.append((df_sg25, df_val_sg25, 'SG_25'))
        elif len(datasets) == 1:
            df_sg25 = sg(datasets[0], differentiation=1, window_size=25, spectra_start=index_spectra_start)
            dataset_transformed.append((df_sg25, 'SG_25'))
    


    if 'SG2_11' in transformations:
        if len(datasets) == 2:
            df_sg2_11 = sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start)
            df_val_sg2_11 = sg(datasets[1], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start)
            dataset_transformed.append((df_sg2_11, df_val_sg2_11, 'SG2_11'))
        if len(datasets) == 1:
            df_sg2_11 = sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start)
            dataset_transformed.append((df_sg2_11, 'SG2_11'))
    


    if 'SG2_25' in transformations:
        if len(datasets) == 2:
            df_sg2_25 = sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start)
            df_val_sg2_25 = sg(datasets[1], differentiation=2, window_size=25, spectra_start=index_spectra_start)
            dataset_transformed.append((df_sg2_25, df_val_sg2_25, 'SG2_25'))
        if len(datasets) == 1:
            df_sg2_25 = sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start)
            dataset_transformed.append((df_sg2_25, 'SG2_25'))
    


    if 'SNV_SG11' in transformations:
        if len(datasets) == 2:
            df_snv_sg11 = plus_sg(datasets[0], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            df_val_snv_sg11 = plus_sg(datasets[1], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            dataset_transformed.append((df_snv_sg11, df_val_snv_sg11, 'SNV_SG11'))
        if len(datasets) == 1:
            df_snv_sg11 = plus_sg(datasets[0], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            dataset_transformed.append((df_snv_sg11, 'SNV_SG11'))
    


    if 'SNV_SG2_11' in transformations:
        if len(datasets) == 2:
            df_snv_sg2_11 = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            df_val_snv_sg2_11 = plus_sg(datasets[1], differentiation=2, window_size=11, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            dataset_transformed.append((df_snv_sg2_11, df_val_snv_sg2_11, 'SNV_SG2_11'))
        if len(datasets) == 1:
            df_snv_sg2_11 = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            dataset_transformed.append((df_snv_sg2_11, 'SNV_SG2_11'))
    


    if 'SNV_SG25' in transformations:
        if len(datasets) == 2:
            df_snv_sg25 = plus_sg(datasets[0], differentiation=1, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            df_val_snv_sg25 = plus_sg(datasets[1], differentiation=1, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            dataset_transformed.append((df_snv_sg25, df_val_snv_sg25, 'SNV_SG25'))
        if len(datasets) == 1:
            df_snv_sg25 = plus_sg(datasets[0], differentiation=1, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            dataset_transformed.append((df_snv_sg25, 'SNV_SG25'))
    


    if 'SNV_SG2_25' in transformations:
        if len(datasets) == 2:
            df_snv_sg2_25 = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            df_val_snv_sg2_25 = plus_sg(datasets[1], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            dataset_transformed.append((df_snv_sg2_25, df_val_snv_sg2_25, 'SNV_SG2_25'))
        if len(datasets) == 1:
            df_snv_sg2_25 = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=False)
            dataset_transformed.append((df_snv_sg2_25, 'SNV_SG2_25'))
    


    if 'SG11_SNV' in transformations:
        if len(datasets) == 2:        
            df_sg11_snv = plus_sg(datasets[0], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            df_val_sg11_snv = plus_sg(datasets[1], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            dataset_transformed.append((df_sg11_snv, df_val_sg11_snv, 'SG11_SNV'))
        if len(datasets) == 1:
            df_sg11_snv = plus_sg(datasets[0], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            dataset_transformed.append((df_sg11_snv, 'SG11_SNV'))
    


    if 'SG2_11_SNV' in transformations:
        if len(datasets) == 2:        
            df_sg2_11_snv = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            df_val_sg2_11_snv = plus_sg(datasets[1], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            dataset_transformed.append((df_sg2_11_snv, df_val_sg2_11_snv, 'SG2_11_SNV'))
        if len(datasets) == 1:
            df_sg2_11_snv = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            dataset_transformed.append((df_sg2_11_snv, 'SG2_11_SNV'))
    


    if 'SG2_25_SNV' in transformations:
        if len(datasets) == 2:
            df_sg2_25_snv = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            df_val_sg2_25_snv = plus_sg(datasets[1], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            dataset_transformed.append((df_sg2_25_snv, df_val_sg2_25_snv, 'SG2_25_SNV'))
        if len(datasets) == 1:
            df_sg2_25_snv = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=snv, sg_first=True)
            dataset_transformed.append((df_sg2_25_snv, 'SG2_25_SNV'))
    


    if 'SG11_MSC' in transformations:
        if len(datasets) == 2:
            df_sg11_msc = plus_sg(datasets[0], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            df_val_sg11_msc = plus_sg(datasets[1], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            dataset_transformed.append((df_sg11_msc, df_val_sg11_msc, 'SG11_MSC'))
        if len(datasets) == 1:
            df_sg11_msc = plus_sg(datasets[0], differentiation=1, window_size=11, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            dataset_transformed.append((df_sg11_msc, 'SG11_MSC'))




    if 'SG2_11_MSC' in transformations:
        if len(datasets) == 2:
            df_sg2_11_msc = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            df_val_sg2_11_msc = plus_sg(datasets[1], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            dataset_transformed.append((df_sg2_11_msc, df_val_sg2_11_msc, 'SG2_11_MSC'))
        if len(datasets) == 1:
            df_sg2_11_msc = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            dataset_transformed.append((df_sg2_11_msc, 'SG2_11_MSC'))




    if 'SG25_MSC' in transformations:
        if len(datasets) == 2:
            df_sg25_msc = plus_sg(datasets[0], differentiation=1, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            df_val_sg25_msc = plus_sg(datasets[1], differentiation=1, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            dataset_transformed.append((df_sg25_msc, df_val_sg25_msc, 'SG25_MSC'))
        if len(datasets) == 1:
            df_sg25_msc = plus_sg(datasets[0], differentiation=1, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            dataset_transformed.append((df_sg25_msc, 'SG25_MSC'))
    


    if 'SG2_25_MSC' in transformations:
        if len(datasets) == 2:
            df_sg2_25_msc = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            df_val_sg2_25_msc = plus_sg(datasets[1], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            dataset_transformed.append((df_sg2_25_msc, df_val_sg2_25_msc, 'SG2_25_MSC'))
        if len(datasets) == 1:
            df_val_sg2_25_msc = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=True)
            dataset_transformed.append((df_val_sg2_25_msc, 'SG2_25_MSC'))
    


    if 'AREA_NORM_SG2_11' in transformations:
        if len(datasets) == 2:
            df_normalize_sg2_11 = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=area_norm, sg_first=False)
            df_val_normalize_sg2_11 = plus_sg(datasets[1], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=area_norm, sg_first=False)
            dataset_transformed.append((df_normalize_sg2_11, df_val_normalize_sg2_11, 'AREA_NORM_SG2_11'))
        if len(datasets) == 1:
            df_normalize_sg2_11 = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=area_norm, sg_first=False)
            dataset_transformed.append((df_normalize_sg2_11, 'AREA_NORM_SG2_11'))
    


    if 'AREA_NORM_SG2_25' in transformations:
        if len(datasets) == 2:
            df_normalize_sg2_25 = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=area_norm, sg_first=False)
            df_val_normalize_sg2_25 = plus_sg(datasets[1], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=area_norm, sg_first=False)
            dataset_transformed.append((df_normalize_sg2_25, df_val_normalize_sg2_25, 'AREA_NORM_SG2_25'))
        if len(datasets) == 1:
            df_normalize_sg2_25 = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=area_norm, sg_first=False)
            dataset_transformed.append((df_normalize_sg2_25, 'AREA_NORM_SG2_25'))
    


    if 'MSC_SG2_11' in transformations:
        if len(datasets) == 2:
            df_msc_sg2_11 = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=msc, sg_first=False)
            df_val_msc_sg2_11 = plus_sg(datasets[1], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=msc, sg_first=False)
            dataset_transformed.append((df_msc_sg2_11, df_val_msc_sg2_11, 'MSC_SG2_11'))
        if len(datasets) == 1:
            df_msc_sg2_11 = plus_sg(datasets[0], differentiation=2, window_size=11, polynominal_order=2, spectra_start=index_spectra_start, transformation=msc, sg_first=False)
            dataset_transformed.append((df_msc_sg2_11, 'MSC_SG2_11'))

    

    if 'MSC_SG2_25' in transformations:
        if len(datasets) == 2:
            df_msc_sg2_25 = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=False)
            df_val_msc_sg2_25 = plus_sg(datasets[1], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=False)
            dataset_transformed.append((df_msc_sg2_25, df_val_msc_sg2_25, 'MSC_SG2_25'))
        if len(datasets) == 1:
            df_msc_sg2_25 = plus_sg(datasets[0], differentiation=2, window_size=25, spectra_start=index_spectra_start, transformation=msc, sg_first=False)
            dataset_transformed.append((df_msc_sg2_25, 'MSC_SG2_25'))
    

    return dataset_transformed
