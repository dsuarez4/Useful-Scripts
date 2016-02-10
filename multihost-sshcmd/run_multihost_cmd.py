#! /bin/python -W ignore

## USAGE:
#
# python multihost-sshcmd.py 
#
##

import sys

add_modules=[
	"",
	""
		]

sys.path[0:0]=add_modules
import json, threading
import argparse
import paramiko
import cffi

print 'past libgmp warn...'

outlock = threading.Lock()

def remoteCmd(user, host, count):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	ssh.connect(host, username=user, gss_auth = True, gss_kex = True)

	stdin, stdout, stderr = ssh.exec_command("id | awk '{print $1}'; hostname;sleep 1")
	stdin.write('xy\n')
	stdin.flush()

	with outlock:
		print "Host %d" %(count)
		for line in stdout.read().splitlines():
			print '%s' % (line)

	ssh.close()

def remoteCmdWithPassword(user, passwd, host, count):
	ssh = paramiko.SSHClient()

