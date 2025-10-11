class Solution:
    def maximumTotalDamage(self, power):
        damageFrequency = defaultdict(int)
        for damage in power:
            damageFrequency[damage] += 1

        uniqueDamages = sorted(damageFrequency.keys())
        totalUniqueDamages = len(uniqueDamages)
        maxDamageDP = [0] * totalUniqueDamages

        maxDamageDP[0] = uniqueDamages[0] * damageFrequency[uniqueDamages[0]]

        for i in range(1, totalUniqueDamages):
            currentDamageValue = uniqueDamages[i]
            currentDamageTotal = currentDamageValue * damageFrequency[currentDamageValue]

            maxDamageDP[i] = maxDamageDP[i - 1]

            previousIndex = i - 1
            while (previousIndex >= 0 and 
                   (uniqueDamages[previousIndex] == currentDamageValue - 1 or 
                    uniqueDamages[previousIndex] == currentDamageValue - 2 or 
                    uniqueDamages[previousIndex] == currentDamageValue + 1 or 
                    uniqueDamages[previousIndex] == currentDamageValue + 2)):
                previousIndex -= 1

            if previousIndex >= 0:
                maxDamageDP[i] = max(maxDamageDP[i], maxDamageDP[previousIndex] + currentDamageTotal)
            else:
                maxDamageDP[i] = max(maxDamageDP[i], currentDamageTotal)

        return maxDamageDP[totalUniqueDamages - 1]

        
