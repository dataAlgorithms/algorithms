/*
 * sortArrCheck.c
 *
 *  Created on: 2017年3月15日
 *      Author: baobao
 */

/*
Given an array, check whether the array is in sorted
order with recursion
*/
int isArrayInSortedOrderRec(int A[], int n) {

    if(n == 1) {
        return 1;
    }

    return (A[n-1] < A[n-2])?0:isArrayInSortedOrderRec(A, n-1);
}


/*
Given an array, check whether the array is in sorted
order with iteration
*/
int isArrayInSortedOrderInt(int A[], int n) {

    int i;
    int flag = 1;

    for(i=0; i<n-1; i++) {

        if(A[i] > A[i+1]) {
        	flag = 0;
        	break;
        }
    }

    return flag;
}

/*
    //Check whether array is sorted
    int theArr[5] = {1, 3, 2, 5, 7};

    if(isArrayInSortedOrderRec(theArr, sizeof(theArr)/sizeof(theArr[0])) == 1) {
    	printf("\n\nThe array is sorted!");
    } else {
    	printf("\n\nThe array is not sorted!");
    }

    if(isArrayInSortedOrderInt(theArr, sizeof(theArr)/sizeof(theArr[0])) == 1) {
    	printf("\n\nThe array is sorted!");
    } else {
    	printf("\n\nThe array is not sorted!");
    }
 */
