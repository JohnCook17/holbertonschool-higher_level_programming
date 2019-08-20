#!/bin/bash
# show avaliable env
curl -sI -X OPTIONS $1 | grep Allow | cut -d ' ' -f2-
