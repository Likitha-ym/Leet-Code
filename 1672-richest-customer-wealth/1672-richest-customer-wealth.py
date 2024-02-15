class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        
        for customer_account in accounts:
            wealth = sum(customer_account)
            max_wealth = max(max_wealth, wealth)
        
        return max_wealth
