import pandas as pd


def main():
    switch = True

    while switch:
        print("Please Select the task that you want to do")
        print("1) excel file to csv file")
        print("2) find info from csv files")
        print("3) exit")
        selected = input("Input the number")

        if selected is 1:
            data_convert()
        elif selected is 2:
            get_info()
        else:
            switch = False


def data_convert():
    dataFile = "Data_From_Honda.xlsx"

    # creating or loading an excel workbook

    org = pd.read_excel(dataFile, sheet_name='organization')
    route = pd.read_excel(dataFile, sheet_name='route')
    tripRq = pd.read_excel(dataFile, sheet_name='trip_request')
    vehicle = pd.read_excel(dataFile, sheet_name='vehicle')
    tripSum = pd.read_excel(dataFile, sheet_name='trip_summary')

    # Opening a output csv file in write mode
    org.to_csv("csv/organization.csv", index=False, header=True)
    route.to_csv("csv/route.csv", index=False, header=True)
    tripRq.to_csv("csv/trip_request.csv", index=False, header=True)
    vehicle.to_csv("csv/vehicle.csv", index=False, header=True)
    tripSum.to_csv("csv/trip_summary.csv", index=False, header=True)


def get_info():
    # Reading CSV files
    org_Data = pd.read_csv("csv/organization.csv")
    route_Data = pd.read_csv("csv/route.csv")
    trip_RQ_Data = pd.read_csv("csv/trip_request.csv")
    trip_SUM_Data = pd.read_csv("csv/trip_summary.csv")
    vehicle_Data = pd.read_csv("csv/vehicle.csv")


