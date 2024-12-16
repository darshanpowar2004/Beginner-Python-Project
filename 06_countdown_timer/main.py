import time

time_stop = int(input("Enter the time in seconds : "))
# sec = 0
#
# while sec <= time_stop:
#     countdown = time_stop - sec
#     print(f"_____{countdown}_____")
#     sec += 1
#     time.sleep(1)
#
# print("_____TIME'S UP!_____")

for x in range(time_stop,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("_____TIME'S UP!_____")
