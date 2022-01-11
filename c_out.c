
#include<stdio.h>
#include<stdlib.h>
#include<strings.h>

int main () {
printf("வணக்கம் - இரு நிலை எண்கள் பாடம்");

int id0 = 60;
int id1 = 13;
int id2 = 0;
id2 = id0&id1;

printf("Line 1 - மதிப்பு of இ is %d\n",id2);

id2 = id0|id1;

printf("Line 2 - மதிப்பு of இ is %d\n",id2);

id2 = id0^id1;

printf("Line 3 - மதிப்பு of இ is %d\n",id2);

id2 = ~id0;

printf("Line 4 - மதிப்பு of இ is %d\n",id2);

id2 = id0<<2;

printf("Line 5 - மதிப்பு of இ is %d\n",id2);

id2 = id0>>2;

printf("Line 6 - மதிப்பு of இ is %d\n",id2);

return 0;
}
