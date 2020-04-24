#!/bin/env bash 

#for i in {1..6}
#do 
#  echo "i am wolf"
#done
#
#for i in {0..50..2}
#do 
#  echo $i
#done 

#for i in $(seq 10) 
#do 
#  echo $i 
#done
#
#for i in $(seq 10 -1 1) 
#do 
#  echo $i 
#done

#for i in $(seq 1 2 10) 
#do 
#  echo $i 
#done

#for i  
#do 
#  echo $i
#done


#for ((i=1;i<=5;i++))
#do 
#  echo "hello"
#done

#for ((i=1;i<=10;i+=2))
#do 
#  echo "hello"
#done

#计算1到100的奇数和

#sum=0
#
#for i in {1..100..2} 
#do 
#  let sum=$sum+$i
#done 
#
#echo "sum:"$sum

#sum=0
#
#for i in {1..100}
#do 
#  if [ $[$i%2] -ne 0 ]
#  then 
#    let sum=$sum+$i
#  fi
#done
#
#echo "sum:"$sum

#for i in {1..5}
#do 
#  if test $i -eq 3
#  then
#    echo "i am break"
#    break
#  fi 
#done

read -p "input a num:" number 

[ $number -eq 1 ] && echo "$number is not zhishu" && exit 
[ $number -eq 2 ] && echo "$number is zhishu" && exit 

for i in `seq 2 $[$number-1]`
do 
  [ $[$number%$i] -eq 0 ] && echo "$number is not zhishu" && exit 
done

echo "$number is zhihsu"
