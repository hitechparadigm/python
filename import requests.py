import requests
import ipykernel
import pandas
import seaborn
import sklearn
import dotenv
import dask
import dask_expr
import sacred
import sqlalchemy
import psycopg2
import shap
import fancyimpute
import missingno
import tensorflow
import matplotlib
import plotly
import nbformat
import skimage
import cv2
import transformers
import yfinance
import l0bnb
import faraway
import pygam
import ISLP
import pybind11
def check_version(package_name):
    try:
        package = __import__(package_name)
        version = getattr(package, '__version__', None)
        if version:
            print(f"{package_name}: {version}")
        else:
            print(f"{package_name}: Version information not available.")
    except ImportError:
        print(f"{package_name}: Not installed.")
packages_to_check = [
    'numpy', 'requests', 'ipykernel', 'pandas', 'seaborn',
    'sklearn', 'dotenv', 'dask', 'dask_expr', 'sacred',
    'sqlalchemy', 'psycopg2', 'shap', 'fancyimpute', 'missingno',
    'tensorflow', 'matplotlib', 'plotly', 'nbformat', 'skimage',
    'cv2', 'transformers', 'yfinance', 'l0bnb', 'faraway', 'pygam',
    'ISLP', 'pybind11'
]
for package in packages_to_check:
    check_version(package)