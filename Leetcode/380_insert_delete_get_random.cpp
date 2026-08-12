class RandomizedSet {
public:

    vector<int> arr;

    unordered_map<int, int> mp;
    // value -> index

    RandomizedSet() {

    }

    bool insert(int val) {

        // Already exists
        if (mp.count(val))
            return false;

        // Insert at end
        arr.push_back(val);

        // Store index
        mp[val] = arr.size() - 1;

        return true;
    }

    bool remove(int val) {

        // Doesn't exist
        if (!mp.count(val))
            return false;

        int idx = mp[val];

        int lastElement = arr.back();

        // Move last element to idx
        arr[idx] = lastElement;

        // Update hashmap
        mp[lastElement] = idx;

        // Remove last
        arr.pop_back();

        // Remove val from hashmap
        mp.erase(val);

        return true;
    }

    int getRandom() {

        int idx = rand() % arr.size();

        return arr[idx];
    }
};