#!/bin/bash
declare -i number1
declare -i number2
declare -i total
echo "What's your favourite number?"
    read number1
echo "What's your favourite number?"
    read number2
total=$number1*$number2
echo "Aha! They equal" $total

exit 0
