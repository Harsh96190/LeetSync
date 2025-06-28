class Solution {
public:
    bool isPalindrome(int x) {
    int og = x,rev = 0,last_digit;
    if (x<0)
    {return false;}
    while (x>0){
    last_digit = x % 10;
    if (rev >INT_MAX/10 || rev<INT_MIN/10)
    {return false;}
    rev = rev*10 + last_digit;
    x =x /10;
    } 
   return og == rev; 
    }
};