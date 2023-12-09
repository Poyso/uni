#include <stdio.h>

float radice2(float);
float abs_val(float);
void radicen(int);

int main(){
  float n = 5;
  int x=2;
  x=n/x;
  printf("%f\n",abs_val(-4));
  printf("%f\n",radice2(4));
  radicen(20);
}


float abs_val(float x){
  return x<0 ? -x : x;
}

void radicen(int x){
  for (int i=0; i<x+1; i++) {
    printf("%d = %f\n", i,radice2(i));
  }
}

float radice2(float x){
  float g=x;
  while (abs_val(g*g-x)>0.00001) {
    g=(g+x/g)/2;
  }
  return g;
}
