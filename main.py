#import libraries for graphing and reading csv files
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

#define variables for easy reference
numi = []
numc = []
nums = []
numj = []
totals = []
mon = ["February", "March", "April"]
cou = ["India", "China", "Singapore", "Japan"]
feb = mar = apr = 0

#open csv file
with open("cases.csv") as cases:
  data = csv.DictReader(cases)
  #read data
  for i in data:
    # collect india data
    if i["Country/Region"] == "India":
      numi.append(int(i["2/1/20"]))
      numi.append(int(i["3/1/20"]))
      numi.append(int(i["4/1/20"]))

    #collect singapore data
    if i["Country/Region"] == "Singapore":
      nums.append(int(i["2/1/20"]))
      nums.append(int(i["3/1/20"]))
      nums.append(int(i["4/1/20"]))

    #collect japan data
    if i["Country/Region"] == "Japan":
      numj.append(int(i["2/1/20"]))
      numj.append(int(i["3/1/20"]))
      numj.append(int(i["4/1/20"]))

    #collect china data
    if i["Country/Region"] == "China":
      #add up data from provinces
      feb += int(i["2/1/20"])
      mar += int(i["3/1/20"])
      apr += int(i["4/1/20"])
  #store final totals for china
  numc = [feb, mar, apr]

#array for current number of cases
totals = [numi[2], numc[2], nums[2], numj[2]]

#line graph of monthly number of cases
plt.figure()
plt.plot(mon, numi, color= 'b')
plt.plot(mon, nums, color= 'r')
plt.plot(mon, numj, color= 'c')
plt.title("COVID-19 Monthly Trends in Asia")
plt.xlabel("Months")
plt.ylabel("Number of cases")
plt.savefig("monthly-trends.png")

#line graph of monthly number of casesin China
plt.figure()
plt.plot(mon, numc, color= 'g')
plt.title("COVID-19 Trends in China")
plt.xlabel("Months")
plt.ylabel("Number of cases")
plt.savefig("china-trend.png")

#bar graph of current cases
plt.figure()
plt.bar(cou, totals)
plt.title("COVID-19 Trends in Asia")
plt.xlabel("Countries")
plt.ylabel("Number of cases")
plt.savefig("country-trends.png")

#print report
print("The total number of cases in China is {}.\nThe total number of cases in India is {}.\nThe total number of cases in Singapore is {}.\nThe total number of cases in Japan is {}.".format(numc[2], numi[2], nums[2], numj[2]))
