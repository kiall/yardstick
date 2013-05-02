#!/bin/bash

echo "nginx.statuses.500:1|c" | nc -w 1 -u 127.0.0.1 8125
