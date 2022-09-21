#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int N;
    cin >> N;
    vector <int> gameMode_creative(N, 0);
    for(int i = 0; i < N; i++) cin >> gameMode_creative[i];
    for(int i = 0; i < N; i++){
        if(i == 0) cout << gameMode_creative[N/2 + 1];
        else if(i < N/2)
    }
    return 0;
}