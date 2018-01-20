/*ACCEPT!*/

class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for (int i = 0; i < moves.length(); ++i)
        {
        	switch(moves[i]){
        		case 'U':
        			y+=1;
        			break;

        		case 'D':
        			y-=1;
        			break;

        		case 'L':
        			x-=1;
        			break;

        		case 'R':
        			x+=1;
        			break;
        	}
        	/* code */
        }

        if(x==0&&y==0){
        	return true;
        }else{
        	return false;
        }
    }
};