/*
 * factory.c
 *
 *  Created on: 2017年3月14日
 *      Author: baobao
 */

//Calculate factorial of positive integer using recursive way
double facRecursive(unsigned int n) {

    if(n == 0 || n == 1) {
        return 1;
    } else {
        return n * facRecursive(n-1);
    }
}

//Calculate factorial of positive integer using iteration way
double facIteration(unsigned int n) {

    double facResult = 1.0;
    int i;

    if(n > 1) {
        for(i=2; i<=n; i++) {
            facResult *= i;
        }
    }

    return facResult;
}
