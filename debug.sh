
###
 # @Author: eive001 Yishang.Zhang@linux.alibaba.com
 # @Date: 2023-03-28 01:10:52
 # @LastEditors: eive001 Yishang.Zhang@linux.alibaba.com
 # @LastEditTime: 2023-03-29 15:21:37
 # @FilePath: /root/tools/CodeAnalyse/debug.sh
 # @Description: 
 # 
 # Copyright (c) 2023 by zhangyishang, All Rights Reserved. 
### 

##
echo "dump function name ========================"
nm $1 | grep '[0-9a-z] [tT]' > map 

echo 
echo replace command to be excute ======================== 
cp debug.in.py debug.py

COMA=""

echo $0 $1 $2
paramCount=$#
printf "paramCount=$paramCount\n"

for (( i = 2; i <= paramCount; i++ )); do
    #statements
   COMA="$COMA  ${!i}"
done
echo  " COMA is   "$COMA
sed -i "s#_replace_#${COMA}#" debug.py
echo "${COMA}"
echo $ARGS

echo  
echo run gdb ======================== 

gdb --batch --command=debug.py  --args $1 > $1-log

echo 
echo analyse the log 
python3 gen_graph.py -i $1-log
#python parse.py  "$1-log" | tee "$1-gdb.path"



rm -rf  debug.py map gdb.txt
