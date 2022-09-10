class Solution:
    def get_adjacents(self, cell, image):
        coordinates = [
            [cell[0]+1, cell[1]],
            [cell[0], cell[1]-1],
            [cell[0]-1, cell[1]],
            [cell[0], cell[1]+1]
        ]
        result = []
        for i in coordinates:
            if i[0] < 0 or i[0] > len(image) - 1 or i[1] < 0 or i[1] > len(image[0]) - 1:
                pass
            else:
                result.append(i)
        return result
    def floodFill(self, image, sr, sc, color):
        if color == image[sr][sc]:
            return image
        cell = [sr, sc]
        prev_color = image[cell[0]][cell[1]]
        image[cell[0]][cell[1]] = color
        adjacents = self.get_adjacents(cell, image)
        for i in adjacents:
            if image[i[0]][i[1]] == prev_color:
                adjacents = self.get_adjacents(i, image)
                self.floodFill(image, i[0], i[1], color)
        return image

s1 = Solution()
print(s1.floodFill(image= [[0,0,0],[0,0,0]], sr=1, sc=2, color=1))