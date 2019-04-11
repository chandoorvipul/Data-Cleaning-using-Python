from ftplib import FTP, error_perm
import os
import glob
import pandas
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
            

def addField(indir="C:\\in\\Extracted"):
    os.chdir(indir)
    fileList=glob.glob("*")
    print ("fileList" ,fileList)
    for filename in fileList:
        df=pandas.read_csv(filename,sep='\s+',header=None)
        df["Station"]=[filename.rsplit("-",1)[0]]*df.shape[0]
        df.to_csv(filename+".csv",index=None,header=None)
        os.remove(filename)
        
def concatenate(indir="C:\\in\\Extracted",outfile="C:\\out\\Concatenated.csv"):
    os.chdir(indir)
    fileList=glob.glob("*.csv")
    dfList=[]
    colnames=["Year","Month","Day","Hour","Temp","DewTemp","Pressure","WindDir","WindSpeed","Sky","Precip1","Precip6","ID"]
    for filename in fileList:
        print (filename)
        df=pandas.read_csv(filename,header=None)
        dfList.append(df)
    concatDf=pandas.concat(dfList,axis=0)    
    concatDf.columns=colnames
    concatDf.head()
    concatDf.to_csv(outfile,index=None)
    
def merge(left="C:\\out\\Concatenated.csv",right="C:\\CS\\station-info.txt",output="C:\\out\\Concatenated-Merged.csv"):
    leftDf=pandas.read_csv(left)   
    rightDf=pandas.read_fwf(right,converters={"USAF":str,"WBAN":str})
    rightDf["USAF_WBAN"]=rightDf["USAF"]+"-"+rightDf["WBAN"]
    mergedDf=pandas.merge(leftDf,rightDf.ix[:,["USAF_WBAN","STATION NAME","LAT","LON"]],left_on="ID",right_on="USAF_WBAN")
    mergedDf.to_csv(output)
