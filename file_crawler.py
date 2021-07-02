import sys
from pathlib import Path
from tools import human_readable, progress_bar, get_func_exec_time
from datetime import datetime


class FileCrawler:
    _directories: int = 0
    _files: int = 0
    _hidden_files: int = 0
    _total_size: int = 0
    _stats_link = "\x1b]8;;file://./crawls-stats.txt/\acrawls-stats.txt\x1b]8;;\a"
    _path = Path(sys.argv[1])

    @classmethod
    def _save_path_info(cls) -> None:
        lines = [
            f'\n----- In your {cls._path} path, you have:\n',
            f'* {human_readable(cls._directories)} directories\n',
            f'* {human_readable(cls._files)} files\n',
            f'* {human_readable(cls._hidden_files)} hidden files\n',
            f'Total size: {human_readable(cls._total_size, is_file_sys=True)}\n',
            f'Information generated on {datetime.today()}\n'
        ]
        with open('crawls-stats.txt', 'a+', encoding='utf8') as file:
            file.writelines(lines)

    @classmethod
    def _update_hidden_files(cls, path: Path) -> None:
        if path.is_file() and path.name.startswith('.'):
            cls._hidden_files += 1

    @classmethod
    def _update_files(cls, path: Path) -> None:
        if path.is_file():
            cls._files += 1

    @classmethod
    def _update_directories(cls, path: Path) -> None:
        if path.is_dir():
            cls._directories += 1

    @classmethod
    def _update_path_info(cls, path: Path) -> None:
        if path.exists():
            cls._total_size += path.stat().st_size
            cls._update_directories(path)
            cls._update_files(path)
            cls._update_hidden_files(path)

    @classmethod
    @get_func_exec_time
    def fetch_info(cls) -> None:
        if not cls._path.exists() or not cls._path.is_absolute() or not cls._path.is_dir():
            return print('The path must exist, must be absolute and must be a directory.')

        print('\nLoading files...\n')

        try:
            for path in progress_bar(list(cls._path.glob('**/*'))):
                cls._update_path_info(path)
        except (PermissionError, OSError):
            print("\n\n🤕️ Due to system errors, the process was interrupted.")

        cls._save_path_info()

        print('\n🤗️ Ctrl+click on ->', cls._stats_link, 'to display info.', '\n')


if __name__ == '__main__':
    try:
        FileCrawler.fetch_info()
    except IndexError:
        print('[command-error]: $ python file_crawler.py your_path')
