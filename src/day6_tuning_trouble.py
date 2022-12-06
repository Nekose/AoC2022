def import_data(datafile: str) -> str:
    signal = ""
    with open(datafile) as file:
        for line in file:
            signal += line.rstrip("\r\n")
        return signal

def locate_start(signal:str,length:int) -> int:
    buffer = signal[:length]
    position = length
    for value in signal[length:]:
        if len(set(buffer)) < length:
            buffer = buffer[1:] + value
            position += 1
        else:
            return position,buffer