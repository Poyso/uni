#include <stdio.h>
#include <stdlib.h>
struct sequenza{
  float *a;
  int n; // numero di elementi attuali nella sequenza
  int c; // capacita' di a, cioe' quando spazio c'e'
};
typedef struct sequenza sequenza;
sequenza new_seq(int);
void print(sequenza);
void set_seq(sequenza,int,float);
float get_seq(sequenza,int);
int lens(sequenza);
sequenza append_sequenza(sequenza,float);
sequenza nuovad_sequenza();
int main(){
  sequenza seq = new_seq(10);
  print(seq);
}
sequenza new_seq(int d){
  sequenza s;
  s.a=malloc(sizeof(float)*d);
  s.n=d;
  for (int i=0; i!=s.n; i++) {
    s.a[i]=0;
  }
  return s;
}
void print(sequenza s){
  for(int i=0;i!=s.n;i++){
    printf("%f ",s.a[i]);
  }
}
void set_seq(sequenza s,int k,float f){
  s.a[k]=f;
}
float get_seq(sequenza s,int k){
  return s.a[k];
}
int lens(sequenza s){
  return s.n;
}
sequenza nuova_sequenza(){
  sequenza v = {NULL,0,0};
  return v;
}
sequenza append_sequenza(sequenza z,float x){
  int i,n=lens(z)+1;
  float *b;
  if(z.n==z.c){
    z.c=2*z.c+1;
    b=malloc(sizeof(float)*z.c);
    for (int i=0; i!=n-1; i++) {
      b[i]=z.a[i];
    }
    free(z.a);
    z.a=b;
  }
  b[n]=x;
  n++;
  return z;
}
