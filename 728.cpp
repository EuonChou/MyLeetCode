class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
    	int temp = 0;
    	vector<int> v;
    	for (int i = left; i <= right ; ++i)
    	{

    		int j = 0;
    		for (j = i; j != 0; j=j/10)
    		{
    			temp = j%10;
    			if(temp==0||i%temp!=0){
    				break;
    			}

    			/* code */
    		}
    		/* code */
    		if(j==0){
    			v.push_back(i);
    		}
    	}

    	return v;
        
    }
};