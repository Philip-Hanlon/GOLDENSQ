import math
def Reading_time (Mynum_words, MyReading_speed):
    Myreading_time = (Mynum_words / MyReading_speed)
    return (Myreading_time)
    """MyNumberofSeconds, MyNumberofMins = math.modf(Myreading_time)

    MyNumberofSeconds = int(60 * MyNumberofSeconds)
    MyNumberofMins = int(MyNumberofMins)
    myReturn = str(Mynum_words) + ' words will take ' + str(MyNumberofMins) + ' minutes and ' + str(MyNumberofSeconds) + ' seconds to read.' 
    myReturn = str(MyNumberofMins) + 'mins ' + str(MyNumberofSeconds) + 'seconds'
    return(myReturn)"""

