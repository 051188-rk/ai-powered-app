import pytest
from utils.groq_client import GroqClient
from utils.gemini_client import GeminiClient
from models.config import Config

def test_config_loads():
    cfg = Config.load()
    assert 'GEMINI_MODEL' in cfg

def test_groq_client_init():
    # this test will skip if groq not installed
    try:
        GroqClient(api_key='dummy')
    except RuntimeError:
        pytest.skip('groq not installed in test env')

def test_gemini_client_init():
    try:
        GeminiClient(api_key='dummy')
    except RuntimeError:
        pytest.skip('google.generativeai not installed')
