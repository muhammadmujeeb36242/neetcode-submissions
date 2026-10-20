class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + "#" + s)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter separating length and string
            while s[j] != "#":
                j += 1

            # Extract the length
            length = int(s[i:j])

            # Extract the string
            start = j + 1
            decoded.append(s[start:start + length])

            # Move to the next encoded string
            i = start + length

        return decoded