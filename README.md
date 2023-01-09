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

Then, we will test the algorithm with massive triangular matrice located in test1.py.
