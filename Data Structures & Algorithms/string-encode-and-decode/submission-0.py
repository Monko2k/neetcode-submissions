class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            strlen = str(len(item))
            res += strlen + '|' + item
        return res


    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        meta = True
        strlen = 0
        cursor = 0
        seek = 0
        seekStr = ""
        while cursor < len(s):
            c = s[cursor]
            if meta:
                if c == '|':
                    meta = False
                    seek = int(seekStr)
                    if seek == 0:
                        res.append("")
                        meta = True
                    seekStr = ""
                else:
                    seekStr += (c)
                cursor += 1
            else:
                print(cursor)
                print(cursor + seek)
                res.append(s[cursor:cursor + seek])
                meta = True
                cursor = cursor + seek
        return res




