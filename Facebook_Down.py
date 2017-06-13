import urllib.request
import re

def download(url):
    if (url.find("www.facebook.com")==-1):
        print("use facebook video links only")
    else:
        print("Fetching video in " + url + " ...")
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

        print("Page Length is : "+ str(len(mystr)))
        regex = r"sd_src:(\"(.*?)\")"
        matches = re.search(regex, mystr)
        print ("SD Version : " + matches.group(2)) 

        regex = r"hd_src:(\"(.*?)\")"
        matches = re.search(regex, mystr)          
        print ("HD Version : " + matches.group(2))        
                


download('https://www.facebook.com/mousalsalet.romdhan/videos/1776027656021934/')
