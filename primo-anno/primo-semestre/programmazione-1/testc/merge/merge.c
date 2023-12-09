#include <stdio.h>
void merge(int[],int,int,int);
void mergesort(int[],int,int);

int main() {
  int arr[] = {6, 5, 12, 10, 9, 1};
  int size = sizeof(arr) / sizeof(arr[0]);

  mergesort(arr, 0, size - 1);

  printf("Sorted array: \n");
  for (int i = 0; i < size; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

void merge(int arr[], int l, int m, int r) {

  // Create L ← A[p..q] and M ← A[q+1..r]
  int n1 = m - l + 1;
  int n2 = r - m;

  int L[n1], M[n2];

  for (int i = 0; i < n1; i++)
    L[i] = arr[l + i];
  for (int j = 0; j < n2; j++)
    M[j] = arr[m + 1 + j];

  // Maintain current index of sub-arrays and main array
  int i, j, k;
  i = 0;
  j = 0;
  k = l;

  // Until we reach either end of either L or M, pick larger among
  // elements L and M and place them in the correct position at A[p..r]
  while (i < n1 && j < n2) {
    if (L[i] <= M[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = M[j];
      j++;
    }
    k++;
  }

  // When we run out of elements in either L or M,
  // pick up the remaining elements and put in A[p..r]
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  while (j < n2) {
    arr[k] = M[j];
    j++;
    k++;
  }
}

// Divide the array into two subarrays, sort them and merge them
void mergesort(int arr[], int l, int r) {
  if (l < r) {
    // m is the point where the array is divided into two subarrays
    int m = l + (r - l) / 2;
    mergesort(arr, l, m);
    mergesort(arr, m + 1, r);
    // Merge the sorted subarrays
    merge(arr, l, m, r);
  }
}
