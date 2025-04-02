#include <stdio.h>
#include <stdlib.h>

int main()
{
int n = 5;
int pozycja = 1;
n = n & ~(1 << pozycja);
printf("Po zerowaniu bitu na pozycji %d: %d\n", pozycja, n);
return 0;
}
