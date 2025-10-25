class Solution:
    def totalMoney(self, n: int) -> int:
        def summ(a, d, k):
            return (2*a + d*(k - 1))*k//2

        numOfWeeks = n//7
        numOfLastDays = n%7
        weekBaseSum = summ(1, 1, 7)*numOfWeeks
        weekRaiseSum = summ(0, 7, numOfWeeks)
        lastDaysSum = summ(numOfWeeks + 1, 1, numOfLastDays)
        
        return weekBaseSum + weekRaiseSum + lastDaysSum
