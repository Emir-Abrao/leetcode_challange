from typing import List
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        
        # Build graph using BFS to find shortest paths
        graph = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            level_size = len(queue)
            level_words = set()
            
            for _ in range(level_size):
                word = queue.popleft()
                curr_dist = distance[word]
                
                # Try all possible transformations
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        next_word = word[:i] + c + word[i+1:]
                        
                        if next_word in wordSet:
                            graph[word].append(next_word)
                            
                            if next_word == endWord:
                                found = True
                            
                            if next_word not in distance:
                                distance[next_word] = curr_dist + 1
                                level_words.add(next_word)
            
            # Remove visited words from this level
            for w in level_words:
                queue.append(w)
                wordSet.discard(w)
        
        if endWord not in distance:
            return []
        
        # DFS to find all shortest paths
        result = []
        
        def dfs(word, path):
            if word == endWord:
                result.append(path[:])
                return
            
            for next_word in graph[word]:
                if next_word in distance and distance[next_word] == distance[word] + 1:
                    path.append(next_word)
                    dfs(next_word, path)
                    path.pop()
        
        dfs(beginWord, [beginWord])
        return result