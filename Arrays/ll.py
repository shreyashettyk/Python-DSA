# https://leetcode.com/problems/determine-if-two-events-have-conflict/description/
# https://leetcode.com/problems/determine-if-two-events-have-conflict/post-solution/?submissionId=1002276234


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        time_1 = []
        time_2 = []
        for time in event1:
            times = time.split(":")
            times = int(''.join(times))
            time_1.append(times)
        for time in event2:
            times = time.split(":")
            times = int(''.join(times))
            time_2.append(times)

        # ["01:15","02:00"],["02:00","03:00"]
        if time_2[0] >= time_1[0] and time_2[0] <= time_1[1]:
            return True
        # ["16:53","19:00"],["10:33""18:15"]
        elif time_2[1] >= time_1[0] and time_2[1] <= time_1[1]:
            return True
        elif time_2[0] < time_1[0] and time_2[1] > time_1[1]:  # [15:19,17:56],[14:11,20:02]
            return True
        else:
            return False

        del time_1, time_2