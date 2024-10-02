class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        // This is the sorted array.
        vector<int> srt(arr);
        sort(srt.begin(), srt.end());

        unordered_map<int,int> rank;
        for (auto& num: srt) {
            // hashmap will handle duplicacy using emplace
            rank.emplace(num, rank.size()+1);
        }

        // iterate through the array to assign ranks back.
        for (int i = 0; i < srt.size(); i++) {
            srt[i] = rank[arr[i]];
        }

        return srt;
    }
};
