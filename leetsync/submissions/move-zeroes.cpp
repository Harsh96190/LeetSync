class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0;
        int count=0;
        int n= nums.size();
        vector <int>temp(n,0);
     for (auto it :nums){
     if (it != 0)
     {
        temp[i]=it;
        i++;
     }  
     else {count ++;}
    }

    int j=0;
    for (auto it : temp)
    {
        nums[j]=it;
        j++;
    }
    }
};