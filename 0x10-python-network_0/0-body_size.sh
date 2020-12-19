#!/bin/bash
# Displays size of body
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
