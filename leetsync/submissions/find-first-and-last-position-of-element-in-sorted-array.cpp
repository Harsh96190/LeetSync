class Solution {
public:
    int FirstPos (vector<int>&nums,int target)
    {   int first=-1;
        int high = nums.size()-1, low = 0;
        while (high >=low)
        {
            int mid = low + (high-low)/2;
            if (nums[mid]==target) high = mid-1,first=mid;
            else if (nums[mid]>target) high = mid-1;
            else low = mid+1;
        }
        return first;
    }

       int LastPos (vector<int>&nums,int target)
    {   int last=-1;
        int high = nums.size()-1, low = 0;
        while (high >=low)
        {
            int mid = low + (high-low)/2;
            if (nums[mid]==target) low = mid+1,last=mid;
            else if (nums[mid]>target) high = mid-1;
            else low = mid+1;
        }
        return last;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>result;
        result.push_back(FirstPos(nums,target));
        result.push_back(LastPos(nums,target));
        return result;
    }
};