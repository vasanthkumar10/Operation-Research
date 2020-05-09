
# Program to find the optimized selection of machines
# Given : machines and cost of operation per hr
# Input : no of units required and hrs
# Country : New York, India and China
# Output : region, total cost, machines
# Writer : Vasanthkumar V (09/05/2020)


# declaration of table data

machines = {
    "large" : 10,
    "xlarge" : 20,
    "2xlarge" : 40,
    "4xlarge" : 80,
    "8xlarge" : 160,
    "10xlarge" : 320
}

newYork = {
    "name" : "New York",
    "large" : 120,
    "xlarge" : 230,
    "2xlarge" : 450,
    "4xlarge" : 774,
    "8xlarge" : 1400,
    "10xlarge" : 2820
}

india = {
    "name" : "India",
    "large" : 140,
    "xlarge" : 0,
    "2xlarge" : 413,
    "4xlarge" : 890,
    "8xlarge" : 1300,
    "10xlarge" : 2970
}

china = {
    "name" : "China",
    "large" : 110,
    "xlarge" : 200,
    "2xlarge" : 0,
    "4xlarge" : 670,
    "8xlarge" : 1180,
    "10xlarge" : 0
}

result = {
    "output" : []
}

# getting units and hrs from user
units = input("enter the units to be produced : ")
hrs = input("enter the hrs : ")

# machine count function
def countMachine(units,min,country):
    count = 0
    # 1150-160-->990...upto units>=160
    while(int(units) >= int(machines[min])):
        units = int(units) - int(machines[min])
        count += 1
    return (units,count,count*country[min])

# finding optimization core logic
def costFinder(country,units,hrs):
    machine = []
    i = 0
    totalCost = 0

    # core logic
    dictionary = dict(
        (k, (float(country[k]) * int(hrs)) / machines[k]) for k in
        machines)
    dictionary = {k: v for k, v in
                       sorted(dictionary.items(), key=lambda item: item[
                           1])}

    # removing zero value pair in dictionary
    dictionary = {x: y for x, y in dictionary.items() if y != 0}

    # calling countMachine function
    keys = list(dictionary.keys())
    while (units != 0):
        min = keys[i]
        (units,count,cost) = countMachine(units, min,country)
        i += 1
        if(count>0):
            machine.append((min,count))

    # finding total cost
        totalCost += cost

    # appending attributes to the dictionary
    result["output"].append({
        "region" : country["name"],
        "totalCost" : totalCost,
        "machines" : machine
       })

# calling costFinder
costFinder(newYork,units,hrs)
costFinder(india,units,hrs)
costFinder(china,units,hrs)

# output
print(result)