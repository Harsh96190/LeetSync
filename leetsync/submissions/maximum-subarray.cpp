class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    int sum = 0 ,final_sum=INT_MIN;
    for (int i =0;i<nums.size();i++)
    {
     sum += nums[i];
    final_sum = max(sum,final_sum);
    if (sum <0){ sum =0;}
     } 

  return final_sum;      
    }
};