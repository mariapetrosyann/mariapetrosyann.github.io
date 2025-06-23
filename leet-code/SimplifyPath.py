class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        new_path = []
        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if new_path:
                    new_path.pop()
            else:
                new_path.append(part)
        file_path = '/'+'/'.join(new_path)
        return file_path
