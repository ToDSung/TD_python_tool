from datetime import timedelta, datetime

# 注意 end_date 不會被遞迴到
def iterate_date(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
  

def covert_string_to_datetime(input_string, input_format, calc_timezone_hour=0):
    formated_datetime = datetime.strptime(input_string, input_format) + timedelta(hours = calc_timezone_hour)
    return formated_datetime

def covert_datetime_to_string(input_datetime, output_format, calc_timezone_hour=0):
    input_datetime = input_datetime + timedelta(hours = calc_timezone_hour)
    formated_string = datetime.strftime(input_datetime, output_format)
    return formated_string

if __name__ == '__main__':
    # 使用範例      
    start_date = covert_string_to_datetime('20190908', '%Y%m%d', 8)
    end_date = covert_string_to_datetime('20190910', '%Y%m%d', 8)
    print(start_date)
    print(end_date)
    for single_date in iterate_date(start_date, end_date):
        print(covert_datetime_to_string(single_date, '%Y/%m/%d-%H:%M:%S', -8))
        # print(covert_datetime_to_string(single_date, '%Y%m%d'))
    