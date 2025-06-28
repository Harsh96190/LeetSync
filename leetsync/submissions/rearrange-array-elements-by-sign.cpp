class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
   
int n = nums.size();
int j =n-1,k=0;

     vector <int>arr(n);
  for (int i = 0; i<n;i++)
     {
        if (nums[i]<0){arr[j--] = nums[i];}
         else{arr[k++]=nums[i];}  
     } 
     j =n-1,k=0;
for (int i = 0;i<n;i++)
{
if (i%2==0){nums[i]= arr[k++];}
else {nums[i]=arr[j--];}

}
return nums;
    }
};