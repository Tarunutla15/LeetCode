class Solution:
    def minimumSteps(self, s: str) -> int:
        l = [x for x in s]
        z = []
        x = True
        left_pointer = 0
        right_pointer = len(l) - 1

        while x:
            
            while left_pointer < len(l) and l[left_pointer] != "1":
                left_pointer += 1
            
            while right_pointer >= 0 and l[right_pointer] != "0":
                right_pointer -= 1

            
            if left_pointer < right_pointer:
                
                l[left_pointer] = "0"
                l[right_pointer] = "1"
                z.append(right_pointer - left_pointer)
                left_pointer += 1
                right_pointer -= 1
            else:
                x = False
        print(sum(z))
        return sum(z)
