from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        max_heap = []
        
        for ts, tid in self.tweets[userId]:
            heapq.heappush(max_heap, (-ts, tid))
        
        for followeeId in self.following[userId]:
            for ts, tid in self.tweets[followeeId]:
                heapq.heappush(max_heap, (-ts, tid))
        
        result = []
        while max_heap and len(result) < 10:
            ts, tid = heapq.heappop(max_heap)
            result.append(tid)
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)