# add-license-for-repo
Add license content for each file in repository recursively.

## Usage

### Step1 Prepare `<LICENSE>` file in current directory named `LICENSE`

### Step2 Edit Parameters

```shell
$ vim add_license_recursively.py

# Edit part 0's parameters according your case
if __name__ == "__main__":
    # 0.init parameters
    repo_root_path = "/home/yuanshuai/code/inferx_model"                                                          
    license_path = "./LICENSE"
    # suffix name with it's comment string for one line
    suffix_dict = {".prototxt":"#", ".c":"//", ".h":"//", ".py":"#"}
```

### Step3 Execute

```shell
$ python ./add_license_recursively.py
```
