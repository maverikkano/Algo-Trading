## freeCodeCamp Course on Algorithmic Trading

[Algorithmic Trading Using Python - Full Course](https://www.youtube.com/watch?v=xfzGZB4HhEE)

Summary: 
1. Get data from IEX Cloud API (sandboxed)
2. Goal: Forumlate a tabular structure of
    - Stock name
    - Stock price
    - Market capitalization
    - No of shares to buy
   * For batch api calls, split the data into 100 parts using chunks() custom method
   * Use the batch API to fetch data of all stocks from the S&P 500 index
     * Store this data in a dataframe for the above mentioned columns (keep N/A for no of shares to buy, as we will calculate that next)
3. Set value of portfolio_value, hardcoded or user inputted (make sure its large enough so we can buy all stocks in at least 1 quantity)
   - `position_size = portfolio_size / len(final_dataframe.index)`
   - `noOfSharesToBuy = math.floor(position_size/stockPrice)`
