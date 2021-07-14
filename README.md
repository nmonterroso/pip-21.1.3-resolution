# pip-21.1.3-resolution

Simple repo demonstrating what I believe to be a problem in the new dependency resolver in pip.

Two libraries that package using `setup.py`:
- `lib/a`
- `lib/b` depends on `lib/a`

And an app (`app/x`) that installs from a `requirements.txt` file. This app depends on both `lib/a` and `lib/b` using relative paths

To see the issue, run:

```
$> docker build . -f app/x/Dockerfile
```

The build will fail with:

```
#11 2.095 INFO: pip is looking at multiple versions of lib-a to determine which version is compatible with other requirements. This could take a while.
#11 2.096 ERROR: Cannot install -r requirements.txt (line 2) and lib-a 0.0.0 (from /pip_resolver/lib/a) because these package versions have conflicting dependencies.
#11 2.096
#11 2.096 The conflict is caused by:
#11 2.096     The user requested lib-a 0.0.0 (from /pip_resolver/lib/a)
#11 2.096     lib-b 0.0.0 depends on lib-a 0.0.0 (from /pip_resolver/lib/a)
#11 2.096
#11 2.096 To fix this you could try to:
#11 2.096 1. loosen the range of package versions you've specified
#11 2.096 2. remove package versions to allow pip attempt to solve the dependency conflict
#11 2.096
#11 2.096 ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/user_guide/#fixing-conflicting-dependencies
```

I don't believe this should be an error because both the dependents point to the same location on the local filesystem. If you do:

```
$> docker build . -f app/x/Dockerfile-legacy
```

The build will succeed. The only difference is that the legacy file uses the `--use-deprecated=legacy-resolver` flag when doing a `pip install`
