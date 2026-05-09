class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        //keep a letter frequency array of s1
        //get legnth of s1 = n, that is the window size for s2
        //slide window on s2 from start to end
        //during each iteration keep letter frequency for this iteration using sliding window technique
        //-- on the one slid away at left, ++one added on right
        //check the table matches s2
        //iterate till s2 is finished
        if(s1.length()>s2.length()) return false;
        std::vector<int> s1_freq(26);
        std::vector<int>s2_freq(26);
        int wind_size = s1.length();
        for(int i =0;i<s1.length();i++){
            s1_freq[s1[i]-'a']++;
        }

        //start sliding window with two pointers
        int left = 0;
        int right = wind_size-1;
        for(int i  = 0; i<wind_size;i++){
            s2_freq[s2[i]-'a']++;
        }
        int sum=0;
        for(int i =0;i<26;i++){
            sum =sum+std::abs(s1_freq[i]-s2_freq[i]);

        }
        if(sum==0)return true;

        while(right<s2.length()){
            right++;
            s2_freq[s2[right]-'a']++;
            s2_freq[s2[left]-'a']--;
            left++;
            
            sum=0;
            for(int i =0;i<26;i++){
            sum = sum+std::abs(s1_freq[i]-s2_freq[i]);
            }
            if(sum==0)return true;
        }
        return false;
        // return s1_freq[2]==1;
    }
};
