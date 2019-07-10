import os
import re
import datetime 
import string 
import shutil

def getDateFromYearAndDayofyear(year, dayofyear):
	#print(year)
	#print(dayofyear)
	dt = datetime.datetime( int(year), 1, 1)
	dt = dt + datetime.timedelta(days=int(dayofyear)-1)
	#print(dt)
	return dt

# YQ2.YQ002.2019.075.E.sac =>YQ2.E.20190316.sac
def sacfile_rename(folder):
	f = open("log.txt",'ab')
	for root, dirs, files in os.walk(folder):
		for file in files:
			matchObj = re.match(r'^([^.]+).([^.]+).([0-9]+).([0-9]+).([EeNnZz]).(sac)$', file)
			
			if matchObj == None:
				continue
				
			#print(matchObj.groups())
			dt = getDateFromYearAndDayofyear( matchObj.group(3), matchObj.group(4) )
			newFileName = matchObj.group(1)+ '.' + matchObj.group(5) + '.' + dt.strftime("%Y%m%d")+'.'+ matchObj.group(6)
			#print(newFileName)
			os.rename( os.path.join(root,file), os.path.join(root,newFileName))
			print( os.path.join(root,file), " => ", os.path.join(root,newFileName) )
			f.write( (os.path.join(root,file) + " => "+ os.path.join(root,newFileName) + "\n").encode() )
	f.close()
	
#move file to F:\阳泉背景噪声\阳泉背景噪声微震数据_SAC (copy) order by date
def movefile_by_date(folder, dstFolder):
	f = open("log.txt",'ab')
	for root, dirs, files in os.walk(folder):
		for file in files:
			matchObj = re.match(r'^([^.]+).([EeNnZz]).([0-9]{8}).(sac)$', file)
			
			if matchObj == None:
				continue
			
			savePath = dstFolder + "\\" + matchObj.group(3)
			
			print(os.path.join(root,file))
			
			if not os.path.exists(savePath):
				os.makedirs(savePath) 
			
			if os.path.exists(savePath + "\\" + file):
				print(savePath + "\\" + file)
				continue
				
			shutil.copyfile(os.path.join(root,file), savePath + "\\" + file )
			print(os.path.join(root,file), "  copyto  " + savePath + "\\" + file )
			f.write( (os.path.join(root,file) + "  copyto  " + savePath + "\\" + file + "\n").encode() )
	f.close()

def rename_by_flodername(folder):
	f = open("log.txt",'ab')
	for root, dirs, files in os.walk(folder):
		for file in files:
			matchObj = re.match(r'^([^.]+).([EeNnZz]).([0-9]{8}).(sac)$', file)
			
			if matchObj == None:
				continue
			
			newFileName = root.split("\\")[-1] + '.' + matchObj.group(2) + '.' + matchObj.group(3) +'.'+ matchObj.group(4)
			os.rename( os.path.join(root,file), os.path.join(root,newFileName))
			print( os.path.join(root,file), " => ", os.path.join(root,newFileName) )
			f.write( (os.path.join(root,file) + " => "+ os.path.join(root,newFileName) + "\n").encode() )
	f.close()
	
#movefile_by_date("C:\\Users\\Aaron\\Desktop\\New folder", "C:\\Users\\Aaron\\Desktop\\阳泉背景噪声微震数据_SAC (copy)")
#rename_by_flodername("F:\\阳泉背景噪声\\yangquan_merge_r")
movefile_by_date("F:\\阳泉背景噪声\\yangquan_merge_r", "F:\\阳泉背景噪声\\阳泉背景噪声微震数据_SAC (copy)\\")