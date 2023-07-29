import os


class Lister:
    def __init__(self, debug=False):
        self._tail = []
        self._ignore_folders_files = []
        self._get_git_ignore()
        self._debug = debug
        self._console = ""

    def list_folders_and_files(self, root='.', deep=0):
        ls = os.listdir(root)
        ls = list(filter(lambda x: x not in self._ignore_folders_files, ls))

        self._tail.append(1)
        for key, item in enumerate(ls):
            pre = ['|\t' if _ == 1 else '\t' for _ in self._tail[:-1]]
            pre = ''.join(pre)

            if key + 1 == len(ls):
                output = pre + '└── ' + item + '\n'
                self._tail[deep] = 0
            else:
                output = pre + '├── ' + item + '\n'
            self._console += output

            if self._debug:
                print(output, end='')

            if os.path.isdir(os.path.join(root, item)):
                self.list_folders_and_files(root=os.path.join(root, item), deep=deep + 1)
                self._tail = self._tail[:-1]

    def _get_git_ignore(self):
        if os.path.exists('.gitignore'):
            with open('.gitignore') as f:
                ignore_folders_files = f.readlines()
                ignore_folders_files = filter(lambda x: x != '\n', ignore_folders_files)
                ignore_folders_files = [x.replace('\n', '') for x in ignore_folders_files]
            ignore_folders_files.append('.gitignore')
            ignore_folders_files.append('.git')
            self._ignore_folders_files = ignore_folders_files
        self._ignore_folders_files.append(os.path.basename(__file__))

    def dump(self, path='structure.md'):
        with open(path, 'w', encoding='UTF-8') as f:
            f.write('```\n')
            f.write(self._console)
            f.write('```')


if __name__ == "__main__":
    lister = Lister()
    lister.list_folders_and_files()
    lister.dump()
