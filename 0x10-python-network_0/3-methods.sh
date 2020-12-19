#!/bin/bash
#Takes in a URL and displays all HTTTP methods
curl -sIL "$1" | grep 'Allow:' | cut -d ' ' -f2-
