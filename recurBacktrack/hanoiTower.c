/*
 * hanoiTower.c
 *
 *  Created on: 2017年3月15日
 *      Author: baobao
 */

#include <stdio.h>
#include <stdlib.h>

void TowersOfHanoi(int n, char frompeg, char topeg, char auxpeg) {
    /* If only 1 disk, make the move and return */
    if(n == 1) {
        printf("\nMove disk 1 from peg %c to peg %c", frompeg, topeg);
        return;
    }

    /*Move top n-1 disks from A to B, using C as auxiliary*/
    TowersOfHanoi(n-1, frompeg, auxpeg, topeg);

    /*Move remaining disks from A to C*/
    printf("\nMove disk %d from peg %c to peg %c", n, frompeg, topeg);

    /*Move n-1 disks from B to C using A as auxiliary*/
    TowersOfHanoi(n-1, auxpeg, topeg, frompeg);
}

/*
void main()
{
    int n;
    printf("\nn阶汉诺塔问题： \n");
    scanf("%d", &n);
    TowersOfHanoi(n, 'A', 'B', 'C');
}


n阶汉诺塔问题： 

Move disk 1 from peg A to peg B
Move disk 2 from peg A to peg C
Move disk 1 from peg B to peg C
Move disk 3 from peg A to peg B
Move disk 1 from peg C to peg A
Move disk 2 from peg C to peg B
Move disk 1 from peg A to peg B
*/
