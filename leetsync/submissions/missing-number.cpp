class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr(n + 1, 0); // Create a count array of size n+1
        
        // Count the occurrences
        for (int i = 0; i < n; i++) {
            arr[nums[i]]++;
        }

        // Find the number which has count 0
        for (int i = 0; i <= n; i++) {
            if (arr[i] == 0) return i;
        }

        return -1; // This should never happen for valid input
    }
};
