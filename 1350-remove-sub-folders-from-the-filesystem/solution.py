class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort() # lexiographically

        res = [folder[0]] # add the first folder

        # iterate through each folder and check if sub folder exists
        for i in range(1, len(folder)): # 1 -> n-1
            last = res[-1]
            last += "/"

            if not folder[i].startswith(last):
                res.append(folder[i])

        return res  
