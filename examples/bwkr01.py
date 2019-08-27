#! /usr/bin/python3
# NAME
#       bwkr01.py   - example 01 using bitwarden_keyring
#
# REVISION HISTORY
#       08/27/2019 T.J. Yang  init. 
# DESCRIPTION
#  1. tested on centos 7.6 using python36  
#  2. Doing CRUD DB operations on top of bitwarden's linux cli tool.
#

# USAGE
#  ./bwkr01.py options
#       
# DEBUG
#        python3 -m pdb bwkr01.py
#
# OPTIONS
#
#
# RETURN CODE
#       SUCCESS (=0) - script completed successfully
#       ERROR   (=1) - error ... bad things happened
#
#  REFERENCE:
#   1. https://github.com/mickaelperrin/bitwarden-decrypt-cli
#
#
# ---------------------------- CONSTANT DECLARATION ---------------------------
# WHAT: Define exit status flags.
# WHY:  Easier to program with a mnemonic than with the numbers.
# NOTE: THESE DO NOT CHANGE UNLESS NOTIFIED BY HP!  Startup depends on these
#       exit statuses being defined this way.
#

SUCCESS = 0
ERROR   = 1
VERBOSE = False
DEBUG   = False
VERSION = '0.5'
libdir = 'lib'

#
# ---------------------------- IMPORT  DECLARATION ---------------------------
#
import base64
import io
import json
import os
import sys
import getopt
import configparser # https://docs.python.org/3/library/configparser.html
import bitwarden_keyring as bwkr

#
# ---------------------------- VARIABLE DECLARATION ---------------------------
#

#
# ---------------------------- FUNCTION  DECLARATION ---------------------------
#

def parse_commandline(argv):
   global DEBUG  # http://stackoverflow.com/questions/21015066/local-variable-referenced-before-assignment-python-error
   global VERBOSE  # http://stackoverflow.com/questions/21015066/local-variable-referenced-before-assignment-python-error
   if len(argv) < 1 :
      usage()
      sys.exit(2)
   try:            # https://pymotw.com/2/getopt/
      opts, args = getopt.getopt(sys.argv[1:],':hdvV',)
   except getopt.GetoptError:
      print ("Wrong options. ")
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-V", "--Version"):
         print ("%s version %s" % (sys.argv[0],VERSION))
         sys.exit()
      elif opt in ("-d","--debug"):
         DEBUG  = True
      elif opt in ("-v","--verbose"):
         VERBOSE  = True

# usage information
def usage ():
  PROGNAME = sys.argv[0]
  print ( PROGNAME + ": " + PROGNAME + """ \
  [options] 
  options:
  -c, --config=<path>     Path to alternate configuration file
  -d, --debug             log message in /var/log/snowt.log
  -h, --help              Print this usage message
  -v, --verbose           Verbose output (additive)
  -V, --version           Display program version and exit""" )

#
# **************************** MAIN SCRIPT ************************************
#

# for linux export BITWARDENCLI_APPDATA_DIR=~/.config/Bitwarden\ CLI/
# instantiate

if __name__ == '__main__':
   parse_commandline(sys.argv[1:])
   config = configparser.ConfigParser()
   config.read('./bwkeyring.conf') # parse existing file
   if DEBUG: print ("topsecret:%s" % config['topsecret.server.com'])

  #print ("BW_SESSION=%s" % bwkr.get_session(os.environ))
#    print ("path=%s" % bwkr.get_db_location(os.environ,"linux"))
#    print ("ASK_BW_SESSION=%s " % bwkr.ask_for_session(False))
#    print ("ASK_BW_SESSION=%s " % bwkr.ask_for_session(True))
#    print ("BW_SESSION=%s " % bwkr.get_session(os.environ))
#    print ("password=%s " % bwkr.get_password("login","nagios01"))


