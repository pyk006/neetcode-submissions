class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        curr_total = [0, 0, 0]

        for i in range(len(bills)):
            if bills[i] == 5:
                curr_total[0] += 1
            if bills[i] == 10:
                if curr_total[0] > 0:
                    curr_total[0] -= 1
                    curr_total[1] += 1
                else:
                    return False
            if bills[i] == 20:
                if curr_total[0] > 2:
                    curr_total[0] -= 3
                    curr_total[2] += 1
                elif curr_total[1] > 0 and curr_total[0] > 0:
                    curr_total[0] -= 1
                    curr_total[1] -= 1
                    curr_total[2] += 1
                else:
                    return False
        
        return True