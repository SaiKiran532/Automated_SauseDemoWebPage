### For running sanity or regression tests
```commond prompt
> pytest -s -v -m "sanity"  testcases_folder_path/ --browser chrome
```

### For running parallel testcases and generating HTML reports
```commond prompt
>  py.test -s -v -n=2 --html=Reports\report.html --browser chrome

```
