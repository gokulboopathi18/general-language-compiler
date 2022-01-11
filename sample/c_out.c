
#include<stdio.h>
#include<stdlib.h>
#include<strings.h>

int main () {
double id0 = 9;
double id1 = 24;
double id2 = 10;
double id3;
double id4;
double id5;
id3 = id1*id1-4*id0*id2;

printf("<<श्रीधराचर्यः सूत्रम्>>\n");

printf("अ = %lf \n",id0);

printf("ब = %lf \n",id1);

printf("स = %lf \n",id2);

printf("द = ब * ब - 4 * अ * स ; (discriminiant) द = %lf \n",id3);

if(id3>0) {
	id4 = (-id1+(id3)/(2*id0));

id5 = (-id1-(id3)/(2*id0));

printf("\n>> मूल1 = %lf, ",id4);

printf("मूल2 = %lf \n",id5);

} else{
	if(id3==0) {
	id4 = -id1/(2*id0);

printf("\n>> मूल1 = %lf, ",id4);

printf("मूल2 = %lf \n",id4);

} else{
	printf("मान्य मूलं नास्ति (NOT VALID DISCRIMINANT) \n");
}
}

return 0;
}
