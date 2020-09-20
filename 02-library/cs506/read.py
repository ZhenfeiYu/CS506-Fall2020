def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path,"r+") as f:
        lines =  f.readlines()
        for line in lines:
            res.append([x for x in line.strip().split(",")])
        for i in range(0, len(res)):
            for j in range(0,len(res[i])):
                if res[i][j][0] in ["0","1","2","3","4","5","6","7","8","9"]:
                    res[i][j] = int(res[i][j])
                else:
                    res[i] = [item.replace('"','') for item in res[i]]
            
    return res


        
