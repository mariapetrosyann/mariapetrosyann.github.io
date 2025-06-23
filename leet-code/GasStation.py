class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        first_tank = 0
        i = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            tank += gain
            first_tank += gain
            if first_tank < 0:
                start_index = i + 1
                first_tank = 0
        if tank >= 0:
            return start_index
        else:
            return -1
