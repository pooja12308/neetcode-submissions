class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        st = []

        for i in s:

            # opening brackets
            if i in d:
                st.append(i)

            # closing brackets
            else:
                if not st:
                    return False

                top = st.pop()

                if d[top] != i:
                    return False

        return len(st) == 0