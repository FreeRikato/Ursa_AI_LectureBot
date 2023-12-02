import whisper
import datetime
import warnings

# Suppress warnings about FP16 not being supported on CPU
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

model = whisper.load_model("base")
result = model.transcribe("example.mp3")

# Function to format the time correctly
def format_time(time_delta):
    # Get hours, minutes, seconds and microseconds
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    # Format microseconds to milliseconds with 3 digits
    milliseconds = f"{time_delta.microseconds // 1000:03d}"
    # Return the formatted time string
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds}"

with open('knowledge_base/SRT/output.srt', 'w') as f:
    for i, parameters in enumerate(result["segments"], start=1):
        f.write(str(i) + '\n')
        start_time = datetime.timedelta(seconds=parameters["start"])
        end_time = datetime.timedelta(seconds=parameters["end"])
        f.write(format_time(start_time) + " --> " + format_time(end_time) + '\n')
        f.write(parameters["text"] + '\n\n')

with open('knowledge_base/TXT/output.txt', 'w') as f:
    f.write(result["text"])
