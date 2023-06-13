import os

def load_mozilla_cv(filename, type):
    with open(filename, encoding='utf-8') as f:
        components = [line.strip().split('\t') for line in f][1:]  # First line is the header
        base = os.path.dirname(filename)
        filepaths_and_text = [[os.path.join(base, f'clips/{component[1]}'), component[2], type] for component in components]
    return filepaths_and_text


def load_voxpopuli(filename, type):
    with open(filename, encoding='utf-8') as f:
        lines = [line.strip().split('\t') for line in f][1:]  # First line is the header
        base = os.path.dirname(filename)
        filepaths_and_text = []
        for line in lines:
            if len(line) == 0:
                continue
            file, raw_text, norm_text, speaker_id, split, gender = line
            year = file[:4]
            filepaths_and_text.append([os.path.join(base, year, f'{file}.ogg.wav'), raw_text, type])
    return filepaths_and_text

def load_tsv(filename):
    with open(filename, encoding='utf-8') as f:
        filepaths_and_text = []
        base = os.path.dirname(filename)
        bad_lines = 0
        for line in f:
            components = line.strip().split('\t')
            if len(components) < 2:
                bad_lines += 1
                if bad_lines > 1000:
                    print(f'{filename} contains 1000+ bad entries. Failing. Sample last entry: {line}')
                    raise ValueError
                continue
            filepaths_and_text.append([os.path.join(base, f'{components[1]}'), components[0]])
    return filepaths_and_text