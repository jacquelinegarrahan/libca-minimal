# libca-minimal
Minimal example using pytest, p4p, pcaspy, and pyepics for demonstrating issues with libca and pytest. In this case, the pcaspy server is launched in a pytest fixture as a subprocess. The test attempts to read a value from the server.  Running tests with pytest yields the following issues:  
1. No import of p4p leads to seg fault.  
2. Pyepics unable to access pvs using packaged libca. Using epicscorelib libca corrects issue.  

## setup
The environment for this test can be built using conda:  

```
$ conda env create -f environment.yml
```

And activated:
```
$ conda activate libca-minimal
```

### running

I have included a small script to demonstrate that this only occurs with pytest:

In one terminal window:  
```
$ python run_server.py
```

In another:  
```
$ python without_pytest.py
```

This example will work regardless of whether the `PYEPICS_LIBCA` variable is manipulated.  

The test issues can be replicated by running:

```
$ pytest .
```

Issue 1 can be demonstrated by commenting out the p4p import. Issue 2 can be demonstrated by commenting out the `PYEPICS_LIBCA` definition.