    class Solution {
    public:
        int arrayPairSum(vector<int>& nums) {
            //Accept!
            //题上给出 数的范围为-10000 到 10000
            std::vector<int> hashTable(20000, 0);
            int sum=0;
            bool flag = true;
            for (std::vector<int>::iterator i = nums.begin(); i != nums.end(); ++i)
            {
                hashTable[*i+10000]++;                
            }


            for (int i = 0; i < 20000; ++i)
            {
                while(hashTable[i]--){
                    if(flag){
                        sum += i-10000;
                        flag = false;
                    }else{
                        flag = true;
                    }
                }

                /* code */
            }
            return sum;
        
        }

        // int arrayPairSum1(vector<int>& nums) {
        //     //不能通过，时间超限
            
        //     int sum = 0;
        //     int temp = 0;
        //     bool flag = true;
        //     for (int i = 0; i < nums.size(); ++i)
        //     {
        //         for (int j = i+1; j < nums.size(); ++j)
        //         {
        //             if(nums[i] > nums[j]){
        //                 temp = nums[i];
        //                 nums[i] = nums[j];
        //                 nums[j] = temp;
        //             }
                    
        //         }   
                
        //         if(i%2==0){
        //             sum += nums[i];
                    
        //         }
        //     }
            
        //     return sum;

        // }
    };