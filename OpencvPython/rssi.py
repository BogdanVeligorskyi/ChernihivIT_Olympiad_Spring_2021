import csv

f = open("output.txt", "w")

inputFile = 'resources/data-2-6.csv'

i = 0
count70 = 0
countTr = 0
cntArr = 0
room = ""
cP = ""
flagPoint = 0
tRoom = 0
B1, B2, B3, B4, B5, B6 = -100, -100, -100, -100, -100, -100

with open(inputFile, newline='') as File:
    reader = csv.reader(File)


    for row in reader:
        if i > 0:
            point = int(row[3])
            issr = float(row[4])
            if point == 1:
                B1 = issr
            elif point == 2:
                B2 = issr
            elif point == 3:
                B3 = issr
            elif point == 4:
                B4 = issr
            elif point == 5:
                B5 = issr
            else:
                B6 = issr

            if count70 == 10:
                maxP = max([B1, B2, B3, B4, B5, B6])
                if maxP > -60:
                    if maxP == B1:
                        if cP != 'B1':
                            cP = 'B1'
                            flagPoint = 1
                        else:
                            flagPoint = 0
                    elif maxP == B2:
                        if cP != 'B2':
                            cP = 'B2'
                            flagPoint = 1
                        else:
                            flagPoint = 0
                    elif maxP == B3:
                        if cP != 'B3':
                            cP = 'B3'
                            flagPoint = 1
                        else:
                            flagPoint = 0
                    elif maxP == B4:
                        if cP != 'B4':
                            cP = 'B4'
                            flagPoint = 1
                        else:
                            flagPoint = 0
                    elif maxP == B5:
                        if cP != 'B5':
                            cP = 'B5'
                            flagPoint = 1
                        else:
                            flagPoint = 0
                    elif maxP == B6:
                        if cP != 'B6':
                            cP = 'B6'
                            flagPoint = 1
                        else:
                            flagPoint = 0
                if B1 > -60:
                    if room == "C3":
                        tRoom += 1
                    else:
                        room = "C3"
                        tRoom = 1
                elif B2 > -60:
                    if room == "C3":
                        tRoom += 1
                    else:
                        room = "C3"
                        tRoom = 1
                elif B3 > -60:
                    if room == "C1":
                        tRoom += 1
                    else:
                        room = "C1"
                        tRoom = 1
                elif B4 > -60:
                    if room == "C1":
                        tRoom += 1
                    else:
                        room = "C1"
                        tRoom = 1
                elif B5 > -60:
                    if room == "C2":
                        tRoom += 1
                    else:
                        room = "C2"
                        tRoom = 1
                elif B6 > -60:
                    if room == "C2":
                        tRoom += 1
                    else:
                        room = "C2"
                        tRoom = 1

                elif B1 > B6 and B2 > B3 and B2 > B4 and B2 > B6:
                    if room == "C3":
                        tRoom += 1
                    else:
                        room = "C3"
                        tRoom = 1
                elif B6 > B2 and B5 > B4 and B5 > B3:
                    if room == "C2":
                        tRoom += 1
                    else:
                        room = "C2"
                        tRoom = 1
                elif B3 > B2 and B4 > B2 and B4 > B5 and B3 > B5:
                    if room == "C1":
                        tRoom += 1
                    else:
                        room = "C1"
                        tRoom = 1
                if tRoom == 7 and flagPoint == 0:
                    print(room)
                    f.write(room + '\n')
                if flagPoint == 1:
                    print(room, cP)
                    rcp = room + " " + cP
                    f.write(rcp + "\n")
                count70 = 0

        i += 1
        count70 += 1
    f.close()