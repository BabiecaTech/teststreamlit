#pip install streamlit
#streamlit hello
import streamlit as st 
import pandas as pd 
import base64 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import MinMaxScaler 
import numpy as np 
import pickle as pkl 
import shap 
import streamlit.components.v1 as components
