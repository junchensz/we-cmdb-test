import csv

systemDesign_prefix = '0001'
subsysDesign_prefix = '0002'
subsys_prefix = '0007'
unit_prefix = '0008'
host_prefix = '0012'
networkSegment_prefix = '0021'
ip_prefix = '0014'
runningInstance_prefix = '0015'

def writeCsv(fileName,rows):
    csvFile = open(fileName,"a")
    writer = csv.writer(csvFile)
    for row in rows:
        writer.writerow(row)

def genGuid(prefix,index):
    return prefix+"_"+'{:0>10d}'.format(index)

def writeSystemDesign(startIndex,count):
    sampleRow = ['0001_0000000001','','0001_0000000001','umadmin','2019/9/9 2:12','umadmin','2019/9/4 21:21','DEMO','34','','DEMO','','','','105','demo system']
    rows=[]
    i = startIndex
    while i < startIndex + count:
        sampleRow[0] = genGuid(systemDesign_prefix,i)
        sampleRow[2] = genGuid(systemDesign_prefix,i)
        sampleRow[7] = 'Demo'+str(i)
        sampleRow[9] = 'Demo'+str(i)
        rows.append(sampleRow.copy())
        i = i +1


    writeCsv('system_design.csv',rows)

def writeSubSystemDesigin(systemDesign,startIndex,count):
    sampleRow = ['0002_0000000001','','0002_0000000001','umadmin','2019/9/4 21:25','umadmin','2019/9/4 21:25','DEMO-SUBSYS1','34','','SUBSYS1','','','','105','129','sub system','0001_0000000001']
    rows=[]
    i = startIndex
    while i < startIndex + count:
        sampleRow[0] = genGuid(subsysDesign_prefix,i)
        sampleRow[2] = genGuid(subsysDesign_prefix,i)
        sampleRow[7] = 'Demo_subsys_design_'+str(i)
        sampleRow[10] = 'Demo_subsys_design_'+str(i)
        sampleRow[17] = systemDesign
        rows.append(sampleRow.copy())
        i = i + 1

    writeCsv('subsys_design.csv',rows)

def writeSubSystem(subsysDesign,startIndex,count):
    sampleRow = ["0007_0000000001",'',"0007_0000000001","umadmin","2019-07-24 08:30:17","umadmin","2019-07-24 06:40:03","ECIF-CORE_PRD","37","2019-07-24 16:30:17","CORE","ECIF-CORE PRD",'','',"111","test","0002_0000000010"]
    rows=[]
    i = startIndex
    while i < startIndex + count:
        sampleRow[0] = genGuid(subsys_prefix,i)
        sampleRow[2] =  genGuid(subsys_prefix,i)
        sampleRow[7] = 'Demo_subsys_'+str(i)
        sampleRow[10] = 'Demo_subsys_'+str(i)
        sampleRow[16] = subsysDesign
        rows.append(sampleRow.copy())
        i = i + 1

    writeCsv('subsys.csv',rows)

def writeUnit(subsys,startIndex,count):
    sampleRow = ["0008_0000000001",'',"0008_0000000001","umadmin","2019-07-24 08:30:35","umadmin","2019-07-24 08:14:07","ECIF-CORE_PRD-APP","37","2019-07-24 16:30:35","APP","",'','',"1","","0007_0000000001","0003_0000000006"]
    rows=[]
    i = startIndex
    while i < startIndex + count:
        sampleRow[0] = genGuid(unit_prefix,i)
        sampleRow[2] = genGuid(unit_prefix,i)
        sampleRow[7] = 'Demo_unit_'+str(i)
        sampleRow[16] = subsys
        rows.append(sampleRow.copy())
        i = i + 1

    writeCsv('unit.csv',rows)

def writeRunningInstance(host,unit,startIndex,count):
    sampleRow = ["0015_0000000008","0015_0000000021","0015_0000000008","umadmin","2019-09-18 17:59:00","umadmin","2019-09-09 03:17:02","GZ3-SYSTEM-GZ3-SUBSYSTEM_STGi-GZ3-TEST_TEST-02","43","2019-09-18 17:59:00","TEST-02","TEST-02",'','',"","115","0012_0000000054","50","4","3","24595","174","0008_0000000008","306",'']
    rows=[]
    i = startIndex
    while i < startIndex + count:
        sampleRow[0] = genGuid(runningInstance_prefix,i)
        sampleRow[2] = genGuid(runningInstance_prefix,i)
        sampleRow[7] = 'Demo_running_instance_'+str(i)
        sampleRow[10] = 'Demo_running_instance_'+str(i)
        sampleRow[16] = host
        sampleRow[22] = unit
        rows.append(sampleRow.copy())
        i = i + 1

    writeCsv('running_instance.csv',rows)

