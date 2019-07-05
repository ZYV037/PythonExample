import os
import time

#fileList = os.listdir("C:\迅雷下载\Mywife系列完整套图附真名(No.001—NO.560)\[mywife.cc]NO.001 to NO.560")


#for d in fileList:
#   print(d)

cur = 0
for rt,dirs,files in os.walk("C:\迅雷下载\pictureFolder"):
    for d in dirs:
        #curDir = rt+'\'
        #curDir += d
        #print(curDir)
        curDir = os.path.join(rt,d)
        print(curDir)
        for curRoot, curDirs, curFiles in os.walk(curDir):
            cur += 1
            if cur < 238:
                continue
            for curFile in curFiles:
                absCurFile = os.path.join(curRoot,curFile)
                
                strCmd = "C:\Program Files (x86)\ACD Systems\ACDSee\GFMF\ACDSeeGFMF.exe "
                strCmd += absCurFile
                print(d)
                os.popen(absCurFile)
                time.sleep(3)
                break
    
