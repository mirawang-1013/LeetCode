class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # if isinstance(paths, builtins.str):
        #     paths = [paths]
        
        content_map = defaultdict(list)

        for info in paths:
          parts = info.split()  
          dir_path = parts[0]
          for fp in parts[1:]:
             if '(' not in fp or not fp.endswith(')'):
                    continue   
             name, content = fp.split('(', 1)
             content = content[:-1] 
             content_map[content].append(f"{dir_path}/{name}")
        result = list(content_map.values())
        return [v for v in result if len(v)>1]