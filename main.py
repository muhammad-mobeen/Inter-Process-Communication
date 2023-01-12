'''
Author: Muhammad Mobeen
Reg No: 200901097
BS-CS-01 (B)
Lab Task [11 Jan 202]
Submitted to Mam Reeda Saeed

GitHub Repo URL: https://github.com/muhammad-mobeen/Inter-Process-Communication
'''
import subprocess


with subprocess.Popen(["python","input.py"],stdin=subprocess.PIPE,stdout=subprocess.PIPE) as process:
    output = process.stdout.read()
    print(output.decode())