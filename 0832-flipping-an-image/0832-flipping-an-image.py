class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            
            image[i] = [1 - p for p in image[i][::-1]]
        return image
