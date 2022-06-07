from selenium import webdriver
import time
import smtplib

url = "https://sa.ucla.edu/ro/ClassSearch/Results/ClassDetail?term_cd=20S&subj_area_cd=STATS%20%20&crs_catlg_no=0100A%20%20%20&class_id=263303200&class_no=%20001%20%20/"

closedText = "Closed: Class Full"
titleLine = "            <title>Class Detail - Class Detail</title>"
smtpOut = "put your email addr here"
smtpPass = "and your password"
toaddrs = "eg phonenumber@vtext.com"

chromeBrowser = webdriver.Chrome()
chromeBrowser.get(url)

while True:
    chromeBrowser.refresh()
    source = chromeBrowser.page_source
    htmlLines = source.split('\n')
    foundClosed = False
    print('page refreshed')
    if titleLine in htmlLines:
        print('found title text')
        for line in htmlLines:
            if line.find(closedText):
                foundClosed = True
        if foundClosed:
            print('Stats100A is CLOSED')
            time.sleep(15) #look again in 15 seconds
        else:
            print('Stats100A is OPEN')
            msg = "Subject: Stats has space, enroll!"

            server = smtplib.SMTP('smtp.charter.net', 25)
            server.starttls()
            server.login(smtpOut, smtpPass)

            print('From: ' + smtpOut)
            print('To: ' + str(toaddrs))
            print('Message: ' + msg)

            server.sendmail(smtpOut, toaddrs, msg)
            server.quit()
            time.sleep(60) #send again in one minute
    else:
        time.sleep(30) #incorrect page, wait 30
