We will have an orthogonal triangle input from a file and we need to find the maximum sum of the numbers according to given rules below;

1. We will start from the top and move downwards to an adjacent number as in below.
2. We are only allowed to walk downwards and diagonally.
3. We can only walk over NON PRIME NUMBERS.
4. We have to reach at the end of the pyramid as much as possible.
5. We have to treat the input as pyramid.

For instance, according to above rules the maximum sum of the numbers from top to bottom in below example is 24.

      *1
     *8 4
    2 *6 9
   8 5 *9 3

As we can see this has several paths that fits the rule of NOT PRIME NUMBERS; 1>8>6>9, 1>4>6>9, 1>4>9>9
1 + 8 + 6 + 9 = 24.  As we see 1, 8, 6, 9 are all NOT PRIME NUMBERS and walking over these yields the maximum sum.

For this path, we are going to use maximumSum function in the max_path_sum.py code.

Then, we will test the algorithm with following triangular matrice located in test1.py.

215
193 124
117 237 442
218 935 347 235
320 804 522 417 345
229 601 723 835 133 124
248 202 277 433 207 263 257
359 464 504 528 516 716 871 182
461 441 426 656 863 560 380 171 923
381 348 573 533 447 632 387 176 975 449
223 711 445 645 245 543 931 532 937 541 444
330 131 333 928 377 733 017 778 839 168 197 197
131 171 522 137 217 224 291 413 528 520 227 229 928
223 626 034 683 839 053 627 310 713 999 629 817 410 121
924 622 911 233 325 139 721 218 253 223 107 233 230 124 233