#! /usr/bin/python3
import base64
import io
import json
import os
import bitwarden_keyring as bwkr

# for linux export BITWARDENCLI_APPDATA_DIR=~/.config/Bitwarden\ CLI/
#bwkr.get_db_location({"BITWARDENCLI_APPDATA_DIR": "/yay"}, "")

#bwkr.ask_for_session(True) == "yay"
# 


if __name__ == '__main__':
    print ("path=%s" % bwkr.get_db_location(os.environ,"linux"))
    #print ("ASK_BW_SESSION=%s " % bwkr.ask_for_session(False))
    #print ("ASK_BW_SESSION=%s " % bwkr.ask_for_session(True))
#    print ("BW_SESSION=%s " % bwkr.get_session(os.environ))
    print ("password=%s " % bwkr.get_password("login","va32lnagios01.mot.com"))

