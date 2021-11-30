# lgtv_rs232
This library helps to communicate with LG TV over RS-232. Tested on LX95 series.


### Installation
```bash
pip install lgtv-rs232
```


### Usage
```python
from lgtv_rs232 import LgTvRs232Client, Power


port = "/tty/USB0"


async def power_on_tv():
    client = LgTvRs232Client(port)
    current_state = await client.power.get_state()
    
    if current_state == Power.OFF:
        await client.power.on()
    
    client.close()
```
