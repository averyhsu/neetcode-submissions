class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for(string x:strs){
            res = res + to_string(x.size())+'#'+x;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        
        while(i<s.size()){
            string num="";
            // Get the string length
            while(s[i]!='#'){
                num = num+s[i];
                i++;
            }
            res.push_back(s.substr(i+1, stoi(num)));
            i= i+1+stoi(num);
        }

        return res;
    

    }
};
