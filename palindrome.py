class Solution:
  def isPalindrome(self, x: int) -> bool:
    s = str(x)
    return s = s[:: -1] #reverse the string by slicing 