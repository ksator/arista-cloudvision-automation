**Table of Contents**

- [About YANG](#about-yang)
- [Generate a tree representation of a YANG module for quick visualization](#generate-a-tree-representation-of-a-yang-module-for-quick-visualization)
  - [Get some YANG modules](#get-some-yang-modules)
  - [Pyang](#pyang)
    - [Requirements](#requirements)
      - [Install Pyang](#install-pyang)
      - [Update the PATH env variable to use pyang](#update-the-path-env-variable-to-use-pyang)
    - [Useful Links](#useful-links)
    - [Generate a tree representation of a YANG module](#generate-a-tree-representation-of-a-yang-module)
  - [gNMIc](#gnmic)
    - [Requirements](#requirements-1)
    - [Useful Links](#useful-links-1)
    - [Generate paths from a YANG module](#generate-paths-from-a-yang-module)
    - [Generate a tree representation of a YANG module](#generate-a-tree-representation-of-a-yang-module-1)

# About YANG

YANG is a data-model language defined by the IETF to model:

- The device configuration known as configuration data (writable data)
- The operational state known as state data (read-only status)

YANG determines the structure and syntax of the data.

The data model written in YANG are defined in YANG modules.

YANG modules can be categorized as:

- IETF defined YANG modules. Example: https://tools.ietf.org/html/draft-ietf-ospf-yang-29
- OpenConfig defined YANG modules. Published on https://github.com/openconfig/public/tree/master/release/models
- Network vendor defined YANG modules. Example: EOS data models https://github.com/aristanetworks/yang

YANG RFCs:

- https://tools.ietf.org/html/rfc6020 (YANG)
- https://tools.ietf.org/html/rfc7950 (YANG 1.1)

# Generate a tree representation of a YANG module for quick visualization

## Get some YANG modules

Before to use Pyang or gNMIc, let's get some YANG modules.  

The YANG modules defined by OpenConfig are published on this repository https://github.com/openconfig/public/tree/master/release/models  
Let's copy all the YANG files from the OpenConfig repository to a local directory

```bash
mkdir yang_modules
git clone https://github.com/openconfig/public.git
cp public/release/models/*.yang yang_modules/.
cp -R public/release/models/*/*.yang yang_modules/.
cp public/third_party/ietf/*.yang yang_modules/.
cd yang_modules/
ls
```

## Pyang

We can use Pyang to generate a tree representation of YANG models for quick visualization.

### Requirements

#### Install Pyang

Install Pyang on your automation setup

```bash
pip install pyang
```

```bash
pip list
```

#### Update the PATH env variable to use pyang

```bash
ls -l /home/arista/.local/bin/
echo $PATH
echo $HOME
export PATH="$HOME/.local/bin:$PATH"
echo $PATH
```

### Useful Links

pyang source code https://github.com/mbj4668/pyang

### Generate a tree representation of a YANG module

```bash
pyang openconfig-interfaces.yang -f tree
pyang openconfig-interfaces.yang -f tree --tree-path=/interfaces/interface/state
pyang openconfig-interfaces.yang -f tree --tree-depth=4
```

## gNMIc

gNMIc is a gNMI client.  
It can also be used to generate paths and tree representation from YANG modules. 

### Requirements

Install gNMIc on your automation setup

```bash
bash -c "$(curl -sL https://get-gnmic.kmrd.dev)"
```

```bash
gnmic version
gnmic help
```

### Useful Links

gNMIc documentation https://gnmic.kmrd.dev/  
gNMIc source code https://github.com/karimra/gnmic

### Generate paths from a YANG module

```bash
gnmic generate path --file openconfig-interfaces.yang --state-only
gnmic generate path --file openconfig-interfaces.yang --types
```

### Generate a tree representation of a YANG module

```bash
gnmic generate --file openconfig-interfaces.yang
gnmic generate --file openconfig-interfaces.yang --json 
```
