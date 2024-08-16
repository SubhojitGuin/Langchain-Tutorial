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
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
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
import pytesseract
# import fitz
import io
import json
import requests

# ---- New Logging Process ----
def newloggingfunction(BOTName, rundate):
    global print
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()
    path = "log\\" + str(BOTName) + "_" + str(rundate) + "_log.txt"
    # path = os.path.join("log", str(BOTName), "_", str(rundate), "_log.txt")
    print(path)
    logger.addHandler(logging.FileHandler(path, "w"))
    print = logger.info
    return (logger.info)


# ------ Changeable Variables ------
ProdMdfVersion = 'NA'
DevMdfVersion = '02'


if __name__ == "__main__":
    print = newloggingfunction("BOT", str(datetime.now().strftime("%Y%m%d")))

    print("Hello Langchain")