#! /usr/bin/python3
import base64
import io
import json
import os
import bitwarden_keyring as bwkr

# for linux export BITWARDENCLI_APPDATA_DIR=~/.config/Bitwarden\ CLI/
if __name__ == '__main__':
  #parse_commandline(sys.argv[1:])
  print ("BW_SESSION=%s" % bwkr.get_session(os.environ))
