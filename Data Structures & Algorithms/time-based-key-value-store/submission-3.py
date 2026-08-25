class TimeMap:

    

    def __init__(self):

        self.keymap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keymap.keys():
            self.keymap[key] = []
        
        self.keymap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keymap:
            return ""
        else:
            search_list = self.keymap[key]

            if len(search_list) == 0:
                return None
            l = 0
            r = len(search_list) - 1

            while l <= r:

                m = (l + r) // 2

                if search_list[m][1] == timestamp:
                    return search_list[m][0]
                elif search_list[m][1] < timestamp:
                    l = m + 1
                elif search_list[m][1] > timestamp:
                    r = m - 1
            
            if l in range(0, len(search_list)) and search_list[l][1] < timestamp:
                return search_list[l][0]
            elif r in range(0, len(search_list)) and search_list[r][1] < timestamp:
                return search_list[r][0]
            return ""
        
        
