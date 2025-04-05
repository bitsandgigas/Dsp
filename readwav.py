from scipy.io import wavfile

def read_wav_file(file_path,maxV):
    # Read the sample rate and audio data
    sample_rate, audio_data = wavfile.read(file_path)
    
    # Create the time series
    time_series = [i / sample_rate for i in range(len(audio_data))]
    audio_data = audio_data*maxV;
    return time_series, sample_rate, audio_data

