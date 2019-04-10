from ftplib import FTP, error_perm
import os
import glob
import patoolib

def ftpDownloader(stationId,startYear,endYear,url="ftp.pyclass.com",user="student@pyclass.com",passwd="student123"):
    ftp=FTP(url)        
    ftp.login(user,passwd)
    if not os.path.exists("C:\\in"):           
        os.makedirs("C:\\in")
    os.chdir("C:\\in")
    for year in range(startYear,endYear+1):
        fullpath='/Data/%s/%s-%s.gz' % (year,stationId,year)    
        filename=os.path.basename(fullpath)
        try:
            with open(filename,"wb") as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
            print("%s succesfully downloaded" % filename)
        except error_perm: 
            print("%s is not available" % filename)
            os.remove(filename)    
    ftp.close()
    
            
def extractFiles(indir="C:\\in",out="C:\\in\\Extracted"):
    os.chdir(indir)
    archives=glob.glob("*.gz")
    print (archives)
    if not os.path.exists(out):
       os.makedirs(out)
    files=os.listdir("Extracted")
    print(files)
    for archive in archives:
        if archive[:-3] not in files:
            patoolib.extract_archive(archive,outdir=out)
            

