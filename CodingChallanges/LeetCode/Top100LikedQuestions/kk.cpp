#include <stdio.h>
#include <vector>

class Solution {
  public:
    int maxSubArray() {
      std::vector<int> nums = {1};
      int f = 0;
      int max_sum;
      for (int i=0; i < nums.size(); i++) {
        int next_vector_size = (nums.size() - i);
        int inner_sum = nums[i];
        for (int j=i; j < next_vector_size; j++) {
          inner_sum += nums[j+1];
        }
        if (f == 0) {
          f = 1;
          max_sum = inner_sum;
          continue;
        }
        if (max_sum < inner_sum) {
          max_sum = inner_sum;
        }
      }
      return max_sum;
    }
};

int main(void) {
  Solution s;
  printf("MAX_SUBARRAY: %d\n", s.maxSubArray());
}
