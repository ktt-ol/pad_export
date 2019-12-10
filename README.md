# pad_export

Exports the text content of the last X pads to a local git repository.

## Install

**venv**

```shell script
sudo apt install python3-venv python3-pip git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

**cron**

```shell script
$SCRIPT/venv/bin/python $SCRIPT/export_pads.py > $SCRIPT/lastrun.log 2>&1
```
