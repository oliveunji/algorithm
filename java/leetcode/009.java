// https://leetcode.com/problems/palindrome-number

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        String numberAsString = Integer.toString(x);
        int left = 0;
        int right = numberAsString.length() - 1;

        while (left < right) {
            if (numberAsString.charAt(left) != numberAsString.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;

    }
}
