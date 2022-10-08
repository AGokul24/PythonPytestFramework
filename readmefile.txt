Command to run in Chrome
pytest -v -s .\testcases\test_login.py --browser chrome
pytest -v -s .\testcases\test_login.py     (By default)

Command to run in Firefox
pytest -v -s .\testcases\test_login.py --browser firefox

Parallel running:
pytest -v -s -n=2 .\testcases\test_login.py --browser chrome

Generate Pytest HTML report
pytest -v  --html=Reports\report.html .\testcases\test_login.py --browser chrome