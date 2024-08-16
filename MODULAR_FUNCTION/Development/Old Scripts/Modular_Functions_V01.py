# ---- Author : Subhojit Guin ----
# ---- Date : 16/08/2024 (dd/mm/yyyy) ----

# -- Import Required Packages --
import sys
import traceback
import logging
import pandas as pd
from logging import exception
import time
import os
import shutil
from time import strptime
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import socket
import urllib3
import smtplib
from zipfile import ZipFile
from typing import Optional
import warnings
import string
import random
import calendar
import zipfile
import glob
from os.path import basename
import patoolib
from pathlib import Path
import concurrent.futures
import pause
from configparser import ConfigParser
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
import numpy
import cv2
import pytesseract
import fitz
import io
import json
import requests

# ---- New Logging Process ----
def newloggingfunction(vendorsmallname, rundate):
    global print
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()
    logger.addHandler(logging.FileHandler(vendorsmallname + str(rundate) + "_log.txt", "w"))
    print = logger.info
    return (logger.info)


# ------ Changeable Variables ------
ProdMdfVersion = 'NA'
DevMdfVersion = '01'