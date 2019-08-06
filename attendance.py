#!/usr/bin/python
import os
import re
import sys
import time
from datetime import datetime, timedelta

def asciiNode():
  print ("""
            .                .                    
            :"-.          .-";                    
            |:`.`.__..__.'.';|                    
            || :-"      "-; ||                    
            :;              :;                    
            /  .==.    .==.  \                    
           :      _.--._      ;                   
           ; .--.' `--' `.--. :                   
          :   __;`      ':__   ;                  
          ;  '  '-._:;_.-'  '  :                  
          '.       `--'       .'                  
           ."-._          _.-".                   
         .'     ""------""     `.                 
        /`-                    -'\                
       /`-                      -'\               
      :`-   .'              `.   -';              
      ;    /                  \    :       I'm searching your first login time.       
     :    :                    ;    ;      Please wait. Catpaws :)
     ;    ;                    :    :             
     ':_:.'                    '.;_;'             
        :_                      _;                
        ; "-._                -" :`-.     _.._    
        :_          ()          _;   "--::__. `.  
         \"-                  -"/`._           :  
        .-"-.                 -"-.  ""--..____.'  
       /         .__  __.         \               
      : / ,       / "" \       . \ ;           
       "-:___..--"      "--..___;-" """)

def getLastLoginTime():
  return os.popen('log show --style syslog --predicate \'process == "loginwindow"\' --debug --info --last 11h | grep "LUIAuthenticationServiceProvider deactivateWithContext:]_block_invoke" | head -1').read()

def onHandleTime():
  timeString = getLastLoginTime()
  timeRegex = "\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])([0-9]|[0-5][0-9])"
  time = re.search(timeRegex, timeString)
  return time.group(0)

def addWorkingHours(time):
  return datetime.strptime(time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=9)

def showUI(leaveTimeObj):
  print ("-------------------------------")
  print ("--- Your Leave Time After: ---")
  print leaveTimeObj.strftime('%Y-%m-%d %H:%M:%S')
  while True:
    sys.stdout.write("\rRemaining work time : %s" % str(leaveTimeObj - datetime.now())[:-7])
    sys.stdout.flush()
    time.sleep(.5)
  
def main() :
  asciiNode()
  onWorkTimeStr = onHandleTime()
  leaveTimeObj = addWorkingHours(onWorkTimeStr)
  showUI(leaveTimeObj)

if __name__ == '__main__':
  main()