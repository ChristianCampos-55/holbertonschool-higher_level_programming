#!/bin/bash
#Takes in a URL and sends a POST request to the URL
curl -sL -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
