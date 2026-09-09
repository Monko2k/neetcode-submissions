class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        taskCount = defaultdict(int)

        for task in tasks:
            taskCount[task] += 1
        
        heap = []
        
        for task, count in taskCount.items():
            heapq.heappush_max(heap, (count, task))

        queue = deque()
        time = 0

        while queue or heap:
            time +=1 
            if queue:
                cooldown, count, task = queue[0]
                if cooldown < time:
                    queue.popleft()
                    heapq.heappush_max(heap, (count, task))
            if heap:
                count, task = heapq.heappop_max(heap)
                if count > 1:
                    queue.append((time + n, count - 1, task))


        return time

        
        