def writeHost(ip,startIndex,count):
    guidIndex = '0012'
    sampleRow = ["0012_0000000031","0012_0000000043","0012_0000000031","umadmin","2019-08-30 00:35:49","umadmin","2019-08-26 03:13:45","TEST-250-02_10.250.1.2","44","","TEST-250-02","TEST-250-02","259","rAwq3wWh2Bl","ins-3yv1ur1i","115","167",'','',"0014_0000000079","TEST-250-02","164","0020_0000000017","162","","08069f86f35c68ba4491be5d90595d32",'','']
    rows=[]
    i = startIndex
    while i < startIndex + count:
        sampleRow[0] = genGuid(host_prefix,i)
        sampleRow[2] = genGuid(host_prefix,i)
        sampleRow[7] = 'Demo_host_'+str(i)
        sampleRow[10] = 'Demo_host_'+str(i)
        sampleRow[19] = ip
        rows.append(sampleRow.copy())
        i = i + 1

    writeCsv('host.csv',rows)

def writeIpAndHost(networkSenment,startIndex,count):
    #guidIndex = '0014'
    sampleRow = ["0014_0000000001",'',"0014_0000000001","umadmin","2019-09-08 15:40:02","umadmin","2019-07-24 11:40:31","10.0.16.1/24","37","","10.0.16.1","Demo DMZ proxy Gateway",'','',"0021_0000000006","172","0014_0000000001_ttt_10.0.16.1_0014_0000000001_10.0.16.0/24_VPC子网网段"]
    rows=[]
    i = startIndex
    while i < startIndex + count:
        ipGuid = ip_prefix+"_"+'{:0>10d}'.format(i)
        sampleRow[0] = ipGuid
        sampleRow[2] = ipGuid
        sampleRow[7] = 'Demo_ip_'+str(i)
        sampleRow[10] = 'Demo_ip_'+str(i)
        sampleRow[14] = networkSenment
        rows.append(sampleRow.copy())
        writeHost(ipGuid,i,1)
        i = i + 1

    writeCsv('ip_addr.csv',rows)


def writeNetworkSegment(startIndex,count):
    #guidIndex = '0021'
    sampleRow = ["0021_0000000001",'',"0021_0000000001","admin","2019-09-09 07:52:55","umadmin","2019-07-24 11:25:55","10.0.0.0/16_idc segment","37","2019-09-09 15:52:55","10.0.0.0/16","demo",'','',"","","","16","demo","179"]
    rows=[]
    i = startIndex
    while i < startIndex + count:
        sampleRow[0] = networkSegment_prefix+"_"+'{:0>10d}'.format(i)
        sampleRow[2] = networkSegment_prefix+"_"+'{:0>10d}'.format(i)
        sampleRow[7] = 'Demo_network_segment_'+str(i)
        sampleRow[10] = 'Demo_network_segment_'+str(i)
        sampleRow[11] = 'Demo_network_segment_'+str(i)
        rows.append(sampleRow.copy())
        i = i + 1

    writeCsv('network_segment.csv',rows)



networkSegmentCount = 1000
ipCountPerNetworkSeg = 50
ipCount = networkSegmentCount * ipCountPerNetworkSeg #host count is same

writeNetworkSegment(1,networkSegmentCount)
for i in range(networkSegmentCount):
    networkSegmentGuid = genGuid(networkSegment_prefix,i+1)
    ipStart = ipCountPerNetworkSeg * i +1 
    writeIpAndHost(networkSegmentGuid,ipStart,ipCountPerNetworkSeg)

systemDesignCount = 10
subSystemDesignCountPerSystemDesign = 10
unitCountPerSubsys = 3
unitCount = systemDesignCount * subSystemDesignCountPerSystemDesign * unitCountPerSubsys

unitStart = 1
subsysStart = 1
subSysDesignStart = 1

writeSystemDesign(1,systemDesignCount)
for i in range(systemDesignCount): # 0 -> 10
    systemDesign = genGuid(systemDesign_prefix,i+1)
    writeSubSystemDesigin(systemDesign,subSysDesignStart, subSystemDesignCountPerSystemDesign)

    subsysPerSubsysDesign = 10
    for j in range(subSystemDesignCountPerSystemDesign): # 0 -> 10
        subsysDesign = genGuid(subsysDesign_prefix, subSysDesignStart + j)
        writeSubSystem(subsysDesign, subsysStart, subsysPerSubsysDesign)

        for k in range(subsysPerSubsysDesign):
            subsys = genGuid(subsys_prefix, subsysStart + k)
            writeUnit(subsys, unitStart, unitCountPerSubsys)
            unitStart = unitStart + unitCountPerSubsys

        subsysStart = subsysStart + subsysPerSubsysDesign
    subSysDesignStart = subSysDesignStart + subSystemDesignCountPerSystemDesign

hostCountPerUnit = int(ipCount / unitCount)
for i in range(unitCount):
    for j in range(hostCountPerUnit):
        hostIndex = i * hostCountPerUnit  +j + 1
        unit = genGuid(unit_prefix, i +1)
        host = genGuid(host_prefix, hostIndex )
        writeRunningInstance(host,unit,hostIndex, 1 )





