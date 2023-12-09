#include <stdio.h>
#define SIZE 5
int* somme_parziali(int[]);
void input(int[]);
 
int main(){
   int n[]={0,1,2,3,4};
   int* r=somme_parziali(n);
   for (int i=0; i!=SIZE; i++) {
    printf("%d ",r[i]);
   }
}

int* somme_parziali(int n[SIZE]){
  int somme=0;
  static int s[SIZE];
  for (int i=0; i!=SIZE; i++) {
    somme+=n[i];
    s[i]=somme;
  }
  return s;
}
