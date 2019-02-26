# Copyright (c) Alex Ellis 2017. All rights reserved.
# Copyright (c) OpenFaaS Author(s) 2018. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import sys
from function import handler

def get_stdin():
    buf = ""
    while(True):
        line = sys.stdin.readline()
        buf += line
        if line == "":
            break
    return buf

if __name__ == "__main__":
    #st = get_stdin()
    result = handler.handle('https://wdwnt.com')
    #out_buffer = "HTTP/1.1 200 OK\r\n"
    #out_buffer += "Content-Length: "+str(len(result))+"\r\n"
    #out_buffer += "\r\n"
    #out_buffer += result

    #sys.stdout.write(out_buffer)
    #sys.stdout.flush()
    if result != None:
        print(result)
