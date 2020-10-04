#!/bin/bash

OUTPUT="$(sudo service factorio players-online)"

if [ -z "$OUTPUT" ]; then
       aws ec2 stop-instances --instance-ids i-0cd692cb7106be2b9
else
        echo $OUTPUT
fi
