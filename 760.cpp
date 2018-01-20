/*Accept!*/




class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {

    	std::vector<int> C;
    	int i = 0, j=0;
        for ( i = 0; i != A.size(); ++i)
        {
        	for (j = 0; j != B.size(); ++j)
        	{
        		if(B[j]==A[i]){
        			C.push_back(j);
        			break;
        		}
        		
        	}
        	
        }

        return C;
    }
};