class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    frequency_dict = {}
    
    for num in arr:
      if num in frequency_dict:
        frequency_dict[num] += 1
      else:
        frequency_dict[num] = 1
    
    frequency_set = set(frequency_dict.values())
    
    return len(frequency_set) == len(frequency_dict)