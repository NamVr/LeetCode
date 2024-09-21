class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> minutes;

        for (const string& time : timePoints) {
            int hour = stoi(time.substr(0,2));
            int minute = stoi(time.substr(3,2));

            minutes.push_back(hour*60 + minute);
        }

        sort(minutes.begin(), minutes.end());

        int diff = INT_MAX;

        for (int i = 0; i < minutes.size()-1; i++) {
            diff = min(diff, minutes[i+1]-minutes[i]);
        }

        diff = min(diff, (1440 + minutes.front() - minutes.back()));

        return diff;
    }
};
