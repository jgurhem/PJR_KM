import pjr.DBHelper as dh
import pjr.DBRelator as dr
import argparse
import common.parser as cp
import common.properties as prop

parser = argparse.ArgumentParser(parents=[cp.get_common()])
args = parser.parse_args()

filter_dict = dh.convert_filter_list_to_dic(args.filter_list)
con = dh.read_json_file_raw('test.db', args.input)
dh.create_filter(con, 'auto', filter_dict)


for i in prop.CASE_INFO:
  print(i, dh.extract_set(con, i))

