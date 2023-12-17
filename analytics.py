from datetime import datetime, timedelta


def is_considered_continuous(seconds, variations = 2):
  return seconds >= 60 - variations  and seconds <= 60 + variations

def get_continuous_segments(lst_times):
  segments = []
  _cur_cont_segment = []
  for tr in lst_times:
      if not _cur_cont_segment:
        _cur_cont_segment.append(tr)
      elif is_considered_continuous((tr - _cur_cont_segment[-1]).total_seconds()):
        _cur_cont_segment.append(tr)
      elif (tr - _cur_cont_segment[-1]).total_seconds() > 1:
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
      if len(segment) > 1:
        if _start.split()[0] == _end.split()[0]:
          lst_text.append(f"{_start} -> {_end.split()[1]}")
        else:
          lst_text.append(f"{_start} -> {_end}")
      else:
        lst_text.append(_start)
  return lst_text


if __name__ == '__main__':

  # Input
  file = "time-track.log"
  start_time = "2023-12-17 00:00:00"
  end_time = "2023-12-18 00:00:00"

  f = open(file, "r+")

  _start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
  _end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

  try:
    lines = f.readlines()
    fmt_lines = map(lambda x: datetime.strptime(x.strip(), "%d/%m/%Y %H:%M:%S"), lines) 
    time_range = filter(lambda x: x >= _start and x < _end, fmt_lines)
    continuous_segments = get_continuous_segments(time_range)
    display_text_lst = to_human_readable(continuous_segments)
    for text in display_text_lst:
        print(text)

  except Exception as e:
    f.close()
    raise e
  finally:
    f.close()


