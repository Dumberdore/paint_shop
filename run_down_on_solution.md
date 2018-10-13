
```
pdumbre@pdumbre-mbp : ~/HBC
$ cat ex1.txt 
5
1 M 3 G 5 G
2 G 3 M 4 G
5 M

$ python paintShop.py ex1.txt 

G G G G M

$ cat ex2.txt 
1
1 G
1 M

$ python paintShop.py ex2.txt 

No solution exists

$ cat ex3.txt 
5
2 M
5 G
1 G
5 G 1 G 4 M
3 G
5 G
3 G 5 G 1 G
3 G
2 M
5 G 1 G
2 M
5 G
4 M
5 G 4 M

$ python paintShop.py ex3.txt 

G M G M G

$ cat ex4.txt 
2
1 G 2 M
1 M

$ python paintShop.py ex4.txt 

M M

$ cat ex5.txt 
6
2 M
5 G
1 G
5 G 1 G 4 M
3 G
5 G
3 G 5 G 1 G
3 G
2 M
5 G 1 G
2 M
5 G
4 M
5 G 4 M
1 M 5 M 3 M 4 G 2 G 6 M

$ python paintShop.py ex5.txt 

G M G M G M

$ cat ex6.txt 
5
2 M
5 G
1 G
5 G 1 G 4 M
3 G
5 G
3 G 5 G 1 G
3 G
2 M
5 G 1 G
2 M
5 G
4 M
5 G 4 M
1 M 5 M 3 M 4 G 2 G

$ python paintShop.py ex6.txt 

No solution exists

```
