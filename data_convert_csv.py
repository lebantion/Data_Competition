import pandas as pd


def main():
    # Reading CSV files
    dataFile = "Data_From_Honda.xlsx"

    print("Reading excel file... Wait for a min...")
    org = pd.read_excel(dataFile, sheet_name='organization')
    route = pd.read_excel(dataFile, sheet_name='route')
    tripRq = pd.read_excel(dataFile, sheet_name='trip_request')
    vehicle = pd.read_excel(dataFile, sheet_name='vehicle')
    tripSum = pd.read_excel(dataFile, sheet_name='trip_summary')
    print("Reading excel file complete")

    switch = True

    while switch:
        print("Please Select the task that you want to do")
        print("1) excel file to csv file")
        print("2) find info from csv files")
        print("3) exit")
        selected = input("Input the number: ")

        if selected == "1":
            data_convert(org, route, tripRq, vehicle, tripSum)
        elif selected == "2":
            get_info(org, route, tripRq, vehicle, tripSum)
        else:
            switch = False


def data_convert(org, route, tripRq, vehicle, tripSum):
    # Opening a output csv file in write mode
    org.to_csv("csv/organization.csv", index=False, header=True)
    route.to_csv("csv/route.csv", index=False, header=True)
    tripRq.to_csv("csv/trip_request.csv", index=False, header=True)
    vehicle.to_csv("csv/vehicle.csv", index=False, header=True)
    tripSum.to_csv("csv/trip_summary.csv", index=False, header=True)


def get_info(org, route, tripRq, vehicle, tripSum):
    print("Driver ID is key")
    driver_IDSet = set((tripSum["driver_id"]))

    for key in driver_IDSet:
        # merge route, trip_summary and vehicle_id
        driver_data = route[route["driver_id"] == key]
        driver_data = pd.merge(driver_data, vehicle, on='vehicle_id')

        driver_data2 = tripSum[tripSum["driver_id"] == key]
        driver_data = pd.merge(driver_data, driver_data2, on='route_id')

        driver_data = driver_data.drop_duplicates()
        driver_data = driver_data.T.drop_duplicates().T

        driver_data.to_csv("csv/filtered/Driver{}.csv".format(key), index=False, header=True)

    org_IDSet = set((tripRq["organization_id"]))

    for key in org_IDSet:
        # merge trip_Request and Organization
        org_Data = tripRq[tripRq["organization_id"] == key]
        org_Data2 = org[org["organization_id"] == key]

        result = pd.merge(org_Data, org_Data2, on='organization_id')
        result.to_csv("csv/filtered/tripRqWithOrg{}.csv".format(key), index=False, header=True)

main()
