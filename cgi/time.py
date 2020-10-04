#!/usr/bin/python3
import os
from datetime import datetime

print('Content-Type: text/html')
print()
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Time</title>')
print('</head>')
print('<body>')
print('<p>Date and time: ', datetime.now().strftime('%c'), '</p>', sep='')
print('<p>IP address: ', os.environ['REMOTE_ADDR'], '</p>', sep='')
print('<p>User-Agent: ', os.environ['HTTP_USER_AGENT'], '</p>', sep='')
print('</body>')
print('</html>')