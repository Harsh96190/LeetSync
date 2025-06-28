class Solution {
public:
    int search(vector<int>& nums, int target) {
       int high = nums.size()-1, low = 0;
        while (high >=low)
        {
            int mid = low + (high-low)/2;
        
            if (nums[mid]==target) return mid;
            if (nums[low]<=nums[mid])
            {
                if(nums[low] <=target && nums[mid]>=target) high = mid-1;
                else low = mid + 1;
            }
            else{
                if(nums[mid] <=target && nums[high]>=target) low = mid + 1;
                else high = mid -1;
            }
        }
        return -1;
    }   
};