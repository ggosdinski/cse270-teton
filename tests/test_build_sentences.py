import pytest
import json
from unittest.mock import mock_open, patch
from build_sentences import (
    get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
    get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures
)

def test_get_seven_letter_word(mocker):
    mocker.patch("builtins.input", return_value="example")
    assert get_seven_letter_word() == "EXAMPLE"
    
    mocker.patch("builtins.input", return_value="short")
    with pytest.raises(ValueError):
        get_seven_letter_word()

def test_parse_json_from_file():
    mock_data = '{"adjectives": ["big", "small"], "nouns": ["cat", "dog"]}'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = parse_json_from_file("dummy.json")
    assert data["adjectives"] == ["big", "small"]
    assert data["nouns"] == ["cat", "dog"]

def test_choose_sentence_structure():
    structure = choose_sentence_structure()
    assert structure in structures

def test_get_pronoun():
    assert get_pronoun() in ["he", "she", "they", "I", "we"]

def test_get_article():
    assert get_article() in ["a", "the"]

def test_get_word():
    sample_list = ["apple", "banana", "cherry"]
    assert get_word("A", sample_list) == "apple"
    assert get_word("B", sample_list) == "banana"
    assert get_word("C", sample_list) == "cherry"

def test_fix_agreement():
    sentence = ["he", "quickly", "run", "a", "orange", "apple"]
    fix_agreement(sentence)
    assert sentence == ["he", "quickly", "runs", "an", "orange", "apple"]

def test_build_sentence():
    mock_data = {
        "adjectives": ["big", "small", "red", "blue", "tall", "short", "bright"],
        "nouns": ["cat", "dog", "fish", "bird", "tree", "house", "car"],
        "verbs": ["run", "jump", "swim", "fly", "climb", "sit", "stand"],
        "adverbs": ["quickly", "slowly", "silently", "loudly", "gracefully", "awkwardly", "boldly"],
        "prepositions": ["on", "in", "under", "over", "beside", "behind", "near"]
    }
    
    assert len(structures) > 0, "La lista structures está vacía o no definida"
    
    sentence = build_sentence("ABACABA", structures[0], mock_data)
    assert isinstance(sentence, str)
    assert len(sentence) > 0
