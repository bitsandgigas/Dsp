# Example usage
file_path = 'your_audio_file.wav'  # Replace with the path to your WAV file
time_series, sample_rate, audio_data = read_wav_file(file_path)

print(f"Sample Rate: {sample_rate}")
print(f"First 10 Time Points: {time_series[:10]}")
print(f"First 10 Audio Data Points: {audio_data[:10]}")