import datetime

fs_read=open("G:\\The Office US S01-S09 (2005-)\\The Office US S01 (360p re-webrip)\\Office6.srt")

fs_write=open("G:\\The Office US S01-S09 (2005-)\\The Office US S01 (360p re-webrip)\\Office6_out.srt","w")

def RepresentsInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def getTimeDiff(beforeTimeString,diff):
	beforeTime=datetime.datetime.strptime(beforeTimeString.strip(),"%H:%M:%S,%f")
	newTime=beforeTime-datetime.timedelta(seconds=diff)
	newTimeString=newTime.strftime("%H:%M:%S,%f")
	return(newTimeString[:-3])

readNextLine=False

for line in fs_read:
	print(line)
	if(readNextLine):
		times=line.split("-->")
		modified_from_time=getTimeDiff(times[0],22)
		modified_to_time=getTimeDiff(times[1],22)
		line=modified_from_time+" --> "+modified_to_time+"\n"
		readNextLine=False
	elif RepresentsInt(line.strip()):
		readNextLine=True
	fs_write.write(line)
	
fs_read.close()
fs_write.close();
	
	


