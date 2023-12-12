#include <stdio.h>
#include <string.h>

int str_to_int(char*);
int somma(int,int);

int main(int argc,char* argv[]){
  int r=somma(str_to_int(argv[1]),str_to_int(argv[2]));
  printf("%d",r);
}

int str_to_int(char* s){
  int j=0,r=0,k=1;
  for (int i=strlen(s)-1; i!=-1; i--) {
    r+=((int)s[i]-48)*k;
    j++;k*=10;
  }
  return r;
}

int somma(int x,int y){
  return x+y;
}

// esercizio
//
// Scrivere un programma che
// ordini le stringhe sulla linea di comando in ordine alfabetico
// e le stampa in ordine in alfabetico
//
// usare merge sort
