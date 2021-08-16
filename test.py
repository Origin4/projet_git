def zeroSum(nums): 
   i_start = 0
   i_end = len(nums) - 1
   while(i_start < i_end):
       temp = nums[i_start] + nums[i_end]
       if temp == 0 : 
           return True
       elif temp < 0 :
           i_start += 1
       else :
           i_end -= 1
   return False

if __name__ == "__main__":
    print("Enter a list of increasing ordered numbers separated by commas : ")
    s = input()
    nums = s.split(",")
    nums = [int(x) for x in nums]
    print("Is there a zero sum in the given list of numbers?")
    print(zeroSum(nums))


