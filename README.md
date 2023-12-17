# Monitor macbook wakeup time
## Painpoint
- Macbook wakes up unexpectedly -> Needs to monitor which time it is active.

## Steps
1. Set cronjob in `cronjob.txt`
2. Run `python3 analytics.py`

## Brainstorming
- Cronjob itself causes wakup? -> No
- Conclusions: Wake up more often when plugging in, but what causes?
- Needs to include tracking processes running right after wake up in log?
- What if on plugged + cronjob running -> wake up? Need to find out!