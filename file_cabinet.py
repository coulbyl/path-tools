from pathlib import Path
from tools import progress_bar, get_func_exec_time
import sys

dirs = [
    {'Images': (
        '.png', '.jpeg', '.jpg', '.gif', '.pds', '.xcf',
        '.ai', '.cdr', '.tif', '.tiff', '.bmp', '.eps',
        '.raw', '.cr2', '.nef', '.orf', '.sr2'
    )},
    {'Documents': (
        '.pdf', '.txt', '.docx', '.doc', '.json', '.html',
        '.htm', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.ods'
    )},
    {'Videos': ('.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm')},
    {'Musique': ('.mp3', '.aac', '.ogg', '.wav')},
    {'Archives': ('.zip', '.rar', '.gz', '.tar', 'tar.gz')},
    {'Logiciels': ('.exe', '.msi', '.deb')},
]


def get_output_dir(suffix):
    od = [list(d.keys())[0] for d in dirs if suffix in list(d.values())[0]]
    return od[0] if len(od) > 0 else 'Autres'


@get_func_exec_time
def cleaner():
    _path = Path(sys.argv[1])
    _files = [file for file in _path.iterdir() if file.is_file()]

    if len(_files) < 1:
        return print('Aucun fichier trouvé.')

    for file in progress_bar(_files):
        output_path = _path / get_output_dir(file.suffix.lower())
        output_path.mkdir(exist_ok=True)
        file.rename(output_path / file.name)


if __name__ == '__main__':
    try:
        cleaner()
    except NotADirectoryError:
        print("Oops! Votre chemin n'est pas un dossiers")
