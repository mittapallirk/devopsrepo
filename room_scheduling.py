import sys
import time

def to_time(t):
    return time.strptime(t, '%H:%M')

def slot_fits(t_from, t_to, slot):
    fr, to, start, end = to_time(t_from), to_time(t_to), to_time(slot[0]), to_time(slot[1])
    return (start <= fr) and (end >= to)


def parse_slots(slots):
    s = iter(slots)
    a = zip(s, s)
    return list(a)


class Room():
    def __init__(self, line):
        parts = line.split(',', 2)
        self.room_num = parts[0]
        self.floor = int(parts[0].split('.')[0])
        self.capacity = parts[1]
        self.available_slots = parse_slots(parts[2].split(','))


def read_rooms():
    with open('rooms.txt', 'r') as f:
        return [Room(line) for line in f.read().rstrip('\n').split(' ')]


def main(_input):
    rooms = read_rooms()
    head_count, floor, t_from, t_to = _input.split(',')

    def floor_distance(room):
        return abs(int(floor) - room.floor)

    rooms = sorted(rooms, key=floor_distance)
    for room in rooms:
        for slot in room.available_slots:
            if slot_fits(t_from, t_to, slot) and head_count <= room.capacity:
                return room.room_num


if __name__ == '__main__':
    print(main(sys.argv[1]))
