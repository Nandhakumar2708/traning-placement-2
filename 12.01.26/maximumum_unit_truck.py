class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        i = 0
        nor_val = 0
        
        # Sort by units per box (descending)
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        while i < len(boxTypes) and truckSize > 0:
            j = 0
            mul_val = 1

            while j < 2:
                if j == 0:
                    if truckSize < boxTypes[i][j]:
                        mul_val *= truckSize
                        truckSize = 0
                    else:
                        mul_val *= boxTypes[i][j]
                        truckSize -= boxTypes[i][j]
                else:
                    mul_val *= boxTypes[i][j]
                j += 1

            nor_val += mul_val
            i += 1

        return nor_val
