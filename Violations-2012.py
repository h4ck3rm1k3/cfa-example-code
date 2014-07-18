#Your program should calculate the number of violations in each category, and the earliest and latest violation date for each category.

import csv
import time 

class Violation :

    VIOLATION_ID=0
    INSPECTION_ID=1
    VIOLATION_CATEGORY=2
    VIOLATION_DATE=3
    VIOLATION_DATE_CLOSED=4
    VIOLATION_TYPE=5

    def __init__(self, filename):
        self.filename=filename
        self.stats = {}

    def proc(self, row):
        """
        process the category
        """
        cat = row[self.VIOLATION_CATEGORY]
        date_str = row[self.VIOLATION_DATE]
        date= time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
  
        if cat not in self.stats :
            self.stats[cat]={
                'first': date, 
                'last': date
            }
        else:

            existing_first = self.stats[cat]['first']
            if time.mktime(date) < time.mktime(existing_first) :
                print 'Before', date, existing_first
                self.stats[cat]['first']=date
            else:
                #print 'not Before',time.asctime(date), time.asctime(existing_first)
                pass


            existing_last = self.stats[cat]['last']
            #print time.asctime(date),time.asctime(existing_last)
            #print time.mktime(date),time.mktime(existing_last)

            date_epoch = time.asctime(date)
            last_epoch = time.asctime(existing_last)

            if date_epoch > last_epoch :
                #print 'last', time.asctime(existing_last),time.asctime(date)
                self.stats[cat]['last']=date
            else:
                #print 'not after', date, existing_last
                pass

    def report(self) :
        with open('report.csv', 'wb') as csvfile:
            fwriter= csv.writer(csvfile, delimiter=',', quotechar='\"')
            fwriter.writerow(['category','first','last'])
            for x in sorted(self.stats):
                fwriter.writerow([x,time.asctime(self.stats[x]['first']),time.asctime(self.stats[x]['last'])])
        
    def read(self):
        """
        Read the file named by self.filename and call proc on each row
        """

        with open(self.filename, 'rb') as csvfile:
            freader= csv.reader(csvfile, delimiter=',', quotechar='\"')
            for row in freader:
                if row[0]=='violation_id':
                    pass
                else:
                    #print '|'.join)(row
                    self.proc(row)
def main():
    v = Violation('Violations-2012.csv')
    v.read()
    v.report()

if __name__ == "__main__": 
    main() 
