class WordsFinder:
    def __init__(self, *file_names: str) -> None:
        self.file_names = file_names

    def get_all_words(self) -> dict[str, list[str, ...]]:
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                data = file.read().lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    data = data.replace(char, ' ')
                all_words[file_name] = data.split()
        return all_words

    def find(self, word: str) -> dict[str, int]:
        all_words = self.get_all_words()
        res = {}
        for file_name, text in all_words.items():
            for index, w in enumerate(text):
                if w == word.lower():
                    res[file_name] = index + 1
                    break
        return res

    def count(self,word: str) -> dict[str, int]:
        all_words = self.get_all_words()
        res = {}
        for file_name, text in all_words.items():
            res[file_name] = text.count(word.lower())
        return res


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
