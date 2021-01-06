
class Solution:
    def isValid(self, s: str) -> bool:
        all_parenthesis = []

        for paren in s:
            if paren == '[' or paren == '{' or paren == '(':
                all_parenthesis.append(paren)
            elif paren == ']' and len(all_parenthesis) > 0:
                if all_parenthesis[-1] == '[':
                    all_parenthesis.pop()
                else:
                    all_parenthesis.append(paren)
            elif paren == ')' and len(all_parenthesis) > 0:
                if all_parenthesis[-1] == '(':
                    all_parenthesis.pop()
                else:
                    all_parenthesis.append(paren)
            elif paren == '}' and len(all_parenthesis) > 0:
                if all_parenthesis[-1] == '{':
                    all_parenthesis.pop()
                else:
                    all_parenthesis.append(paren)
            else:
                all_parenthesis.append(paren)

        if len(all_parenthesis) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("]]"))
