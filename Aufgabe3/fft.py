from wave import open
from winsound import PlaySound, SND_FILENAME as FILE_FLAG
from struct import pack, unpack
from numpy import fft, floor

BLOCK_SIZE = 1000
DELETE = 150
params = ()
frames = []
filter_frames = []

def read_wave_file(filename):
    global params, frames

    wave_file = open(filename, 'r')
    params = wave_file.getparams()

    for i in range(wave_file.getnframes()):
        frame = wave_file.readframes(1)
        frames.append(unpack('<h', frame)[0])

    wave_file.close()


def fourier():
    global frames

    number_blocks = int((len(frames) / BLOCK_SIZE))

    for block in range(number_blocks):
        fourier = fft.fft(frames[block * BLOCK_SIZE: (block + 1) * BLOCK_SIZE])

        delete_minmum(fourier)

        ifourier(fourier)


def delete_minmum(fourier):

    for i in range(DELETE):
        minmum = min(fourier)
        for k in range(len(fourier)):
            if fourier[k] == minmum:
                fourier[k] = 0
                break

    return fourier

def ifourier(fourier):
    global filter_frames

    ifourier = fft.ifft(fourier)

    for i in range(len(ifourier)):
        tmp = pack('<h', int(floor(ifourier[i].real)))
        filter_frames.append(tmp)


def write_wave_file(filename):
    global params, solve
    wave_file = open(filename, 'w')

    wave_file.setparams(params)

    for filter_frame in filter_frames:
        wave_file.writeframesraw(filter_frame)

    wave_file.close()

def play_sound(filename):
	PlaySound(filename, FILE_FLAG)

if __name__ == "__main__":
    filename = 'ceremony.wav'
    output = 'output.wav'

    print("Orignaldatei:")
    play_sound(filename)
    read_wave_file(filename)
    print("Datei eingelesen")
    fourier()
    print("Fouriertransformation")
    write_wave_file(output)
    print("Gefilterte Datei:")
    play_sound(output)