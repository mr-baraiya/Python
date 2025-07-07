import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by start day
        events.sort(key=lambda x: x[0])

        min_heap = []  # stores end days
        i = 0
        n = len(events)
        count = 0

        # Find the last possible day any event ends
        last_day = max(end for _, end in events)

        # Simulate each day
        for day in range(1, last_day + 1):
            # Add all events starting today
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Remove all expired events
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event that ends the earliest
            if min_heap:
                heapq.heappop(min_heap)
                count += 1

        return count
