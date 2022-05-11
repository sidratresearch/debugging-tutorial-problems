#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

    char ch_arr[4][13] = {
        "albatross",
        "spectactular",
        "printing"};

    printf("Hello. In this script, program, we'll start to read things from a character array\n");

    for (int i = 0; i < 4; i++)
    {
        printf("This is the next word: %s\n", ch_arr[i]);
    }

    return 0;
}