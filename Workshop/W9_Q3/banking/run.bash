for i in {1..8}
do
    echo $i
    mkdir -p output
    /bin/python3 sol.py < ./testcases/$i.in > ./output/$i.out
    diff --strip-trailing-cr -w ./testcases/$i.sol ./output/$i.out
done