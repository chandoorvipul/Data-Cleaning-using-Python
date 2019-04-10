# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:26:50 2019

@author: S530459
"""


from ftplib import FTP
import os

def ftpDownloader(stationId,startYear,endYear,url="ftp.pyclass.com",user = "student@pyclass.com",passwd="student123"):
    ftp=FTP(url)
    ftp.login(user,passwd)
    if not os.path.exists("C:\\Users\\S530459\\Desktop\\data cleaning"):
        os.makedirs("C:\\Users\\S530459\\Desktop\\data cleaning\\data")
    os.chdir("C:\\Users\\S530459\\Desktop\\data cleaning")
    for year in range(startYear, endYear+1):
        fullpath = '/Data/%s/%s-%s.gz' %(year,stationId,year)
        filename= os.path.basename(fullpath)
        try:
            with open(filename, 'wb') as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
            print("% sucessfully downloaded" % filename)
        except error_perm:
            print("%s is not available" % filename)
            os.remove(filename)
    ftp.close()