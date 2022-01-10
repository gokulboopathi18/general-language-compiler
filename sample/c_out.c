
#include<stdio.h>
#include<stdlib.h>
#include<strings.h>

int main () {
int id0 = 0;
int id1 = 1;
int id2 = 1;
int id3 = 10;
printf("%d முறை பிபோனச்சி எண்கள்: \n",id3+2);

printf("%d ",id0);

printf("%d ",id1);

for (int id4 = 0; id4<id3; id4++)
{id2 = id0+id1;

printf("%d ",id2);

id0 = id1;

id1 = id2;
}
printf("\n");

return 0;
}
