from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.ensemble import RandomForestRegressor

from algorithms.regression import PCR, RandomForest, PLSR
from algorithms.classification import PCA_LDA
from transformations import snv, sg, msc, plus_sg, area_norm
import pandas as pd
from utils import make_average
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('/home/dsilva/teste_pcr/foss_para_arff_calibracao.csv', sep=';', decimal=',')
df_val = pd.read_csv('/home/dsilva/teste_pcr/foss_para_arff_validacao.csv', sep=';', decimal=',')
df_all = pd.read_csv('/home/dsilva/teste_pcr/foss_all_samples.csv', sep=';', decimal=',')

rf_hyper = RandomForest(df, 100, 10, dataset_validation=df_val)
#rf_hyper.search_hyperparameters(verbose=2, n_processors=2, max_depth=[10, 50, 5], min_samples_leaf=[1, 2, 3], max_features=['sqrt', 'auto'])

#best df_all
#{'bootstrap': True, 'max_depth': 20, 'max_features': 'sqrt', 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
# r2 = 0.8166044727900362

# df
#{'bootstrap': True, 'max_depth': 10, 'max_features': 'sqrt', 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 400}