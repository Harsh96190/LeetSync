class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        unordered_set<int> num_set(nums.begin(), nums.end());
        int longest = 0;

        for (int num : num_set) {
            
            if (num_set.find(num - 1) == num_set.end()) {
                int current = num;
                int streak = 1;

                while (num_set.find(current + 1) != num_set.end()) {
                    current++;
                    streak++;
                }

                longest = max(longest, streak);
            }
        }

        return longest;
    }
};
