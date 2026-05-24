class Solution {
  public:
    int coin(vector<int>& arr) {
        int st = 0;
        int lst = arr.size() - 1;
        while(st < lst) {
            if(arr[lst] > arr[st]) {
                lst -= 1;
            } else {
                 st += 1;
            }
        }
        return arr[st];
    }
};