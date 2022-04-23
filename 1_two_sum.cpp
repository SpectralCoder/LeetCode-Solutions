class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
         unordered_map<int,int> data;
        int n = nums.size();
        for(int i=0;i<n;++i){
            if(data.find(target-nums[i]) != data.end()) return vector<int>{data[target-nums[i]],i};
            data[nums[i]] = i;
        }
        return {-1,-1};
    }
};