from datetime import datetime


def write_logs(dec: int, bin: str, hex: str):
    """Writes down given values to logs with date and time
    Arguments : 
    dec : decimal number as int
    bin : binary number as str
    hex : hexadecimal number as str
    """
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    f = open("logs/logs.txt", "a+")
    f.write(f"[{now}] DECIMAL : {dec}, BINAIRE : {bin}, HEXADECIMAL : {hex}\n")
    f.close()


def clear_logs():
    """Clears logs
    """
    f = open("logs/logs.txt", "w+")
    f.write("")
    f.close()


def get_last_x_logs(x: int) -> str:
    """Returns the last x lines of logs as str
    Arguments : 
    x : number of lines as int, x > 0
    """
    f = open("logs/logs.txt", "r")
    lines = f.readlines()
    if x > lines.length:
        x = lines.length
    if x > 50:
        x = 50
    return_val = ""
    for i in range(1, x+1):
        return_val = return_val+lines[-1*x]
    f.close()
    return return_val
