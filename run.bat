pytest -v  --html=Reports\reportChrome.html .\testcases --browser chrome
pytest -v  --html=Reports\reportFirefox.html .\testcases --browser firefox
REM pytest -v -n=2 --html=Reports\report.html .\testcases --browser chrome
REM pytest -v -s -n=2 --html=Reports\report.html .\testcases --browser firefox