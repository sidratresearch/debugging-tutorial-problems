// This program segfaults
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *ptr;
    *ptr = 'x';

    return 0;
}