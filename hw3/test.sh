#!/bin/bash

function Error() {
   echo "ERROR: $1";
}

function Info() {
   echo "> $1";
}

function hasDuplicates() {
   duplicateCount=`sort $1 | uniq -d | wc -l |tr -d ' '`;
   if [ "0" = $duplicateCount ]; then
      echo "NO";
   else
      echo "YES";
   fi
}

function checkForDuplicates() {
   for i in `seq 1 10`; do
      status=`hasDuplicates perms/$i.txt`
      if [ $status = "YES" ]; then
         Error "File perms/$i.txt contain duplicate permutations";
      else
         Info "File perms/$i.txt contain no duplicate permutations";
      fi
   done
}

function fac() {
   echo "define f(x) {if (x>1){return x*f(x-1)};return 1}
           f($1)" | bc
}

function checkNFactorial() {
   for i in `seq 1 10`; do
      if [ `wc -l < perms/$i.txt |tr -d ' '` != `fac $i` ]; then
         Error "perms/$i.txt does not contain `fac $i` permutations";
      else
         Info "perms/$i.txt contain `fac $i` permutations";
      fi
   done
}

function generateTestFiles() {
   if [ ! -d "./perms" ]; then
      mkdir "./perms";
   fi

   for i in `seq 1 10`; do
      Info "Generating permutation file $i.txt";
      python permute.py $i > "perms/$i.txt";
   done
}

function main() {
   generateTestFiles
   checkForDuplicates
   checkNFactorial
}
main
