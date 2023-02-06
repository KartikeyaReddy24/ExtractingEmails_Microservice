from mylib.sqs import *


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


print("\n------------------------------- DATA SAVED -------------------------------\n")

print(
    "\n\t----------- Time Taken For Execution: %s  -----------\n\n"
    % (convert(time.time() - start_time))
)
