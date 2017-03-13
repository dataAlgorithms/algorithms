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

/*
Test 

/*
 * helloWorld.c
 *
 *  Created on: 2017年3月13日
 *      Author: baobao
 */

#include <stdio.h>
#include <stdlib.h>


//int helloWorld(void);
double facRecursive(unsigned int n);
double facIteration(unsigned int n);

int main(void) {
	//helloWorld();

	//Calculate factorial using recursive way
	printf("%lf ", facRecursive(0));
	printf("%lf ", facRecursive(1));
	printf("%lf ", facRecursive(10));
	printf("%lf\n", facRecursive(1000));

	//Calculate factorial using loop way
	printf("%lf ", facIteration(0));
	printf("%lf ", facIteration(1));
	printf("%lf ", facIteration(10));
	printf("%lf\n", facIteration(1000));

	return 1;
}


1.000000 1.000000 3628800.000000 1.#INF00
1.000000 1.000000 3628800.000000 1.#INF00

*/
