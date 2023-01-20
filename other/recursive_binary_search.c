#include <stdio.h>

int binSearch(int t, int *arr, int l, int r)
{
    int m = (l+r)/2;
    if (arr[m] == t) return m;
    if (r<=l) return -1;
    if (t<arr[m]) return binSearch(t,arr,l,m-1);
    if (t>arr[m]) return binSearch(t,arr,m+1,r);
    return 0;
}

int main()
{
    int arr[10] = {3,6,9,12,15,18,21,24,27,30};
    int res = binSearch(30,arr,0,sizeof(arr)-1);
    printf("%d\n",res);
    return 0;
}