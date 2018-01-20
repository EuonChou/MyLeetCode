/*Accept!*/


//好的答案
// class Solution {
// public:
//     int findComplement(int num) {
//         unsigned mask = ~0;
//         while (num & mask) mask <<= 1;
//         return ~mask & ~num;
//     }
// };

class Solution {
public:
    int findComplement(int num) {
    	int sum = 0, b = 1;
    	vector<int> v;
    	while(num){
    		v.push_back(num % 2);
    		num = num >> 1;
    	}

    	for (std::vector<int>::iterator i = v.begin(); i != v.end(); ++i)
    	{
    		cout << *i << " ";
    	}

    	sum = 0;
    	for (int i = 0; i < v.size(); i++)
    	{
    		if(v[i]==0){
    	       //取反 并还原为原值
    			b = 1; 
    			for (int j = 0; j < i; j++)
    			{
    				b = b*2;
    			}
                
    			sum += b;

    		}
    		
    	}

    	return sum;



        
    }
};

