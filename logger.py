from datetime import datetime
import sys

file = sys.argv[1]

with open(file, 'a') as logfile:
  while True:
    activity = input().split(maxsplit=1)
    
    if not activity:
      continue
    
    if activity[0] == 'STOPPED':
      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
      log = f'{timestamp} [STOPPED] Logging Stopped.\n'
      logfile.write(log)
      break
    
    if len(activity) < 2:
      continue
    
    action = activity[0]
    message = activity[1]
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    log = f'{timestamp} [{action}] {message}\n'
    logfile.write(log)
    logfile.flush()
    