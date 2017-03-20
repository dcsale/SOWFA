#!/bin/bash
awk -v line=$1 -v new_content="$2" '{
        if (NR == line) {
                print new_content;
        } else {
                print $0;
        }
}' $3


