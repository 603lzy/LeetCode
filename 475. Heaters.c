int cmp(const void *a, const void *b){
        return *(int*)a - *(int*)b;
    }
    
int max(int a, int b){
    return a > b ? a : b;
}

int min(int a, int b){
    return a < b ? a : b;
}

int findRadius(int* houses, int housesSize, int* heaters, int heatersSize) {
    int radius = 0, i = -1, j = 0;
    qsort(houses, housesSize, sizeof(houses[0]), cmp);
    qsort(heaters, heatersSize, sizeof(heaters[0]), cmp);
    while (++i < housesSize){
        if (houses[i] <= heaters[j]){
            if (j == 0){
                radius = max(radius, heaters[0] - houses[i]);
                continue;
            }
        }else{
            while (j != (heatersSize - 1) && heaters[j] < houses[i])
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
