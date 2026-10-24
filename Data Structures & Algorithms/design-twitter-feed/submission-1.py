class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                counter, tweetId = self.tweets[followeeId][idx]
                heapq.heappush_max(heap, (counter, tweetId, followeeId, idx - 1))
        
        while heap and len(res) < 10:
            counter, tweetId, followeeId, idx = heapq.heappop_max(heap)
            res.append(tweetId)
            if idx >= 0:
                counter, tweetId = self.tweets[followeeId][idx]
                heapq.heappush_max(heap, (counter, tweetId, followeeId, idx - 1))
        return res



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
