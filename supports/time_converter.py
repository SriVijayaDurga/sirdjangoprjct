from datetime import datetime

def time_converter():
    t = datetime.now()
    dt_obj = datetime.strptime(str(t),'%Y-%m-%d %H:%M:%S.%f')
    millisec = dt_obj.timestamp() * 1000
    return(int(millisec))




