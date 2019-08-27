#! /usr/bin/python3
import base64
import io
import json
import os
import bitwarden_keyring as bwkr

# for linux export BITWARDENCLI_APPDATA_DIR=~/.config/Bitwarden\ CLI/
#bwkr.get_db_location({"BITWARDENCLI_APPDATA_DIR": "/yay"}, "")

#bwkr.ask_for_session(True) == "yay"
#bwkr.ask_for_session(True) 
bwkr.get_session("BW_SESSION")
