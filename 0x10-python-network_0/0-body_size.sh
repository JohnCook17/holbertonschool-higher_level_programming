#!/bin/bash
# curl to find size of body
curl -s $1 | wc -c
