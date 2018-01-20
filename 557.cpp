/*Accept!*/

/*学会了STL库的Reverse函数*/

class Solution {
public:
    string reverseWords(string s) {
    	int j = 0;

     	for (int i = 0; i <= s.length(); ++i)
    	{
    		if(s[i]==' '){
    			reverse(s.begin() +j, s.begin()+i);
    			i++;
    			j = i;

    		}
    	}

    	reverse(s.begin()+j, s.end()）;    //注意 s.end()代表s末尾的下一个迭代器  并不是结尾元素。 而reverse 第二个参数恰好也是需要下一个位置！！

    	return s;
    }
};