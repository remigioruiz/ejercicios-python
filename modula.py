import numpy as np
from scipy.io import wavfile
import argparse
from playsound import playsound

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
    

def main():
    parser = argparse.ArgumentParser(prog="MODULA 0.1",description="Generate modulated audio tones")
    parser.add_argument('-dest','--destination',type=str,default="modulated_audio_signal.wav",help="Destination file name")
    parser.add_argument('-dur','--duration',type=int,default=3,help="Audio duration, in seconds")
    parser.add_argument('-sr','--sample_rate',type=int,default=44100,help="Sample rate in Hz")
    parser.add_argument('-freq','--frequency',type=int,default=440,help="Base frequency in Hz")
    parser.add_argument('-mr','--modulation_rate',type=int,default=12,help="Modulation rate in Hz")
    parser.add_argument('-play','--play_audio',action='store_true',help="Play modulated signal")

    args = parser.parse_args()
    generate_tone(args)

if __name__ == '__main__':
    main()
