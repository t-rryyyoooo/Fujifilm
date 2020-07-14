import sys
import datetime

def A1(end=None):
    times = []
    time = datetime.datetime.strptime("05:55", "%H:%M")

    while time.hour < 23:
        times.append(time)
        time = time + datetime.timedelta(minutes=5)
    
    if end == 7:
        for i in range(len(times)):
            if str(times[i].minute)[-1] == 0:
                del times[i]

    elif end == 13:
        for i in range(len(times)):
            if str(times[i].minute)[-1] == 5:
                del times[i]


    return times

def A7(end):
    times = []
    if end == 1:
        time = datetime.datetime.strptime("06:06", "%H:%M")
        while time.hour < 23:
            times.append(time)
            time = time + datetime.timedelta(minutes=10)
    
    elif end == 13:
        time = datetime.datetime.strptime("06:10", "%H:%M")
        times.append(time)

    return times

def A13(end=None):
    times = []
    time = datetime.datetime.strptime("05:52", "%H:%M")
    while time.hour < 23:
        times.append(time)
        time = time + datetime.timedelta(minutes=10)

    if end == 1:
        times = times[:len(times) - 1]

    elif end == 7:
        times = times[len(times) - 1]

    return times

def time_A7(direction):
    if direction == "U":
        times = fromA2toA7(7, "U")


def fromA2toA7(station, direction):
    if direction == "U":
        move = [3, 5, 2, 3, 4, 3]
        times = A1
        for i in range(len(times)):
            times[i] = times[i] + datetime.timedelta(minutes=sum(move[:station - 1]))

        return times

    elif direction == "D":
        move = [3, 5, 2, 3, 4, 3, 4, 2, 2, 3, 6, 2]
        times_A7 = A7(end=1)
        for i in range(len(times_A7)):
            times_A7[i] = times_A7[i] + datetime.timedelta(minutes=sum(move[station - 1 : 6]))
        
        times_A13 = A13(end=1)
        for i in range(len(times_A13)):
            times_A13[i] = times_A13[i] + datetime.timedelta(minutes=sum(move[station - 1 : 12]))

        times = times_A7 + times_A13
        times = sorted(times)

        return times

def fromA7toA12(station, direction):
    if direction == "U":
        move = [3, 5, 2, 3, 4, 3, 4, 2, 2, 3, 6, 2]
        times = A1(end=13)
        for i in range(len(times)):
            times[i] = times[i] + datetime.timedelta(minutes=sum(move[ : station- 1]))

        time = datetime.datetime.strptime("06:10", "%H:%M") + datetime.timedelta(minutes=sum(move[ : station- 1]))
        times.append(time)
        times = sorted(times)

        return times

    elif direction == "D":
        move = [4, 2, 2, 3, 6, 2]
        times = A13()
        for i in range(len(times)):
            times[i] = times[i] + datetime.timedelta(minutes=sum(move[station - 7 : 6]))

        return times


def main():
    R, S, DIR, HH =input().split()
    if R == "A":
        if S == "A1":
            times = A1()

        elif S == "A13":
            times = A13()

        elif S == "A7":
            times = A7()

        elif 2 <= int(S[1:]) <= 6:
            times = fromA2toA6(int(S[1:]), DIR)

        elif 8 <= int(S[1:]) <= 12:
            times = fromA8toA12(int(S[1:]), DIR)



if __name__ == '__main__':
    main()

