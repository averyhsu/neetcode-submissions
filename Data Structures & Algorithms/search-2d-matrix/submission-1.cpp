class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        //I only look at the first row, 
        //Find the first number that is bigger than target
        //Since its the FIRST, all prev numbers must be smaller therfore, target must be in 
        //the previous row
        int row = matrix.size();
        int col = matrix[0].size();
        int top = 0;
        int bot = row;
        int mid;
        int target_row;
        //look at first column
        while(top<bot){
            mid = (top+bot)/2;
            if(matrix[mid][0]==target) return true;
            else if(matrix[mid][0]<target){
                top = mid+1;
            }
            else// >target
            {
                bot = mid;
            }
        }
        target_row = top;
        if(target_row ==0) return false;
        --target_row;
        auto &search = matrix[target_row];
        return binary_search(search.begin(), search.end(), target);
    }
};
