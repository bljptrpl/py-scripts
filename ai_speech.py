# conda install pytorch torchvision torchaudio cpuonly -c pytorch
# https://www.assemblyai.com/blog/end-to-end-speech-recognition-pytorch/
import torchaudio
train_dataset = torchaudio.datasets.LIBRISPEECH("./", url = "train-clean-100", download = True)
test_dataset = torchaudio.datasets.LIBRISPEECH("./", url = "test-clean", download = True)