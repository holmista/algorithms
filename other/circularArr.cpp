#include <iostream>
using namespace std;

void printCircular(int arr[], int startIdx, int arrLen){
    int i = startIdx;
    while(i<startIdx+arrLen){
        cout << arr[i%arrLen];
        i++;
    }
}

int main(){
    int arr[] = {1, 2, 3, 4, 5, 6};
    printCircular(arr, 2, sizeof(arr)/sizeof(int));
    return 0;
}