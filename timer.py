import time

secs= input("Enter the time in seconds : ")

def countdowntimer(secs):
    while secs >0:

        min = int(secs/60)
        secs = int(secs%60)

        timer = f'{min}:{secs}'
        print(timer,end = "\r")
        time.sleep(1)
        secs -=1
   
    print("Time Up")

countdowntimer(int(secs))
    