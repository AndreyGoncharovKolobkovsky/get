#include <iostream>
#include <string>
using namespace std;
#include <math.h>
unsigned long long int get_a_hexadecimal(){
    string s;
    char c;
    unsigned long long int num_10 = 0;
    while(true){
        c = getchar();
        if((c <= 'F' and c >= 'A') or (c <= '9' and c >= '0')){
            s += c;
        } else if(c == ' ' or c == '\n') break;
        else return 0;
    }
    int Pos_16[6] = {10, 11, 12, 13, 14, 15};
    for(unsigned int i = 0; i < s.size(); i++){
        num_10 *= 16;
        if(s[i] <= 'F' and s[i] >= 'A') num_10 += Pos_16[s[i] - 'A'];
        else num_10 += (s[i] - '0');
    }
    return num_10;
}
int main1()
{
    cout << get_a_hexadecimal() << endl;
    return 0;
}