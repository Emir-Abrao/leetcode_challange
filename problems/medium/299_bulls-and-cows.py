class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        # Since digits are only '0'-'9', we can use fixed-size lists.
        secret_count = [0] * 10
        guess_count = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[int(s)] += 1
                guess_count[int(g)] += 1

        cows = 0
        for d in range(10):
            cows += min(secret_count[d], guess_count[d])

        return f"{bulls}A{cows}B"