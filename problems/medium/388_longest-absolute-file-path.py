class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        max_len = 0
        path_len = {0: 0}  # depth -> cumulative path length up to (but not including) this depth
        
        for line in lines:
            # Count the number of tabs to determine depth
            depth = 0
            while depth < len(line) and line[depth] == '\t':
                depth += 1
            
            # Get the actual name (without tabs)
            name = line[depth:]
            
            # Calculate the length of the path up to this item
            # path_len[depth] is the length of the parent path
            # We add len(name) for current item
            # We add 1 for the '/' separator (if not at root)
            if depth == 0:
                current_len = len(name)
            else:
                current_len = path_len[depth] + len(name) + 1  # +1 for '/'
            
            # Check if this is a file (contains a '.')
            if '.' in name:
                max_len = max(max_len, current_len)
            else:
                # It's a directory, store the cumulative length for its children
                path_len[depth + 1] = current_len
        
        return max_len