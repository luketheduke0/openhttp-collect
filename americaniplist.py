#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  


#Makes a list of all known US IP addresses based on a range of IPs

#import csv
import sys
linearray = []
ip1array = []
ip2array = []
error = 0
finalstring = ""


with open('us_ips.csv', 'r') as f:
    for line in f:
        #splits csv values into array
        linearray = line.split(",")
        #splits IP addresses into array separated by period
        #eg, ip1array[0,1,2,3] == (192,168,1,254) or whatever
        try:
            ip1array = str(linearray[0]).split(".")
            ip2array = str(linearray[1]).split(".")
            print(ip2array)
        except IndexError:
            print("Ran out of stuff to split")
            sys.exit(0)
        
        while(int(ip1array[0]) <= int(ip2array[0])):
            
            while(int(ip1array[1]) <= int(ip2array[1])):
                
                while(int(ip1array[2]) <= int(ip2array[2])):
                    
                    while(int(ip1array[3]) <= int(ip2array[3])):
                        
                        finalstring = (str(ip1array[0])+"."+str(ip1array[1])+"."+str(ip1array[2])+"."+str(ip1array[3]))
                        print(finalstring)
                        with open("usiplist.txt", "a") as myfile:
                            myfile.write(finalstring+"\n")
            
                        ip1array[3] = int(ip1array[3]) + 1
            
                    ip1array[2] = int(ip1array[2]) + 1
                    ip1array[3] = 0
            
                ip1array[1] = int(ip1array[1]) + 1
                ip1array[2] = 0
            
            ip1array[0] = int(ip1array[0]) + 1
            ip1array[1] = 0
        
        






