class Solution {
public:
    int maxArea(vector<int>& heights) {
        int start = 0;
        int end = heights.size()-1;
        int largest = 0;
        while(start!=end){
            int volume = min(heights[start], heights[end])*(end-start);
            if(volume>largest){
                largest = volume;
            }
            if (min(heights[start], heights[end]) == heights[start]){
                start++;
            }
            else{
                end--;
            }
        }
        return largest;
        
    }
};
