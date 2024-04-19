rem chrome
pytest -s -v -m "sanity"  TestCases/ --browser chrome


rem firefox

pytest -s -v -m "regression"  TestCases/ --browser firefox