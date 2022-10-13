#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

class Solution:
  def isPalindrome(self, head) -> bool:
    p = ''
    while (head):
      p += str(head[0])
      head.pop(0)
    if (not p):
      return False
    p_len = len(p)
    if (p_len == 1):
      return True
    if (p[:p_len//2] == ''.join(reversed(p[(p_len//2) + p_len%2:]))):
      return True
    return False

if __name__ == '__main__':
  s = Solution()
  head = [1, 2, 2, 1]
  head = [1,3,4,4,1]
  head = []
  print(s.isPalindrome(head))
