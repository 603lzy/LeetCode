class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        int radius = 0, i = -1, j = 0;
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        while (++i < houses.size()){
            if (houses[i] <= heaters[j]){
                if (j == 0){
                    radius = max(radius, heaters[0] - houses[i]);
                    continue;
                }
            }else{
                while (j != (heaters.size() - 1) && heaters[j] < houses[i])
                    j++;
                if (j == 0 || heaters[j] < houses[i]){
                    radius = max(radius, houses[i] - heaters[j]);
                    continue;
                } 
            }
            radius = max(radius, min(houses[i] - heaters[j - 1], heaters[j] - houses[i]));
        }
        return radius;
    }
};
