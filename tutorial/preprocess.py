import os

bash_script = 'preprocess.sh'

def convert_audio(file_in, file_out):
    """
    preprocess using ffmpeg in .sh
    :param: file_in: path/to/sound.mp3(.wav, mpeg)
    :param: file_out: file_out: path/to/sound.wav (8000)
    """
    # check input file
    if not os.path.exists(file_in):
        raise Exception('File ERROR')
        
    _, file_extension = os.path.splitext(file_in)
    if not file_extension in ['.mp3', '.wav', '.mpeg', '.flac']:
        raise Exception('File ERROR')

    # check dir_out exists
    if not os.path.exists(os.path.split(file_out)[0]):
        raise Exception('Dir_out does not exists {}'.format(os.path.split(file_out)[0]))
    
    command = 'sh ' + bash_script + ' ' + file_in + ' ' + file_out  
    os.system(command)

    while not os.path.exists(file_out):
        continue


def preprocess(file_in, logging=None):
    """
    :param file_in: test_sounds/test.mp3
    :return: preprocessed/test.wav
    """
    # create preprocessed file_name.wav
    file_name = os.path.split(file_in)[1]               # ('test_sounds', 'test.mp3')
    file_name, _ = os.path.splitext(file_name)          # ('test' , '.mp3')
    if not os.path.exists('preprocessed'):              # если такой папки нет
        os.makedirs('preprocessed')                     # то создадим ее
    new_wav_path = 'preprocessed/' + file_name + '.wav'

    logging.info('----------- Preprocess... -----------')
    convert_audio(file_in=file_in, file_out=new_wav_path)
    logging.info('---------- Preprocess Done ----------')
    return new_wav_path


def check_sound_file(file_path):
    file_name = os.path.split(file_path)[1]                   # ('test_sounds', 'test.mp3')
    _, file_ext = os.path.splitext(file_name)                 # ('test' , '.mp3')

    return os.path.exists(file_path) and file_ext in ['.wav', '.mp3', '.mpeg', '.flac']
