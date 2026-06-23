class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        highest_altitude = current_altitude
        for altitude_gain in gain:
            current_altitude += altitude_gain
            highest_altitude = max(highest_altitude, current_altitude)
        return highest_altitude