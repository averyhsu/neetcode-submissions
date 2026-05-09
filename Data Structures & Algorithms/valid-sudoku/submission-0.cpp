#include <unordered_set>
#include <iostream>


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_set<int> row[9];        // key -> value
        std::unordered_set<int> col[9]; 
        std::unordered_set<int> sqr[3][3]; 
        
        for(int i = 0; i<9; i++){ //row traversak
            for(int j=0; j<9;j++){//column
               int val = board[i][j];
               if (val == '.') continue;
               
               if( row[i].find(val)!=row[i].end() || 
                 col[j].find(val)!=col[j].end()||
                 sqr[i/3][j/3].find(val)!=sqr[i/3][j/3].end()){

                        return false;
                    }
                row[i].insert(val);
                col[j].insert(val);
                sqr[i/3][j/3].insert(val);

            }
        }
        return true;

        
    }
};
