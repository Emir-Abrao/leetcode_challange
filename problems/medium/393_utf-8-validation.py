from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_num_bytes(byte):
            # Only consider the least significant 8 bits
            byte = byte & 0xFF
            
            # 1-byte character: 0xxxxxxx
            if (byte >> 7) == 0:
                return 1
            # 2-byte character: 110xxxxx
            elif (byte >> 5) == 0b110:
                return 2
            # 3-byte character: 1110xxxx
            elif (byte >> 4) == 0b1110:
                return 3
            # 4-byte character: 11110xxx
            elif (byte >> 3) == 0b11110:
                return 4
            else:
                return -1
        
        def is_continuation_byte(byte):
            # Continuation byte: 10xxxxxx
            byte = byte & 0xFF
            return (byte >> 6) == 0b10
        
        i = 0
        while i < len(data):
            num_bytes = get_num_bytes(data[i])
            
            # Invalid starting byte
            if num_bytes == -1:
                return False
            
            # Check if we have enough bytes left
            if i + num_bytes > len(data):
                return False
            
            # Check continuation bytes
            for j in range(1, num_bytes):
                if not is_continuation_byte(data[i + j]):
                    return False
            
            i += num_bytes
        
        return True