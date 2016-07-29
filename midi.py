import rtmidi_python as rtmidi
from random import randrange
import sys
import csv


def usage():
    print 'python midi.py [max delay] [trial amount] [trial name] [port name]'

def main():
    if len(sys.argv) < 4:
        usage()
        return

    max_delay = float(sys.argv[1])
    trials = int(sys.argv[2])
    trial_name = sys.argv[3]


    while trials > 0:

        start = raw_input("Start? (y/n)")
        start = start.upper()

        if start == "Y":

            midi_out = rtmidi.MidiOut()


            PORT_NAME = sys.argv[4]
            midi_out.open_port(PORT_NAME)
            value = randrange(0, 127)
            midi_out.send_message([0xb0, 42, value])

            while 1:
                audible = raw_input("Could they hear it? (1/0)")
                audible = audible.upper()

                if audible == '1' or audible == '0':
                    with open(trial_name + '.csv', 'a') as f:
                        write = csv.writer(f)
                        write.writerow([str(round((value/127.0) * max_delay, 3)) + '\n', audible])
                        f.close()
                    break
                else:
                    print "invalid answer"

            trials -= 1

        elif start == "N":
            break
        else:
            continue

if __name__ == '__main__':
    main()