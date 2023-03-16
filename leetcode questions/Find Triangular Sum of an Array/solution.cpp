#include <iostream>
#include "vector"
using namespace std;

class Solution {
public:
    int triangularSum(vector<int> &nums) {
            int n = nums.size();
            if(n==1) return nums[0];
            for(int i=0; i<n-1; i++){
                nums[i] = (nums[i]+nums[i+1])%10;
            }
            nums.resize(n-1);
            return triangularSum(nums);
        }
};

int main(){
    Solution sol;
    vector<int> nums = {1,2,3,4,5};
    int sum = sol.triangularSum(nums);
    cout << sum << endl;
    return 0;
}