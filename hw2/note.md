
```shell
conda create -n ml-anaconda-r-python-env python=3.12 r-base anaconda
conda activate ml-anaconda-r-python-env
conda deactivate
R --version
python --version

```

```shell
## install R package
R
```
```R
install.packages("readxl")
install.packages("dplyr")
install.packages("polyreg")
install.packages(c("readxl", "dplyr", "polyreg"))

source("hw2-nonlinear-regression-R.R")
```

```shell
## Run code python
conda activate ml-anaconda-r-python-env

python hw2-nonlinear-regression-python.py
```