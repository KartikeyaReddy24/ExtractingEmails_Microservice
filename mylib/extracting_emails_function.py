import time
import random
import re
from mylib.sqs import *
from googlesearch import search
from mylib.variables import *
from mylib.sqs import *



def extract(reciept):
    while True:
        for cell in sqs_queue().receipt:
            print("\nSearching for: ", cell.body)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
            }
            search_value = ""
            for val in cell.body.split():
                search_value += val + "+"

            for i in search(search_value, num_results=1):
                if count > 0 and count % 18 == 0:
                    print(
                        "\n\n\t\t::::::::::: You have now reached maximun Websearches. Please wait :::::::::::\n\n"
                    )
                    time.sleep(360)
                count += 1
                random.uniform(30, 60)
                time.sleep(16)
                LinksCount += 1
                print(
                    f"\n\n\tNo. of Web Searches: {LinksCount}\n\tExtracting Emails in: {i}"
                )
                SearchingFor.append(cell.body)
                LinksSearched.append(i)
                try:
                    time.sleep(18)
                    EMAIL_REGEX = r"-*([\w\-\.]{1,100}@(?!example.com)(?!wixpress.com)(?!email.com)(?!sentry-viewer.wixpress.com)(?!2x.gif)(?!sentry.o2dev.net)(?!2x.png.com)(?!sentry.wixpress.com)(?!sentry-next.wixpress.com)(?!sentry.io)(?!16.14.0.com)(?!aphixsoftware.com)(?:\w[\w\-]+\.)+(?!jpg)(?!png)(?!js)(?!gif)[\w]+)-*"
                    r = requests.get(i, headers=headers)
                    for re_match in re.findall(EMAIL_REGEX, r.text):
                        l.add(re_match)
                        links.add(i)
                        print("\n\t", re_match)
                except:
                    print("\n\tNot Found: ", i)
                    NotFoundLink.add(i)
            cell.delete(QueueUrl=sqs_queue.url, ReceiptHandle=cell.receipt_handle)
            print("\n\n\tThis SQS message is now deleted.")
            time.sleep(10)
