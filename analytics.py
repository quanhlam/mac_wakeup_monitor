import sys
import math
from datetime import datetime, timedelta

def is_considered_continuous(seconds, variations=2):
  return seconds >= 60 - variations  and seconds <= 60 + variations

def get_continuous_segments(lst_times, variations=2):
  segments = []
  _cur_cont_segment = []
  for tr in lst_times:
      if not _cur_cont_segment:
        _cur_cont_segment.append(tr)
      elif is_considered_continuous((tr - _cur_cont_segment[-1]).total_seconds(), variations):
        _cur_cont_segment.append(tr)
      else:
        segments.append(_cur_cont_segment)
        _cur_cont_segment = []
  
  if _cur_cont_segment:
      segments.append(_cur_cont_segment)
  return segments


def to_human_readable(lst_segments):
  lst_text = []
  for segment in lst_segments:
      _start = segment[0].strftime("%d/%m %H:%M:%S")
      _end = segment[-1].strftime("%d/%m  %H:%M:%S")
      secs_diff = (segment[-1] - segment[0]).total_seconds()

      txt = ""
      desc = ""
      if secs_diff < 60 * 60:
        desc = f"{round(secs_diff/(60))} minutes"
      else:
        desc = f"{round(secs_diff/(60*60))} hours"
      if len(segment) > 1:
        if _start.split()[0] == _end.split()[0]:
          txt = f"{_start} -> {_end.split()[1]}"
        else:
          txt = f"{_start} -> {_end}"
      else:
        txt = _start

      if secs_diff >= 120:
        txt += f" ({desc})"

      lst_text.append(txt)
  return lst_text

def get_variation_input():
  if len(sys.argv) > 1:
      return int(sys.argv[1])
  return None


if __name__ == '__main__':

  # Input
  file = "/Users/Quan_Lam/repos/personal/automations/time-track.log"
  #start_time = "2023-12-16 00:00:00"
  #end_time = "2023-12-18 00:00:00"
  #_start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
  #_end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
  _start = datetime.now() - timedelta(days=1)
  _end = datetime.now()


  f = open(file, "r+")

  try:
    variation = get_variation_input()
    lines = f.readlines()
    fmt_lines = map(lambda x: datetime.strptime(x.strip(), "%d/%m/%Y %H:%M:%S"), lines) 
    time_range = filter(lambda x: x >= _start and x < _end, fmt_lines)
    continuous_segments = get_continuous_segments(time_range, variation if variation else 2)
    display_text_lst = to_human_readable(continuous_segments)
    print(f"=== Activities in the last {math.floor((_end-_start).total_seconds()/3600)} hours ===")
    for text in display_text_lst:
        print(text)

  except Exception as e:
    f.close()
    raise e
  finally:
    f.close()


