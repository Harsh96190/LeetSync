class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int>mp;
        int sum = 0,count = 0;
         mp[0] = 1;
for ( int i = 0;i<nums.size();i++)
{      sum += nums[i];
      if (mp.find(sum-k)!=mp.end())
    {
        count += mp[sum-k];
    }
 
    mp[sum]++;
  
}
    return count;   
    }
};