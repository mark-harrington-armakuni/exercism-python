from exercises.grep import grep_from_files

def test_grep_string_match_single_file():
  assert grep_from_files("hello", ["input.txt"]) == ["hello", "hello again"]

def test_grep_string_match_mutiple_files():
  assert grep_from_files("hello", ["input.txt", "other_input.txt"]) == ["input.txt:hello", "input.txt:hello again", "other_input.txt:hello world", "other_input.txt:hello python"]

def test_grep_regex_match_numbers_single_file():
  assert grep_from_files("[0-9]", ["input.txt"]) == ["123"]

def test_grep_regex_match_numbers_mutiple_files():
  assert grep_from_files("[0-9]", ["input.txt", "other_input.txt"]) == ["input.txt:123", "other_input.txt:456"]

def test_grep_regex_match_uppercase_single_file():
  assert grep_from_files("[A-Z]", ["input.txt"]) == ["Uppercaseone"]

def test_grep_regex_match_uppercase_mutiple_files():
  assert grep_from_files("[A-Z]", ["input.txt", "other_input.txt"]) == ["input.txt:Uppercaseone", "other_input.txt:Uppercasetwo"]
