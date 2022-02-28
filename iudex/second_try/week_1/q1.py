import sys


class Music:
    def __init__(self, id, time):
        self.id = id
        self.time = time
        self.next = 0
        self.before = 0


class Queue:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.total_musics = 0

    def add_music(self, music_added):
        if self.total_musics == 0:
            self.start = music_added
            self.end = music_added
        else:
            music_added.before = self.end
            self.end.next = music_added
            self.end = music_added

        self.total_musics += 1

    def remove_music(self):
        music_to_remove = self.start

        if(self.total_musics == 1 or self.total_musics == 0):
            self.start = 0
            self.end = 0
        else:
            music_to_remove.next.before = 0
            self.start = music_to_remove.next

        self.total_musics -= 1

    def pause_music(self, time):
        music_to_pause = self.start

        if(self.total_musics > 1):
            music_to_pause.next.before = 0
            self.start = music_to_pause.next

        music_to_pause.time -= time

        self.end.next = music_to_pause
        music_to_pause.next = 0
        music_to_pause.before = self.end

        self.end = music_to_pause

    def play(self, time_to_play):
        while(time_to_play > 0):
            if self.total_musics == 0:
                print('A linha possui {} programas.'.format(self.total_musics))
                return

            music_to_play = self.start
            music_time = music_to_play.time

            if(time_to_play >= music_time):
                self.remove_music()
                print(
                    'O programa {} executou por {} segundos.'.format(music_to_play.id, music_time))
                print(
                    'O programa {} terminou.'.format(music_to_play.id))
                time_to_play -= music_time
            else:
                self.pause_music(time_to_play)
                print(
                    'O programa {} executou por {} segundos.'.format(music_to_play.id, time_to_play))
                time_to_play = 0

        print(
            'A linha possui {} programas.'.format(self.total_musics))


def main():
    queue = Queue()

    for line in sys.stdin:
        if('ADD' in line):
            [_, id, time_string] = line.split(' ')
            time = int(time_string)

            new_music = Music(id, time)

            queue.add_music(new_music)

            print('O programa {} foi agendado com sucesso!'.format(id))

        if('EXE' in line):
            [_, time_to_execute_string] = line.split(' ')
            time_to_execute = int(time_to_execute_string)

            queue.play(time_to_execute)


if __name__ == '__main__':
    main()
