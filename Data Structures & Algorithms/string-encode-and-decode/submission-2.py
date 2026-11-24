class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for voc in strs:
            string = string + str(len(voc)) + "#" + voc
        return string

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            
            str_len = int(s[i:j])
            start = j + 1
            end = start + str_len
            decoded.append(s[start:end])

            i = end

        return decoded