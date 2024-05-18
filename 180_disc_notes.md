# Dynamic Programming

## Climbing Stairs

  1. Ways to solve the problem: imagine you are at the solution, try to deconstruct
  2. Every step you are at can be attributed to the last two moves (1 or 2 jumps)
  3. Recursive relation: dp[i] = dp[i - 1] + dp[i - 2]
  
  code: 
   ```
   if (n == 2) return 2;
   if (n == 1) return 1;
   
   vector<int>dp(n+1);
   
   dp[0] = 0;
   dp[1] = 1;
   dp[2] = 2;
   
   for (int i = 3; i < dp.size(); i++){
	   dp[i] = dp[i-1] + dp[i-2];
   }
   
   return dp[n];
   ```
   
  time complexity: O(N), as we have to loop through the size of the vector
  
## Triange

  1. Ways to solve the problem: compare the next two adjacent paths to the next row at each step
  2. Keep a two-d array that holds the minimums for the previous steps
  3. formula at each step: dp[i] = min[op1, op2]
  4. Must look at every jth node in every ith layer
  5. Recursive relation: minimum path from the node is the mininimum of the two children plus itself
  
  code:
  ```
  
  int solve(int i, int j, vector<vector<int>>& triangle, vector<vector<int>>& dp){
        if (i >= triangle.size() || j >= triangle.size()) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        int op1 = triangle[i][j] + solve(i+1, j, triangle, dp); //next row, same col. (left child)
        int op2 = triangle[i][j] + solve(i+1, j+1, triangle, dp); //next row, next col. (right child)
        return dp[i][j] = min(op1, op2);
    }
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>>dp(triangle.size()+1, vector<int>(triangle.size() + 1,-1));
        return solve(0,0,triangle,dp);
    }
  
  ```

