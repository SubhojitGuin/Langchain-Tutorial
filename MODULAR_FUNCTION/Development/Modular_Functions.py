# ---- Author : Subhojit Guin ----
# ---- Date : 16/08/2024 (dd/mm/yyyy) ----

# ---- Import Required Packages ----
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
import io
import json
import requests
from dotenv import load_dotenv

load_dotenv()

LogFilePath = "log\\"

# ---- New Logging Process ----
def newloggingfunction(BOTName, rundate):
    
    global print
    global LogFilePath

    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger()
    LogFilePath = "log\\" + str(BOTName) + "_" + str(rundate) + "_log.txt"
    logger.addHandler(logging.FileHandler(LogFilePath, "w"))
    print = logger.info
    return (logger.info)

# ++++++++++++++++ Changeable variable names +++++++++++++++++

# ------ Version Number ------
ProdMdfVersion = 'NA'
DevMdfVersion = '02'


# ++++++++++++++++++++++ Main checking +++++++++++++++++++++++
if __name__ == "__main__":
    print = newloggingfunction("BOT", str(datetime.now().strftime("%Y%m%d")))
    
    print(f"Log File Path -- '" + str(LogFilePath) + "'")

    print("Hello Langchain")