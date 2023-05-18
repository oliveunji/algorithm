class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numToIndexMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numToIndexMap.containsKey(complement)) {
                return new int[] { numToIndexMap.get(complement), i };
            }
            numToIndexMap.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two elements add up to the target");
    }
}