class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove all dashes and convert to uppercase
        cleaned = s.replace('-', '').upper()
        
        # Calculate the length of the first group
        first_len = len(cleaned) % k
        if first_len == 0:
            first_len = k
        
        # Build the result
        result = []
        
        # Add first group
        result.append(cleaned[:first_len])
        
        # Add remaining groups
        for i in range(first_len, len(cleaned), k):
            result.append(cleaned[i:i+k])
        
        # Join with dashes
        return '-'.join(result)