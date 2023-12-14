import numpy as np
from scipy.io import wavfile
import argparse
from playsound import playsound
from colorama import init, Fore, Style
import pyfiglet

init()

def write_data(name, duration, sample_rate, frequency, modulation_rate):
    with open(name.replace('.wav', '_data.txt'), 'w') as file:
        file.write(f"Duration: {duration} seconds\n")
        file.write(f"Sample Rate: {sample_rate} Hz\n")
        file.write(f"Frequency: {frequency} Hz\n")
        file.write(f"Modulation Rate: {modulation_rate} Hz\n")

def generate_tone(args):
    name = args.destination
    duration = args.duration
    sample_rate = args.sample_rate
    frequency = args.frequency
    modulation_rate = args.modulation_rate
    
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    carrier_wave = np.sin(2 * np.pi * frequency * t)

    modulation_wave = np.sin(2 * np.pi * modulation_rate * t)
    modulated_wave = np.sin(2 * np.pi * (frequency + modulation_rate * modulation_wave) * t)
    modulated_wave /= np.max(np.abs(modulated_wave), axis=0)
    wavfile.write(name, sample_rate, np.int16(modulated_wave * 32767))

    print("Modulated signal audio saved correctly.")
    if args.play_audio:
        print(f"\nPlaying '{name}'")
        playsound(name)

    if args.write_data:
        write_data(name, duration, sample_rate, frequency, modulation_rate)
        print("Created data file, correctly")

def main():
    parser = argparse.ArgumentParser(prog="MODULA 0.1",description="Generate modulated audio tones")
    parser.add_argument('-dest','--destination',type=str,default="modulated_audio_signal.wav",help="Destination file name")
    parser.add_argument('-dur','--duration',type=int,default=3,help="Audio duration, in seconds")
    parser.add_argument('-sr','--sample_rate',type=int,default=44100,help="Sample rate in Hz")
    parser.add_argument('-freq','--frequency',type=int,default=440,help="Base frequency in Hz")
    parser.add_argument('-mr','--modulation_rate',type=int,default=12,help="Modulation rate in Hz")
    parser.add_argument('-play','--play_audio',action='store_true',help="Play modulated signal")
    parser.add_argument('-wr','--write_data',action='store_true',help="Create text file with audio data")

    args = parser.parse_args()
    try:
        print(pyfiglet.figlet_format("modula",font="larry3d"))
        generate_tone(args)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "\nUNEXPECTED ERROR: ",str(e) + Fore.RESET + Style.RESET_ALL)

if __name__ == '__main__':
    main()
