from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        if n == 0: return len(tasks)

        # Set up
        schedule = []
        taskMap = {}
        
        for task in tasks:
            numTasks = taskMap.get(task,0)
            taskMap[task] = numTasks + 1
        

        coolQ = deque([None] * n)
        heap = []
        for name,count in taskMap.items():
            heapq.heappush(heap,(count*-1,name))
        
        queCount = 0
        while len(heap) or queCount:
            print(len(heap),queCount)

            if heap: 
                currTask = heapq.heappop(heap)
                schedule.append(currTask[1])
                taskCount = (currTask[0] * -1) - 1 
                if taskCount:
                    coolQ.appendleft((-taskCount,currTask[1]))
                    queCount += 1
                else:
                    coolQ.appendleft(None)
            else: 
                coolQ.appendleft(None)
                schedule.append(None)

            queTask = coolQ.pop()
            if queTask: 
                heapq.heappush(heap,queTask)
                queCount -= 1
        print(schedule)  
        return len(schedule)

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 3
s = Solution()
s.leastInterval(tasks,2)