#!/usr/bin/env bash

# Usage: ./new.sh QUIZ_NUMBER

QUIZ_NUMBER=$1
if [ -f "${QUIZ_NUMBER}.py" ]; then
    echo "${QUIZ_NUMBER}.py exists!!"
    exit 1
fi

touch "${QUIZ_NUMBER}.py"
echo "QUIZ_NUMBER = \"${QUIZ_NUMBER}\"">> "${QUIZ_NUMBER}.py"
cat template.py >> "${QUIZ_NUMBER}.py"
touch "${QUIZ_NUMBER}.ex.in"
touch "${QUIZ_NUMBER}.in"

code ${QUIZ_NUMBER}.py -r
code ${QUIZ_NUMBER}.in -r
code ${QUIZ_NUMBER}.ex.in -r
