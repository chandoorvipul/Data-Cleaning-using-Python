# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:40:41 2019

@author: S530459
"""

from ftplib import FTP
import os

def ftpDownloader(filename,host="ftp.pyclass.com",user = "student@pyclass.com",passwd="student123"):
    ftp=FTP(host)
    ftp.login(user,passwd)
    ftp.cwd("Data")
    os.chdir("C:\\Users\\S530459\\Desktop\\data cleaning")
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR %s' % filename, file.write)
        