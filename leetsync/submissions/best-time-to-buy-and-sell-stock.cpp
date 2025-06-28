class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int minimum_price =prices[0], profit = 0;
      for (int i = 0 ;i<prices.size();i++)
      {
        minimum_price = min(minimum_price,prices[i]);
        profit = max (profit,prices[i]-minimum_price);
      } 
      return profit;

    }
};