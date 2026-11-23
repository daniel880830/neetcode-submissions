class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"[" : "]", "(" : ")", "{" : "}"}
        stack = []
        for ch in s:
            if ch in "[({":
                stack.append(ch)
            elif  ch in "])}":
                if len(stack) == 0:
                    return False
                top = stack.pop()

                if pairs[top] != ch:
                    return False
        return len(stack) == 0
                