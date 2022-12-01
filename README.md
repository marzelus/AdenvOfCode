* Compile requirements

  ``` bash
  pip-compile --output-file requirements.txt requirements.in --no-emit-index-url --no-header --upgrade --rebuild
  ```

* Install dependencies

  ``` bash
  python initVenv.py
  ```
