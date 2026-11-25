class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        total = 0
        start = 0
        end = len(people) - 1
        curr = 0
        while start <= end:
            if people[start] + people[end] <= limit:
                total += 1
                start += 1
                end -= 1
            elif people[start] == limit:
                total += 1
                start += 1
            elif people[end] == limit:
                total += 1
                end -= 1
            elif people[start] + people[end] == limit:
                total += 1
                start += 1
                end -= 1
            else:
                total += 1
                end -= 1

        return total