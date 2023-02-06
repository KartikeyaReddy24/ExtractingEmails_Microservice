from datetime import datetime
import pandas as pd
import uuid
from mylib.variables import *


websearch = pd.DataFrame(SearchingFor)
searchlinks = pd.DataFrame(LinksSearched)
copying_links = pd.DataFrame(links)
data = pd.DataFrame(l)
NotFounddata = pd.DataFrame(NotFoundLink)
LinksEmails = pd.concat((copying_links, data), ignore_index=True, axis=1)
searchData = pd.concat((websearch, data), ignore_index=True, axis=1)

print("\nLinks Searched\n", copying_links)
print("\nEmail-ID's Collected:\n", data)
print("\nNot Found Links:\n", NotFounddata)
print("\nLinks Searched and Emails Collected:\n", LinksEmails)

currentDateTime = datetime.now()
timestamp = datetime.timestamp(currentDateTime)

file_name = str(uuid.uuid4().hex)
print("\n\t\tThe File name alloted: ", file_name)

with pd.ExcelWriter(str(file_name) + ".xlsx", engine="xlsxwriter") as writer:
    searchData.to_excel(writer, sheet_name="Websearch Cell & Emails")
    searchlinks.to_excel(writer, sheet_name="LinksSearched")
    copying_links.to_excel(writer, sheet_name="UniqueLinksSearched")
    data.to_excel(writer, sheet_name="Emails")
    LinksEmails.to_excel(writer, sheet_name="Links & Emails")
    NotFounddata.to_excel(writer, sheet_name="NotFoundList")
    writer.save()
    print("\n\t\t\tFile saved")
