class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        stamps = []
        stampReplacement = "?" * len(stamp)
        stampReplacementEscaped = r"\?" * len(stamp)
        stampFillerPattern = re.compile(f"(?!{stampReplacementEscaped})" + "".join(fr"(?:{v}|\?)" for v in stamp))
        while target != "?" * len(target):
            try:
                matchIdx = re.search(stampFillerPattern, target).start()
            except:
                return []
            stamps.append(matchIdx)
            target = target[:matchIdx] + stampReplacement + target[matchIdx + len(stamp):]
        return stamps[::-1]