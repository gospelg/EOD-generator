def main():
    usrinput = data_grab()
    router = sheet1()
    contact = sheet2()
    notes = notesheet()
    maths = mathisfun(usrinput)
    generate(usrinput, maths)
    sheets(router, contact, notes)
    
    
    

def data_grab():
  
    launch = input('input launch point \n')
    startmiles = input('input your starting mileage \n')
    starttime = input('input your starting time \n')
    destination = input('input your destinantion point \n')
    ontime = input('input your arrival time \n')
    onmiles = input('input your mileage upon arrival \n')
    offtime = input('input your departure time \n')
    homemiles = input('input your home miles \n')
    hometime = input('input your home time \n') 
    workperformed = input('Decribe the work performed onsite \n')

    datagroup = (launch, startmiles, starttime, destination, ontime, onmiles, offtime, homemiles, hometime, workperformed)
    return datagroup

def sheet1():
    print ("Do you have anything to add to the routersheet?")
    answer = input("y/n? ").lower()
    
    if answer == "y": 
    
        info = input("Enter your routersheet info \n")
        rsheet = ("ADD TO ROUTERSHEET: \n" + info)
        return rsheet

    else:

        rsheet = ""
        return rsheet


#this next function looks querys the user for any info that needs to be added to the contacts sheet
def sheet2():
    print ("Do you have anything to add to the contacts sheet? ")
    answer = input("y/n? ").lower()
    
    if answer == "y":
      
        info = input("Enter your contactsheet info \n")
        csheet = ("ADD TO CONTACTSHEET: \n" + info)
        return csheet
    
    else: 
        
        csheet = ""
        return csheet

   
def notesheet():
    print ("Are there any additional notes you would like to add? ")
    answer = input("y/n? ").lower()
    
    if answer == "y":
        
        info = input("Add your notes now \n")
        notes = ("Additional notes: \n" + info)
        return notes
    
    else: 
        
        csheet = ""
        return csheet

def time_calc(hours1, minutes1, hours2, minutes2):
    total_h = hours2 - hours1
    total_m = minutes2 - minutes1
    
    if total_m < 0:
        total_h -= 1
        total_m = 60 - abs(total_m)

    trip_time = str(total_h) + " hours " +  str(total_m) + " minutes"
    return trip_time
#this function does most of the calculating, including distances and calls the time_calc function to find elapsed times.
def mathisfun(data):

    onmiles = data[5]
    startmiles = data[1]
    homemiles = data[7]
    
    starttime = data[2]
    ontime = data[4]
    offtime = data[6]
    hometime = data[8] 
    
    trip_a = int(onmiles) - int(startmiles)
    trip_b = int(homemiles) - int(onmiles)
    totalmiles = int(trip_a) + int(trip_b)
  
#this takes user string inputs and converts them to formatting freindly to the time_calc



    th1 = int(starttime[0:2])
    tm1 = int(starttime[3:5])
    th2 = int(ontime[0:2])
    tm2 = int(ontime[3:5])

    th3 = int(offtime[0:2])
    tm3 = int(offtime[3:5])
    th4 = int(hometime[0:2])
    tm4 = int(hometime[3:5])
    

    
    point_AB = time_calc(th1, tm1, th2, tm2)
    point_BC = time_calc(th3, tm3, th4, tm4)
    time_on = time_calc(th2, tm2, th3, tm3)    
    allthedata = (trip_a, trip_b, time_on, totalmiles, point_AB, point_BC, time_on)
    return allthedata

def generate(tuple1, tuple2):
  

    with open("eod.txt", "w") as text_file:
        print("Starting miles: {0} \nEnding miles: {1} \nTOTAL: {2} \n".format(tuple1[1], tuple1[7], tuple2[3]), file=text_file)
        print("From {0} to {1}: {2} - {3} ({4} miles) {5} - {6} ({7}) <-travel".format(tuple1[0], tuple1[3], tuple1[1], tuple1[5], tuple2[0], tuple1[2], tuple1[4], tuple2[4]), file=text_file)
        print("From {0} to {1} ({2}) <- onsite. \n\n{3}\n".format(tuple1[4], tuple1[6], tuple2[6], tuple1[9]), file=text_file)
        print("From {0} to {1}: {2} - {3} ({4} miles) {5} - {6} ({7}) <- travel.".format(tuple1[3], tuple1[0], tuple1[5], tuple1[7], tuple2[1], tuple1[6], tuple1[8], tuple2[5]), file=text_file)    

def sheets(sheet1, sheet2, sheet3):
    
    with open("eod.txt", "a") as text_file:
        print(sheet1, file=text_file)
        print(sheet2, file=text_file)
        print(sheet3, file=text_file)

main()

    
    
