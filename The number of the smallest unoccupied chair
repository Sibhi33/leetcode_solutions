class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int tf) {
        int n = times.size();  // Number of people
        vector<pair<pair<int, int>, int>> events;  // To store events (arrival, departure)
        
        // Create events: (time, type), person index
        for (int i = 0; i < n; i++) {
            events.push_back({{times[i][0], 1}, i});  // Arrival event (1 means arrival)
            events.push_back({{times[i][1], -1}, i}); // Departure event (-1 means departure)
        }
        
        // Sort events by time; for same time, departure comes before arrival
        sort(events.begin(), events.end());
        
        vector<int> assignedChairs(n, -1);  // Track which chair each person gets
        priority_queue<int, vector<int>, greater<int>> availableChairs;  // Min-heap for free chairs
        
        // Initially all chairs are available
        for (int i = 0; i < n; i++) {
            availableChairs.push(i);
        }

        // Process each event
        for (auto& event : events) {
            int time = event.first.first;
            int type = event.first.second;
            int person = event.second;

            // If it's the target friend's arrival
            if (person == tf && type == 1) {
                return availableChairs.top();  // Return the smallest chair available
            }
            
            // If it's an arrival event
            if (type == 1) {
                assignedChairs[person] = availableChairs.top();  // Assign the smallest chair
                availableChairs.pop();  // Remove the chair from available
            }
            // If it's a departure event
            else {
                availableChairs.push(assignedChairs[person]);  // Free up the chair
                assignedChairs[person] = -1;  // Mark chair as free
            }
        }
        
        return -1;  // This line should not be reached
    }
};
