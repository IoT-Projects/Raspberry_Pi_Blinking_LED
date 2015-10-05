import RPi.GPIO as GPIO            	## Import GPIO Library
import time                        	## Import 'time' library (for 'sleep')


pin = 7


GPIO.setmode(GPIO.BOARD)            ## Use BOARD pin numbering


ourRange = range(1,10)

for count in ourRange:
    GPIO.setup(pin, GPIO.OUT)   	## set output
    GPIO.output(pin, GPIO.HIGH) 	## set HIGH (LED ON)
    time.sleep(1)	    			## wait
    GPIO.output(pin, GPIO.LOW)  	## set LOW (LED OFF)


GPIO.cleanup()
