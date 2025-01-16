#!/bin/bash

while IFS= read -r line; do
    # Trim whitespace and store in trimmed_line
    trimmed_line=$(echo -n "$line" | xargs)
    
    # Only process non-empty lines
    if [ ! -z "$trimmed_line" ]; then
        kattis new "$trimmed_line"
    fi
done < problems.txt