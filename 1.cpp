class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	int i=0, j=0;
        for (i = 0; i < nums.size(); ++i){
        	for(j=i+1; j < nums.size(); ++j){
        		if(nums[i] + nums[j]==target){
        			break;
        		}
        	}
        	/* code */
        	if(j<nums.size()){
        		break;
        	}
        }

        vector<int>temp;
        temp.push_back(i);
        temp.push_back(j);

        return temp;

    }
};