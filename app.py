import pandas as pd
from fuzzywuzzy import process
import warnings
import numpy as np
import streamlit as st
warnings.filterwarnings('ignore')

final_reco=pd.read_pickle(r'C:\Users\nagar\Documents\python files\Python Projects\anime_pickel.pkl')


def reco(og, cnt):
    a, s, b = process.extractOne(og, final_reco.name)
    ret = list(final_reco[a].sort_values(ascending=False).index[1:cnt + 1].values)
    return ret


st.header('Top rated anime recomendations')

option=st.selectbox('Search the anime',final_reco.columns )

recomendation=reco(option,5)
st.write(recomendation)
