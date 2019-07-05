import os
import re
import datetime 
import string 

def getDateFromYearAndDayofyear(year, dayofyear):
	#print(year)
	#print(dayofyear)
	dt = datetime.datetime( int(year), 1, 1)
	dt = dt + datetime.timedelta(days=int(dayofyear)-1)
	#print(dt)
	return dt


for root, dirs, files in os.walk("."):
	for file in files:
		matchObj = re.match(r'^([^.]+).([^.]+).([0-9]+).([0-9]+).([EeNnZz]+).(sac)$', file)
		
		if matchObj == None:
			continue
			
		#print(matchObj.groups())
		dt = getDateFromYearAndDayofyear( matchObj.group(3), matchObj.group(4) )
		newFileName = matchObj.group(1)+ '.' + matchObj.group(5) + '.' + dt.strftime("%Y%m%d")+'.'+ matchObj.group(6)
		#print(newFileName)
		os.rename( os.path.join(root,file), os.path.join(root,newFileName))
		print( os.path.join(root,file), " => ", os.path.join(root,newFileName) )
		