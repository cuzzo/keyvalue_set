#! /usr/bin/env python

import sys

def keyReplace(str, key, value):
	keyValue = str.split('=')
	if len(keyValue) != 2:
		return False
		
	tKey = keyValue[0].strip()
	if tKey != key:
		return False
	
	tValue = keyValue[1].strip()
	str = str.replace(tValue, value)
	return str

def main():
	if len(sys.argv) < 4:
		print 'Invalid required parameters.'
		sys.exit(1)

	key = sys.argv[1]
	value = sys.argv[2]
	filePath = sys.argv[3]
	
	try:
		f = open(filePath, 'r')
	except:
		print 'File does not exist--will not create and set key/value.'
		sys.exit(1)
	
	lines = f.readlines()
	f.close()
	
	replaced = False
	outLines = []
	for line in lines:
		line = line.replace('\n', '')
		rLine = keyReplace(line, key, value)
		if rLine:
			replaced = True
			outLines.append(rLine)
			continue
		
		outLines.append(line)
		
	if not replaced:
		outLines.append('%s=%s' % (key, value))
		
	f = open(filePath, 'w')
	for line in outLines:
		f.write('%s\n' % line)
	f.close()

	print key, value, filePath
	
if __name__ == '__main__':
	main()